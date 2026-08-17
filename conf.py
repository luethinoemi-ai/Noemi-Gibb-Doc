html_theme_options = {
    "github_url": "https://github.com/luethinoemi-ai/Noemi-Gibb-Doc",
}

#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Noemi-Gibb-Doc'
copyright = '2026, Noemi Lüthi'
author = 'Noemi Lüthi'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_copybutton",
    "sphinx_design",
    "sphinxcontrib.mermaid",
    "myst_parser",
    "sphinx.ext.todo",
    "sphinx_tabs.tabs",
]

todo_include_todos = True

templates_path = ['docs/_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = "shibuya"

html_favicon = "docs/_static/n.logo.png"

html_static_path = ['docs/_static']

html_context = {
    "source_type": "github",
    "source_user": "luethinoemi-ai",
    "source_repo": "Noemi-Gibb-Doc",
    "source_version": "main",
    "source_docs_path": "/docs/",
}

html_sidebars = {
    "**": [
        "sidebars/localtoc.html",
        "sidebars/edit-this-page.html",
    ]
}

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
