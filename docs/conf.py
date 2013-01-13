# from path import path
# import logging
import sphinx
# import sys
# from setuptools import find_packages

release = ''
project = 'SevSeg'
author = ''
copyright = ''

# logging.basicConfig(level=logging.DEBUG)

# Extension
extensions = [
    #    'sphinxcontrib.programoutput',
    'sphinxcontrib.programscreenshot',
    'sphinxcontrib.gtkwave',
    #    'sphinx.ext.graphviz',
    #'sphinx.ext.autosummary',
]

# Source
master_doc = 'index'
templates_path = ['_templates']
source_suffix = '.rst'
exclude_trees = []
pygments_style = 'sphinx'

# html build settings
html_theme = 'default'
html_static_path = ['_static']

# htmlhelp settings
htmlhelp_basename = '%sdoc' % project
