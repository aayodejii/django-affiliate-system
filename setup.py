import os

from setuptools import find_packages, setup

# Read the contents of README file
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()


# Read requirements - DON'T use -r syntax
def read_requirements(filename):
    """Read requirements from file, excluding comments and -r references"""
    with open(filename) as f:
        return [
            line.strip()
            for line in f
            if line.strip() and not line.startswith("#") and not line.startswith("-r")
        ]


# Core requirements
install_requires = read_requirements("requirements.txt")

# Optional dependencies
extras_require = {
    "calendar": [
        "google-auth>=2.0.0",
        "google-api-python-client>=2.0.0",
    ],
    "celery": [
        "celery>=5.2.0",
        "redis>=4.5.0",
    ],
    "dev": [
        "pytest>=7.0.0",
        "pytest-django>=4.5.0",
        "pytest-cov>=4.0.0",
        "pytest-mock>=3.10.0",
        "black>=23.0.0",
        "flake8>=6.0.0",
        "isort>=5.12.0",
        "mypy>=1.0.0",
        "django-stubs>=4.0.0",
        "djangorestframework-stubs>=3.14.0",
        "tox>=4.0.0",
        "twine>=4.0.0",
        "wheel>=0.40.0",
        "build>=0.10.0",
        "coverage>=7.0.0",
        "factory-boy>=3.2.0",
        "faker>=18.0.0",
    ],
}

# Convenience extras
extras_require["all"] = extras_require["calendar"] + extras_require["celery"]

setup(
    name="django-affiliate-system",
    version="0.1.0",
    author="Ayodeji Akenroye",
    author_email="aayodeji.f@gmail.com",
    description="A comprehensive Django affiliate marketing and referral tracking system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aayodejii/django-affiliate-system",
    packages=find_packages(exclude=["tests", "tests.*", "docs"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
        "Framework :: Django :: 4.2",
        "Framework :: Django :: 5.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Office/Business :: Financial",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.9",
    install_requires=install_requires,
    extras_require=extras_require,
    include_package_data=True,
    zip_safe=False,
    keywords=[
        "django",
        "affiliate",
        "referral",
        "tracking",
        "commission",
        "marketing",
    ],
    project_urls={
        "Bug Reports": "https://github.com/aayodejii/django-affiliate-system/issues",
        "Source": "https://github.com/aayodejii/django-affiliate-system",
        "Documentation": "https://django-affiliate-system.readthedocs.io/",
    },
)
