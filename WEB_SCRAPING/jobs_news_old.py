from scraping_sites.site_old import *
import os
from threading import Thread
import time
from datetime import datetime
import sys
import pickle
import webbrowser
from math import ceil

from pytimedinput import timedInput

class JobsNews:
    def __init__(self):
        self.dict_site = {}
        self.all_sites = ['veja', 'r7', 'cnn', 'globo']

        self.screen = 0

        self.news = self._read_file('news') if 'news' is os.listdir() else []
        self.sites = self._read_file('site') if 'site' is os.listdir() else []
    
    def _update_file(self, lista, mode='news'):
        with open(mode, 'wb') as fp:
            pickle.dump(lista, fp)
    
    def _read_file(self, mode='news'):
        with open(mode, 'rb') as fp:
            n_list = pickle.load(fp)
            return n_list

self = JobsNews()