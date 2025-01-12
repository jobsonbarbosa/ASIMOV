import flet as ft

def main(page: ft.Page):
    page.title = "Lista de Tarefas"
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Lista(vazia) que armazenará as tarefas
    tarefas = []

    # Função para adicionar tarefa
    def adicionar_tarefa(e):
        if campo_tarefa.value.strip() != "":  
            tarefas.append(campo_tarefa.value.strip())
            lista_tarefas.controls.append(ft.Text(campo_tarefa.value.strip()))
            campo_tarefa.value = ""  
            lista_tarefas.update()
            campo_tarefa.update()

    # Campo de entrada de texto para o nome da tarefa
    campo_tarefa = ft.TextField(label="Digite o nome da tarefa", width=300)

    # Botão para adicionar a tarefa
    botao_adicionar = ft.ElevatedButton("Adicionar Tarefa", on_click=adicionar_tarefa)

    # Lista que exibirá as tarefas
    lista_tarefas = ft.Column()

    # Adiciona os componentes à página
    page.add(
        ft.Row([campo_tarefa, botao_adicionar], alignment=ft.MainAxisAlignment.CENTER),
        lista_tarefas,
    )

# Inicia a aplicação
ft.app(target=main)
