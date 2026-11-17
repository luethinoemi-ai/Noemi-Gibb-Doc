# Noemi GIBB Doc

Personal documentation created during my apprenticeship as an application developer.

It contains school notes and learning material, organized by module and semester. The content is written with Sphinx and the Shibuya theme.

**Read online:** https://luethinoemi-ai.github.io/Noemi-Gibb-Doc/

## Contents

- **Module:** notes and summaries for each school module
- **Semester 3:** material from the current semester

## Features

- Shibuya theme with dark mode
- GitHub integration
- Markdown support (MyST)
- Mermaid diagrams
- Copy button for code blocks
- Automatic deployment to GitHub Pages

Extensions: myst-parser, sphinx-copybutton, sphinx-design, sphinx-tabs, sphinx-togglebutton, sphinxcontrib-mermaid, sphinx.ext.todo

## Build locally

You only need this if you want to work on the docs yourself.

```bash
git clone https://github.com/luethinoemi-ai/Noemi-Gibb-Doc.git
cd Noemi-Gibb-Doc
pip install -r requirements.txt
make html
```

The result is in `_build/html/index.html`.

## Project structure

```text
Noemi-Gibb-Doc/
├── .github/workflows/   deployment to GitHub Pages
├── docs/
│   ├── Module/          notes per module
│   ├── Semester-03/     material from semester 3
│   ├── _static/
│   └── _templates/
├── conf.py              Sphinx configuration
├── index.rst            start page
├── requirements.txt
├── Makefile
└── README.md
```

## Deployment

The website is built and published automatically with GitHub Actions on every push.

## Author

Noemi, application development apprentice.
GitHub: [@luethinoemi-ai](https://github.com/luethinoemi-ai)
