#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Fallen70'
SITENAME = 'WorkBook'
THEME = "./theme/"

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'
# On Unix/Linux
DATE_FORMATS = {
    'fr': ( "fr_FR.UTF-8" , "%d-%b-%Y" ),
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('Pagefind', 'https://pagefind.app/'),)

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False

STATIC_PATHS = ['images']

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
