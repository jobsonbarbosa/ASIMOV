from pathlib import Path
from werkzeug.security import generate_password_hash, check_password_hash

from sqlalchemy import create_engine, String, Boolean, Integer, select, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship

pasta_atual = Path(__file__).parent
PATH_TO_BD = pasta_atual / 'bd_usuarios.sqlite'

class Base(DeclarativeBase):
    pass

# Tabela de Usuários
class UsuarioFerias(Base):
    __tablename__ = 'usuarios_ferias'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(30))
    senha: Mapped[str] = mapped_column(String(128))
    email: Mapped[str] = mapped_column(String(30))
    acesso_gestor: Mapped[bool] = mapped_column(Boolean(), default=False)
    inicio_na_empresa: Mapped[str] = mapped_column(String(30))
    eventos_ferias: Mapped[list['EventosFerias']] = relationship(
        back_populates='parent',
        lazy='subquery'
    )
    
    def __repr__(self):
        return f"Usuário({self.id=}, {self.nome=})"
    
    def define_senha(self, senha):
        self.senha = generate_password_hash(senha)
    
    def verifica_senha(self, senha):
        return check_password_hash(self.senha, senha)

# Tabela de Ferias  
class EventosFerias(Base):
    __tablename__ = 'eventos_ferias'
    id: Mapped[int] = mapped_column(primary_key=True)
    parent_id: Mapped[int] = mapped_column(ForeignKey('usuarios_ferias.id')) # referencia o usuário da tabela UsuarioFerias
    parent: Mapped['UsuarioFerias'] = relationship(lazy='subquery') # Deixa explicito que há uma relação entre tabelas
    inicio_ferias: Mapped[str] =  mapped_column(String(30))
    fim_ferias: Mapped[str] = mapped_column(String(30))
    total_dias: Mapped[int] = mapped_column(Integer())
    
engine = create_engine(f'sqlite:///{PATH_TO_BD}')
Base.metadata.create_all(bind=engine)


# CRUD =============================== #

def cria_usuario(
    nome,
    senha,
    email,
    acesso_gestor=False
):
    with Session(bind=engine) as session:
        usuario = Usuario(
            nome=nome,
            email=email,
            acesso_gestor=acesso_gestor
        )
        usuario.define_senha(senha)
        session.add(usuario)
        session.commit()

def le_todos_usuarios():
    with Session(bind=engine) as session:
        comando_sql = select(Usuario)
        usuarios = session.execute(comando_sql).fetchall()
        usuarios = [user[0] for user in usuarios]
        return usuarios

def le_usuario_por_id(id):
    with Session(bind=engine) as session:
        comando_sql = select(Usuario).filter_by(id=id)
        usuarios = session.execute(comando_sql).fetchall()
        return usuarios[0][0]
    
def modifica_usuario(
        id, 
        **kwargs

        ):
    with Session(bind=engine) as session:
        comando_sql = select(Usuario).filter_by(id=id)
        usuarios = session.execute(comando_sql).fetchall()
        for usuario in usuarios:  
            for key, value in kwargs.items():
                if key == 'senha':
                    usuario[0].define_senha(value)
                else:
                    setattr(usuario[0], key, value)

        session.commit()
    
def deleta_usuario(id):
    with Session(bind=engine) as session:
        comando_sql = select(Usuario).filter_by(id=id)
        usuarios = session.execute(comando_sql).fetchall()
        for usuario in usuarios:
            session.delete(usuario[0])
        session.commit()

if __name__ == '__main__':
    
    cria_usuario(
        nome='Ana Carolina Barbosa',
        senha='senhafacilsempre',
        email='anacarolinadejesusbarbosa@gmail.com',
        acesso_gestor=False,
    )

    
    # ===== verifica senha ====
    
    usuario_jobson = le_usuario_por_id(id=1)
    print(usuario_jobson.verifica_senha('1234567'))