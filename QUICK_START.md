# Quick Start Commands

## Initial Setup

### 1. Create Package Structure

```bash
# Create main directory
mkdir django-affiliate-system
cd django-affiliate-system

# Create package directories
mkdir -p django_affiliate_system/{services,migrations,templates,static}
mkdir -p tests
mkdir -p docs

# Create __init__ files
touch django_affiliate_system/__init__.py
touch django_affiliate_system/services/__init__.py
touch django_affiliate_system/migrations/__init__.py
touch tests/__init__.py
```

### 2. Copy Your Files

```bash
# From your existing project, copy files to django_affiliate_system/
# - models.py
# - views.py
# - serializers.py
# - authentication.py
# - permissions.py
# - middleware.py
# - signals.py
# - tasks.py
# - urls.py
# - admin.py (or create utils.py with your auto-admin code)

# Copy service files
# - services/tracking.py
# - services/commissions.py
```

### 3. Create Package Files

```bash
# Download or create these files in the root directory
touch setup.py
touch setup.cfg
touch pyproject.toml
touch MANIFEST.in
touch README.md
touch LICENSE
touch CHANGELOG.md
touch requirements.txt
touch .gitignore

# Create version file
touch django_affiliate_system/__version__.py
touch django_affiliate_system/apps.py
```

### 4. Update All Imports

Use find and replace:

```bash
# Find all Python files and update imports
find django_affiliate_system -name "*.py" -type f -exec sed -i.bak \
  's/from affiliate_system\.core/from django_affiliate_system/g' {} +

find django_affiliate_system -name "*.py" -type f -exec sed -i.bak \
  's/import affiliate_system\.core/import django_affiliate_system/g' {} +

# Clean up backup files
find . -name "*.bak" -delete
```

## Development Commands

### Install in Development Mode

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install package in editable mode
pip install -e .

# Or with all extras
pip install -e ".[all]"
```

### Run Tests

```bash
# Install test dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run with coverage
pytest --cov=django_affiliate_system --cov-report=html

# Run specific test
pytest tests/test_models.py

# Run with verbose output
pytest -v

# View coverage report
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
start htmlcov/index.html  # Windows
```

### Code Quality

```bash
# Format code with black
black django_affiliate_system/ tests/

# Sort imports
isort django_affiliate_system/ tests/

# Lint with flake8
flake8 django_affiliate_system/

# Type checking with mypy
mypy django_affiliate_system/

# Run all quality checks
black . && isort . && flake8 && mypy django_affiliate_system/
```

## Building and Publishing

### Build Package

```bash
# Clean old builds
rm -rf build/ dist/ *.egg-info/
find . -type d -name __pycache__ -exec rm -r {} +
find . -type f -name '*.pyc' -delete

# Build source distribution and wheel
python -m build

# Check build
twine check dist/*

# List contents
tar tzf dist/django-affiliate-system-*.tar.gz
unzip -l dist/django_affiliate_system-*.whl
```

### Test Locally

```bash
# Install locally
pip install dist/django-affiliate-system-*.tar.gz

# Or from wheel
pip install dist/django_affiliate_system-*.whl

# Test import
python -c "import django_affiliate_system; print(django_affiliate_system.__version__)"
```

### Publish to TestPyPI

```bash
# Upload to TestPyPI
twine upload --repository testpypi dist/*

# Test installation from TestPyPI
pip install --index-url https://test.pypi.org/simple/ \
  --extra-index-url https://pypi.org/simple/ \
  django-affiliate-system

# Test in new environment
python -m venv test_env
source test_env/bin/activate
pip install --index-url https://test.pypi.org/simple/ \
  --extra-index-url https://pypi.org/simple/ \
  django-affiliate-system
python -c "import django_affiliate_system; print('Success!')"
deactivate
rm -rf test_env
```

### Publish to PyPI

```bash
# Final upload to PyPI
twine upload dist/*

# Verify on PyPI
pip install django-affiliate-system

# Test installation
python -c "import django_affiliate_system; print(django_affiliate_system.__version__)"
```

## Git Commands

### Initialize Repository

```bash
# Initialize git
git init

# Add files
git add .

# First commit
git commit -m "Initial commit - django-affiliate-system package"

# Create GitHub repository (using gh CLI)
gh repo create django-affiliate-system --public --source=. --remote=origin

# Or add remote manually
git remote add origin https://github.com/yourusername/django-affiliate-system.git

# Push to GitHub
git push -u origin main
```

### Tagging Releases

```bash
# Create version tag
git tag -a v0.1.0 -m "Release version 0.1.0"

# Push tag
git push origin v0.1.0

# List tags
git tag -l

# Delete tag (if needed)
git tag -d v0.1.0
git push origin :refs/tags/v0.1.0
```

## Testing with Django Project

### Create Test Project

```bash
# Create test directory
mkdir test_project
cd test_project

# Create Django project
django-admin startproject myproject .

# Install your package
pip install -e ../django-affiliate-system

# Or from PyPI
pip install django-affiliate-system
```

### Configure Test Project

```python
# myproject/settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party
    'rest_framework',
    'rest_framework_simplejwt',

    # Your package
    'django_affiliate_system',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django_affiliate_system.middleware.CORSMiddleware',  # Add this
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_affiliate_system.middleware.TenantMiddleware',  # Add this
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'django_affiliate_system.authentication.HybridAuthentication',
    ],
}

AFFILIATE_SYSTEM = {
    'DOMAIN_PROTOCOL': 'http',
    'DOMAIN': 'localhost:8000',
    'DEFAULT_COMMISSION_RATE': 10.0,
    'COOKIE_DURATION_DAYS': 30,
    'ALLOWED_CORS_ORIGINS': [
        'http://localhost:3000',
    ],
}

# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('affiliate/', include('django_affiliate_system.urls')),
]
```

### Run Test Project

```bash
# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver

# Test API
curl http://localhost:8000/affiliate/api/tenants/
```

## Common Tasks

### Update Version

```bash
# Edit version
vim django_affiliate_system/__version__.py
# Change: __version__ = "0.1.1"

# Update changelog
vim CHANGELOG.md

# Commit changes
git add django_affiliate_system/__version__.py CHANGELOG.md
git commit -m "Bump version to 0.1.1"

# Tag release
git tag -a v0.1.1 -m "Release version 0.1.1"
git push && git push --tags

# Build and publish
rm -rf build/ dist/ *.egg-info/
python -m build
twine upload dist/*
```

### Add New Feature

```bash
# Create feature branch
git checkout -b feature/new-feature

# Make changes
# ... edit files ...

# Run tests
pytest

# Format and lint
black . && isort . && flake8

# Commit
git add .
git commit -m "Add new feature"

# Push and create PR
git push origin feature/new-feature
gh pr create
```

### Fix Bug

```bash
# Create bugfix branch
git checkout -b fix/bug-description

# Make changes
# ... fix bug ...

# Add test
# ... add test in tests/ ...

# Verify fix
pytest tests/test_specific.py

# Commit
git add .
git commit -m "Fix: bug description"

# Push
git push origin fix/bug-description
```

## Useful Scripts

### Check Package Completeness

```bash
# check_package.sh
#!/bin/bash

echo "Checking package structure..."

# Check required files
for file in setup.py README.md LICENSE CHANGELOG.md requirements.txt; do
    if [ -f "$file" ]; then
        echo "✓ $file exists"
    else
        echo "✗ $file missing"
    fi
done

# Check package directory
if [ -d "django_affiliate_system" ]; then
    echo "✓ Package directory exists"

    # Check required Python files
    for file in __init__.py __version__.py apps.py models.py views.py; do
        if [ -f "django_affiliate_system/$file" ]; then
            echo "  ✓ $file exists"
        else
            echo "  ✗ $file missing"
        fi
    done
else
    echo "✗ Package directory missing"
fi

# Run checks
echo "
Running Python checks..."
python setup.py check

echo "
Building package..."
python -m build --dry-run

echo "
Package check complete!"
```

### Clean Everything

```bash
# clean.sh
#!/bin/bash

echo "Cleaning build artifacts..."
rm -rf build/ dist/ *.egg-info/

echo "Cleaning Python cache..."
find . -type d -name __pycache__ -exec rm -r {} + 2>/dev/null
find . -type f -name '*.pyc' -delete
find . -type f -name '*.pyo' -delete
find . -type f -name '*.bak' -delete

echo "Cleaning test artifacts..."
rm -rf .pytest_cache/ .tox/ htmlcov/ .coverage

echo "Cleaning IDE files..."
rm -rf .vscode/ .idea/ *.swp *.swo

echo "Clean complete!"
```

### Run All Quality Checks

```bash
# quality_check.sh
#!/bin/bash

echo "Running quality checks..."

echo "
1. Formatting with black..."
black --check django_affiliate_system/ tests/ || exit 1

echo "
2. Import sorting with isort..."
isort --check-only django_affiliate_system/ tests/ || exit 1

echo "
3. Linting with flake8..."
flake8 django_affiliate_system/ || exit 1

echo "
4. Type checking with mypy..."
mypy django_affiliate_system/ || exit 1

echo "
5. Running tests..."
pytest --cov=django_affiliate_system --cov-report=term-missing || exit 1

echo "
✓ All quality checks passed!"
```

Make scripts executable:

```bash
chmod +x check_package.sh clean.sh quality_check.sh
```

## Environment Setup

### Development Environment

```bash
# Create .env file
cat > .env << EOF
DJANGO_SETTINGS_MODULE=myproject.settings
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://user:pass@localhost/dbname
EOF

# Load environment
source .env
```

### Virtual Environment Management

```bash
# Using venv
python -m venv venv
source venv/bin/activate

# Using virtualenv
virtualenv venv
source venv/bin/activate

# Using conda
conda create -n django-affiliate python=3.11
conda activate django-affiliate

# Deactivate
deactivate  # or: conda deactivate
```

## Documentation

### Build Docs (if using Sphinx)

```bash
cd docs/
make html
open _build/html/index.html
```

### Update README

```bash
# Preview README
grip README.md
# Opens at http://localhost:6419
```

## Troubleshooting

### Clear pip cache

```bash
pip cache purge
```

### Reinstall package

```bash
pip uninstall django-affiliate-system
pip install --no-cache-dir django-affiliate-system
```

### Check installed version

```bash
pip show django-affiliate-system
python -c "import django_affiliate_system; print(django_affiliate_system.__version__)"
```

### Debug import issues

```bash
python -v -c "import django_affiliate_system"
```

## Additional Resources

- PyPI: https://pypi.org/project/django-affiliate-system/
- TestPyPI: https://test.pypi.org/project/django-affiliate-system/
- GitHub: https://github.com/yourusername/django-affiliate-system
- Documentation: https://django-affiliate-system.readthedocs.io/

## Support

Need help?

- Check the README.md
- Read the MIGRATION_GUIDE.md
- Review the PUBLISHING.md
- Open an issue on GitHub
