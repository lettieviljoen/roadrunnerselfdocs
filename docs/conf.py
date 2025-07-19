# conf.py

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'Roadrunner Self'
copyright = '2025'
author = 'Gert Vlok'

# -- General configuration ---------------------------------------------------

extensions = []

templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

html_theme = 'alabaster'  # You can change this to 'sphinx_rtd_theme' or any other

html_static_path = ['_static']
