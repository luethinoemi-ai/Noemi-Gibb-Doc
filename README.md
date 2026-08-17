# Noemi-Gibb-Doc

A personal documentation project built with Sphinx.

## Overview

This repository contains school notes, learning material, and personal documentation created during my apprenticeship as a software developer.

The project is built with Sphinx and automatically deployed to GitHub Pages using GitHub Actions.

## Documentation

Website:

https://luethinoemi-ai.github.io/Noemi-Gibb-Doc/

Repository:

https://github.com/luethinoemi-ai/Noemi-Gibb-Doc

## Features

- Shibuya theme
- Dark mode support
- GitHub integration
- Mermaid diagrams
- Markdown support
- Copy button for code blocks
- GitHub Actions deployment
- GitHub Pages hosting

## Extensions

- myst-parser
- sphinx-copybutton
- sphinx-design
- sphinx-tabs
- sphinx-togglebutton
- sphinxcontrib-mermaid
- sphinx.ext.todo

## Project Structure

```text
Noemi-Gibb-Doc
├── .github/
│   └── workflows/
├── docs/
│   ├── Module/
│   ├── Semester-03/
│   ├── _static/
│   └── _templates/
├── README.md
├── requirements.txt
├── conf.py
├── index.rst
├── Makefile
└── make.bat
```

## Installation

Clone the repository:

```bash
git clone https://github.com/luethinoemi-ai/Noemi-Gibb-Doc.git
cd Noemi-Gibb-Doc
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Build Documentation

Build the documentation locally:

```bash
make html
```

Open:

```text
_build/html/index.html
```

## Deployment

The documentation is automatically built and published through GitHub Actions whenever changes are pushed to the repository.

## Author

Noemi Lüthi

Software Development Apprentice
