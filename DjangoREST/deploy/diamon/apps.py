from django.apps import AppConfig
import html
import pathlib
import os


class WebappConfig(AppConfig):
    name = 'diamon'
    MODEL_PATH = Path('model')

"""
class DiamonConfig(AppConfig):
    name = 'diamon'
"""