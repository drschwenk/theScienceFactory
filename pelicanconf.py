#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Dustin Schwenk'
# SITETITLE = u'The Science Factory'
SITENAME = u'The Science Factory'

SITESUBTITLE = u''
THEME = '/Users/schwenk/projects/sf_Blog/custom_themes/gum'
SITELOGO = './images/me_late_2015.jpg'


PATH = 'content'
DISPLAY_PAGES_ON_MENU = True
PAGE_PATHS = ['pages']
DEFAULT_CATEGORY = 'random'

TIMEZONE = 'America/Los_Angeles'

TYPOGRIFY = True
HIDE_SIDEBAR = True
GITHUB_URL = 'https://github.com/drschwenk'
DEFAULT_LANG = u'en'

SOCIAL = (('linkedin', 'https://www.linkedin.com/in/dustinschwenk'),
          ('github', 'https://github.com/drschwenk'))

# MENUITEMS = (('Archives', '/archives.html'),
#              ('Categories', '/categories.html'),
#              ('Tags', '/tags.html'),)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = ['images', 'pdfs','notebooks', 'code', 'templates']

CODE_DIR = 'code'
NOTEBOOK_DIR = 'notebooks'

#EXTRA_HEADER = open('_nb_header.html').read().decode('utf-8')

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video', 'assets',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'liquid_tags.literal', 'render_math', 'pelican_dynamic']


DEFAULT_PAGINATION = 5