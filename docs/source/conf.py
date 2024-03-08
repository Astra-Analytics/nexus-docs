# Configuration file for the Sphinx documentation builder.

# -- Project information

project = "NexusDB API Documentation"
copyright = "2021, Astra Analytics, Inc."
author = "Astra Analytics, Inc."

release = "0.1"
version = "0.1.0"

# -- General configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "sphinxawesome_theme.highlighting",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

# -- Options for HTML output

html_theme = "sphinxawesome_theme"
html_favicon = "favicon.ico"

# -- Options for EPUB output
epub_show_urls = "footnote"
