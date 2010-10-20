# -*- coding: utf-8 -*-
#
# python-gammu documentation build configuration file, created by
# sphinx-quickstart on Tue Mar 10 18:14:17 2009.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# The contents of this file are pickled, so don't put values in the namespace
# that aren't pickleable (module imports are okay, they're removed automatically).
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# Change what .. option:: parses
import sphinx.domains.std
import re

def gammu_process_link(self, env, refnode, has_explicit_title, title, target):
    program = env.temp_data.get('std:program')
    if not has_explicit_title:
        if ' ' in title and not (title.startswith('/') or
                                 title.startswith('-')):
            program, target = re.split(' (?=-|--|/)?', title, 1)
            program = sphinx.domains.std.ws_re.sub('-', program)
            target = target.strip()
    elif ' ' in target:
        program, target = re.split(' (?=-|--|/)?', target, 1)
        program = sphinx.domains.std.ws_re.sub('-', program)
    refnode['refprogram'] = program
    return title, target

sphinx.domains.std.option_desc_re = re.compile(
    r'((?:/|-|--|^)[-_a-zA-Z0-9]+)(\s*.*?)(?=,\s+(?:/|-|--)|$)')
sphinx.domains.std.OptionXRefRole.process_link = gammu_process_link

# If your extensions are in another directory, add it here. If the directory
# is relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
sys.path.insert(0, '@CMAKE_CURRENT_BINARY_DIR@/../../python')
sys.path.append('@Gammu_SOURCE_DIR@/external/breathe')
sys.path.append('@CMAKE_CURRENT_SOURCE_DIR@')

# General configuration
# ---------------------

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 'breathe', 'configext', 'sphinx.ext.graphviz']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['@CMAKE_CURRENT_SOURCE_DIR@/.templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Gammu'
copyright = u'2009-2010, Michal Čihař <michal@cihar.com>'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '@VERSION@'
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
#unused_docs = []

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = ['.build']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# Options for HTML output
# -----------------------

# The style sheet to use for HTML and HTML Help pages. A file of that name
# must exist either in Sphinx' static/ path, or in one of the custom paths
# given in html_static_path.
html_style = 'default.css'

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['@CMAKE_CURRENT_SOURCE_DIR@/doc/.static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_use_modindex = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, the reST sources are included in the HTML build as _sources/<name>.
#html_copy_source = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'gammudoc'


# Options for LaTeX output
# ------------------------

# The paper size ('letter' or 'a4').
latex_elements = {
    'papersize': 'a4',
}

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, document class [howto/manual]).
latex_documents = [
  ('contents', 'gammu.tex', ur'Gammu Manual',
   ur'Michal Čihař <michal@cihar.com>', 'manual', True),
  ('smsd/index', 'smsd.tex', ur'Gammu SMSD Daemon Manual',
   ur'Michal Čihař <michal@cihar.com>', 'manual', True),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
latex_domain_indices = True

# Options for breathe extension
# -----------------------------

breathe_projects = {
    'api':'@DOXYGEN_OUTPUT@/xml',
    }

breathe_default_project = 'api'


man_pages = [
    ('smsd/files', 'gammu-smsd-files', 'gammu-smsd(1) backend using filesystem as a message storage', u'Michal Čihař <michal@cihar.com>', 7),
    ('smsd/tables', 'gammu-smsd-tables', 'description of tables for database backends of gammu-smsd(1)', u'Michal Čihař <michal@cihar.com>', 7),
    ('smsd/mysql', 'gammu-smsd-mysql', 'gammu-smsd(1) backend using MySQL database server as a message storage', u'Michal Čihař <michal@cihar.com>', 7),
    ('smsd/pgsql', 'gammu-smsd-pgsql', 'gammu-smsd(1) backend using PostgreSQL database server as a message storage', u'Michal Čihař <michal@cihar.com>', 7),
    ('smsd/dbi', 'gammu-smsd-dbi', 'gammu-smsd(1) backend using DBI abstraction layer to use any supported database as a message storage', u'Michal Čihař <michal@cihar.com>', 7),
    ('smsd/run', 'gammu-smsd-run', 'documentation for RunOnReceive directive', u'Michal Čihař <michal@cihar.com>', 7),
    ('smsd/null', 'gammu-smsd-null', 'gammu-smsd(1) backend not storing messages', u'Michal Čihař <michal@cihar.com>', 7),
    ('smsd/config', 'gammu-smsdrc', 'gammu-smsd(1) configuration file', u'Michal Čihař <michal@cihar.com>', 5),
    ('smsd/inject', 'gammu-smsd-inject', 'Inject messages into queue of SMS daemon for Gammu', u'Michal Čihař <michal@cihar.com>', 1),
    ('smsd/monitor', 'gammu-smsd-monitor', 'Monitor state of SMS daemon for Gammu', u'Michal Čihař <michal@cihar.com>', 1),
    ('smsd/smsd', 'gammu-smsd', 'SMS daemon for Gammu', u'Michal Čihař <michal@cihar.com>', 1),
    ('config/index', 'gammurc', 'gammu(1) configuration file', u'Michal Čihař <michal@cihar.com>', 5),
    ('gammu/index', 'gammu', 'Does some neat things with your cellular phone or modem.', u'Michal Čihař <michal@cihar.com>', 1),
    ('formats/backup', 'gammu-backup', 'gammu(1) backup file format.', u'Michal Čihař <michal@cihar.com>', 5),
]

