# AI-Engineer-Journey

## Overview

A Python project focused on building practical software engineering skills for AI Engineering.

This project covers Python fundamentals, object-oriented programming, dataclasses, type hints, modular code organization, JSON and CSV processing, error handling, logging, and automated testing.

The Grade Manager CLI application analyzes student grades from CSV files and provides average, top, and summary operations.

## Installation

Clone the repository:

```bash
git clone https://github.com/alvanoghlu/AI-Engineer-Journey.git
cd AI-Engineer-Journey
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Usage

Run the application using the following commands:

Calculate student averages:

```bash
python src/grade_cli.py average --file data/grades.csv
```

Find the top student:

```bash
python src/grade_cli.py top --file data/grades.csv
```

Display a summary of student grades:

```bash
python src/grade_cli.py summary --file data/grades.csv
```

Display available commands and options:

```bash
python src/grade_cli.py --help
```

## Project Structure

```text
AI-Engineer-Journey/
│
├── archive/          # Previous exercises and practice files
├── data/             # CSV and JSON data files
├── src/              # Application source code
├── tests/            # Automated tests
│
├── pytest.ini        # Pytest configuration
├── requirements.txt  # Project dependencies
└── README.md         # Project documentation
```

## Tests

Run all automated tests:

```bash
python -m pytest -v
```

## Code Quality

Check code quality with Ruff:

```bash
python -m ruff check .
```

Format code with Ruff:

```bash
python -m ruff format .
```

Check type hints with Mypy:

```bash
python -m mypy .
``