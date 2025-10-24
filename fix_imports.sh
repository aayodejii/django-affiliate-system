#!/bin/bash

# Update all imports in package
find django_affiliate_system -type f -name "*.py" -exec sed -i \
  -e 's/from affiliate_system\.core/from django_affiliate_system/g' \
  -e 's/import affiliate_system\.core/import django_affiliate_system/g' \
  -e 's/from affiliate_system\.users\.models import User/from django.contrib.auth import get_user_model\nUser = get_user_model()/g' \
  {} +

echo "✓ Imports updated!"
