# AI-Engineer-Journey

A Python project focused on building practical software engineering skills for AI Engineering.

This project covers Python fundamentals, object-oriented programming, dataclasses, type hints, modular code organization, JSON and CSV processing, error handling, logging, and automated testing.

## Project Structure

```text
AI-Engineer-Journey/
│
├── archive/     # Previous exercises and practice files
├── data/        # CSV and JSON data files
├── src/         # Application source code
├── tests/       # Automated tests
│
├── pytest.ini   # Pytest configuration
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/alvanoghlu/AI-Engineer-Journey.git
cd AI-Engineer-Journey
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Usage

Run the grade CLI application:

```bash
python src/grade_cli.py average
```

## Testing

Run all tests:

```bash
python -m pytest
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
```
