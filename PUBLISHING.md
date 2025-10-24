# Publishing to PyPI Guide

This guide will walk you through publishing `django-affiliate-system` to PyPI.

## Prerequisites

1. **Create PyPI Account**

   - Sign up at [https://pypi.org/account/register/](https://pypi.org/account/register/)
   - Sign up at [https://test.pypi.org/account/register/](https://test.pypi.org/account/register/) (for testing)

2. **Install Required Tools**

   ```bash
   pip install build twine
   ```

3. **Configure PyPI Credentials**

   Create or edit `~/.pypirc`:

   ```ini
   [distutils]
   index-servers =
       pypi
       testpypi

   [pypi]
   username = __token__
   password = pypi-YOUR-API-TOKEN-HERE

   [testpypi]
   username = __token__
   password = pypi-YOUR-TESTPYPI-API-TOKEN-HERE
   ```

   **Get API Tokens:**

   - PyPI: [https://pypi.org/manage/account/token/](https://pypi.org/manage/account/token/)
   - TestPyPI: [https://test.pypi.org/manage/account/token/](https://test.pypi.org/manage/account/token/)

## Pre-Publication Checklist

### 1. Clean Up Repository

```bash
# Remove old builds
rm -rf build/ dist/ *.egg-info/

# Remove Python cache
find . -type d -name __pycache__ -exec rm -r {} +
find . -type f -name '*.pyc' -delete
```

### 2. Update Version Number

Edit `django_affiliate_system/__version__.py`:

```python
__version__ = "0.1.0"  # Update this
```

### 3. Update CHANGELOG.md

Create a changelog entry:

```markdown
# Changelog

## [0.1.0] - 2025-01-XX

### Added

- Initial release
- Multi-tenant affiliate system
- Referral link management
- Commission tracking
- REST API endpoints
```

### 4. Verify Package Structure

```bash
# Check that all files are included
python setup.py check

# List files that will be included
python setup.py sdist --dry-run
```

### 5. Run Tests

```bash
# Run all tests
pytest

# With coverage
pytest --cov=django_affiliate_system --cov-report=html
```

### 6. Check Code Quality

```bash
# Format code
black django_affiliate_system/ tests/

# Check linting
flake8 django_affiliate_system/

# Type checking (optional)
mypy django_affiliate_system/
```

## Publishing Steps

### Step 1: Test Locally

```bash
# Install package locally in editable mode
pip install -e .

# Test imports
python -c "import django_affiliate_system; print(django_affiliate_system.__version__)"
```

### Step 2: Build the Package

```bash
# Clean previous builds
rm -rf build/ dist/ *.egg-info/

# Build source distribution and wheel
python -m build

# Verify build contents
tar tzf dist/django-affiliate-system-0.1.0.tar.gz
```

### Step 3: Test on TestPyPI (Recommended)

```bash
# Upload to TestPyPI
twine upload --repository testpypi dist/*

# Test installation from TestPyPI
pip install --index-url https://test.pypi.org/simple/ \
    --extra-index-url https://pypi.org/simple/ \
    django-affiliate-system
```

### Step 4: Upload to PyPI

```bash
# Upload to production PyPI
twine upload dist/*

# Enter your username and password when prompted
# Or use API token from ~/.pypirc
```

### Step 5: Verify Installation

```bash
# Create a new virtual environment
python -m venv test_env
source test_env/bin/activate  # On Windows: test_env\Scripts\activate

# Install from PyPI
pip install django-affiliate-system

# Test it works
python -c "import django_affiliate_system; print(django_affiliate_system.__version__)"
```

## Post-Publication

### 1. Create GitHub Release

```bash
# Tag the release
git tag -a v0.1.0 -m "Release version 0.1.0"
git push origin v0.1.0

# Create release on GitHub with release notes
```

### 2. Update Documentation

- Update ReadTheDocs if configured
- Update README badges
- Announce on social media, forums, etc.

### 3. Monitor

- Check PyPI download stats
- Monitor GitHub issues
- Respond to user feedback

## Updating the Package

When releasing updates:

1. **Update version number** in `__version__.py`
2. **Update CHANGELOG.md** with changes
3. **Run tests** to ensure everything works
4. **Build and upload**:
   ```bash
   rm -rf build/ dist/ *.egg-info/
   python -m build
   twine upload dist/*
   ```

## Version Numbering (Semantic Versioning)

Follow [Semantic Versioning](https://semver.org/):

- **MAJOR** version (1.0.0): Incompatible API changes
- **MINOR** version (0.1.0): Add functionality (backwards compatible)
- **PATCH** version (0.0.1): Bug fixes (backwards compatible)

Examples:

- `0.1.0` - Initial release
- `0.1.1` - Bug fix
- `0.2.0` - New feature added
- `1.0.0` - Stable release, production-ready

## Troubleshooting

### Issue: "File already exists"

If you get this error when uploading:

```bash
# Increment version number in __version__.py
# Then rebuild
python -m build
twine upload dist/*
```

### Issue: Package Not Found After Upload

Wait a few minutes for PyPI to index the package, then try:

```bash
pip install --no-cache-dir django-affiliate-system
```

### Issue: Import Errors

Make sure all dependencies are listed in `setup.py` and `requirements.txt`

### Issue: Missing Files in Distribution

Check `MANIFEST.in` and ensure all necessary files are included:

```bash
python setup.py sdist --dry-run
```

## Useful Commands

```bash
# Check package metadata
twine check dist/*

# View package info
pip show django-affiliate-system

# Uninstall package
pip uninstall django-affiliate-system

# Install specific version
pip install django-affiliate-system==0.1.0

# Install latest development version from GitHub
pip install git+https://github.com/yourusername/django-affiliate-system.git
```

## Resources

- [Python Packaging Guide](https://packaging.python.org/)
- [PyPI Help](https://pypi.org/help/)
- [Twine Documentation](https://twine.readthedocs.io/)
- [Semantic Versioning](https://semver.org/)
- [TestPyPI](https://test.pypi.org/)

## Security Notes

- **Never commit** API tokens or credentials
- Use API tokens instead of username/password
- Configure `.pypirc` file permissions: `chmod 600 ~/.pypirc`
- Consider using environment variables for CI/CD

## Automated Publishing with GitHub Actions

Create `.github/workflows/publish.yml`:

```yaml
name: Publish to PyPI

on:
  release:
    types: [published]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install build twine

      - name: Build package
        run: python -m build

      - name: Publish to PyPI
        env:
          TWINE_USERNAME: __token__
          TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
        run: twine upload dist/*
```

Add `PYPI_API_TOKEN` to your GitHub repository secrets.
