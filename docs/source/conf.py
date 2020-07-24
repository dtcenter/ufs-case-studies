# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'Case Studies for UFS Weather Model'
copyright = '2020 '
author = 'Xia Sun'

# The full version, including alpha/beta/rc tags
release = '0.1'

rst_epilog = "\n.. include:: .special.rst\n"
# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
#extensions = [
#]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []
pygments_style = 'sphinx'
#autodoc_mock_imports = ['sphinx_copybutton']
# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#import sphinx_rtd_theme
master_doc = 'index'
extensions = [
    'sphinx_copybutton',
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.autodoc',
    'sphinx_gallery.gen_gallery',
#    'sphinx_rtd_theme',
#    'sphinx_gallery.gen_gallery',
#    'sphinx-prompt',
]
#extensions = ['sphinx.ext.autosectionlabel',]

#    ...
#    "sphinx_rtd_theme",
#]

sphinx_gallery_conf = {
     'examples_dirs': '../examples',   # path to your example scripts
#     'gallery_dirs': 'auto_examples',  # path to where to save gallery generated output
}

def setup(app):
    app.add_stylesheet('custom.css') 
latex_engine = 'pdflatex'
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
    #  'maketitle': r'\newcommand\sphinxbackoftitlepage{For referencing this document please use: \newline \break Author1, Author2,, 2020. UFS Medium-Range Weather App Users Guide v1.0.0. 91pp. Available at https://ufscommunity.org.}\sphinxmaketitle'
}

html_theme = "sphinx_rtd_theme"
html_theme_options = {"body_max_width": "none"}
html_sidebars = {}
epub_title = project
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
