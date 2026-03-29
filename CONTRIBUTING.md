# Contributing

Contributions are welcome! Please follow these steps.

## Setup

```bash
git clone https://github.com/aayodejii/django-affiliate-system.git
cd django-affiliate-system
python -m venv venv
source venv/bin/activate
pip install -e ".[dev]"
```

## Running Tests

Tests live in `django_affiliate_system/tests.py`. Run them with:

```bash
pytest django_affiliate_system/tests.py
```

Or with coverage:

```bash
pytest django_affiliate_system/tests.py --cov=django_affiliate_system --cov-report=term-missing
```

## Code Style

This project uses [black](https://black.readthedocs.io/) and [isort](https://pycqa.github.io/isort/). Format your code before submitting:

```bash
black django_affiliate_system/
isort django_affiliate_system/
```

## Submitting a Pull Request

1. Fork the repository and create a feature branch from `main`
2. Add tests for any new behaviour
3. Ensure all tests pass
4. Submit a pull request with a clear description of the change

## Reporting Issues

Open an issue at https://github.com/aayodejii/django-affiliate-system/issues
