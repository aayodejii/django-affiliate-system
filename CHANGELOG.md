# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Planned

- Admin dashboard UI
- More attribution models (linear, time-decay)
- Fraud detection system
- Advanced reporting and analytics
- Multi-currency support
- Webhook retry mechanism
- API rate limiting

## [0.1.0] - 2025-01-XX

### Added

- Initial release of django-affiliate-system
- Multi-tenant affiliate system support
- Referral link management and tracking
- Click, signup, and conversion tracking
- Commission calculation engine
- Flexible commission rules
- Payout management
- Session-based tracking with attribution models
- REST API with Django REST Framework
- JWT and API key authentication
- Hybrid authentication system
- Multi-touch attribution (first-click, last-click)
- Google Calendar integration (optional)
- Celery task support (optional)
- Comprehensive admin interface
- CORS middleware
- Tenant isolation middleware
- Webhook support for external conversions
- Detailed affiliate statistics endpoint
- CSV export functionality in admin

### Features

- **Multi-Tenant Architecture**: Support multiple affiliate programs from single instance
- **Flexible Authentication**: JWT for users, API keys for tenants, or hybrid mode
- **Advanced Tracking**: Session-based tracking with multiple attribution models
- **Commission Engine**: Percentage or fixed-amount commissions with min/max limits
- **RESTful API**: Complete CRUD operations for all resources
- **Admin Interface**: Auto-generated admin with CSV export
- **Webhook Integration**: Track conversions from external systems
- **Analytics**: Comprehensive statistics for affiliates and tenants

### Technical Details

- Python 3.9+ support
- Django 4.0+ support
- Django REST Framework integration
- PostgreSQL/MySQL/SQLite compatible
- Optional Celery for async tasks
- Optional Google Calendar integration

### Documentation

- Comprehensive README with quick start guide
- API usage examples
- Installation instructions
- Configuration guide
- Contributing guidelines

## Version History

### Versioning Strategy

We follow Semantic Versioning:

- **MAJOR** version: Incompatible API changes
- **MINOR** version: New features (backwards compatible)
- **PATCH** version: Bug fixes (backwards compatible)

### Support Policy

- Latest major version: Full support
- Previous major version: Security fixes only
- Older versions: No support

## Links

- [PyPI Package](https://pypi.org/project/django-affiliate-system/)
- [GitHub Repository](https://github.com/aayodejii/django-affiliate-system)
- [Documentation](https://django-affiliate-system.readthedocs.io/)
- [Issue Tracker](https://github.com/aayodejii/django-affiliate-system/issues)
