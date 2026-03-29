from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    AffiliateViewSet,
    CommissionRuleViewSet,
    CommissionViewSet,
    PayoutViewSet,
    ReferralActionViewSet,
    ReferralLinkRedirectView,
    ReferralLinkViewSet,
    TenantViewSet,
)

# Create router for viewsets
router = DefaultRouter()
router.register(r"affiliates", AffiliateViewSet, basename="affiliates")
router.register(r"referral-links", ReferralLinkViewSet, basename="referral-links")
router.register(r"referral-actions", ReferralActionViewSet, basename="referral-actions")
router.register(r"commissions", CommissionViewSet, basename="commissions")
router.register(r"payouts", PayoutViewSet, basename="payouts")
router.register(r"commission-rules", CommissionRuleViewSet, basename="commission-rules")
router.register(r"tenants", TenantViewSet, basename="tenants")

urlpatterns = [
    path("", include(router.urls)),
    path("r/<slug:slug>/", ReferralLinkRedirectView.as_view(), name="referral-redirect"),
]

app_name = "django_affiliate_system"
