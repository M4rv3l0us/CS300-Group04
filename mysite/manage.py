#!/usr/bin/env python
"""
manage.py: A command-line utility that lets you interact with this Django project in various ways.
You can read all the details about manage.py in django-admin and manage.py.
"""
"""Django's command-line utility for administrative tasks."""
import os
import sys
sys.path.append(r'D:\My stuffs\Software Engineering\mysite\mysite')


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.base")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed " 
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
