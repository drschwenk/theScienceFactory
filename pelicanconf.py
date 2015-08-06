#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Dustin Schwenk'
SITENAME = u'The Science Factory'
SITESUBTITLE = u''
THEME = "/Users/schwenk/Metis/sf_Blog/custom_themes/gum"


PATH = 'content'
DISPLAY_PAGES_ON_MENU = True
PAGE_PATHS = ['pages']
DEFAULT_CATEGORY = 'random'

TIMEZONE = 'America/New_York'

TYPOGRIFY = True
HIDE_SIDEBAR = True
GITHUB_URL = 'https://github.com/schwenkmetis'
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['images', 'pdfs','notebooks', 'code']

CODE_DIR = 'code'
NOTEBOOK_DIR = 'notebooks'

#EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'liquid_tags.literal', 'render_math','pelican_dynamic']

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('Github', 'https://github.com/schwenkmetis'),
#           ('LinkedIn', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# MENUITEMS = (('Pelican', 'http://getpelican.com/')
#             ('Python.org', 'http://python.org/'),
