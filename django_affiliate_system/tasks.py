# tasks.py

from django.utils import timezone

try:
    from celery import shared_task

    CELERY_AVAILABLE = True
except ImportError:
    CELERY_AVAILABLE = False

    # Fallback decorator if Celery isn't installed
    def shared_task(func):
        return func


from .models import Commission, Payout


@shared_task
def process_payout(payout_id):
    """
    Process a payout for an affiliate.

    This is a stub — integrate with your payment provider (Stripe, PayPal, etc.)
    before using in production. Update payout.reference with the external
    payment ID returned by the provider.
    """
    if not CELERY_AVAILABLE:
        raise ImportError("Celery is required for async tasks")

    payout = Payout.objects.get(id=payout_id)

    if payout.status != "pending":
        return

    payout.status = "processing"
    payout.save()

    try:
        # TODO: Replace with real payment provider integration
        # e.g. stripe.Transfer.create(...) or paypalrestsdk.Payout.create(...)
        raise NotImplementedError("Payment provider integration not configured")

    except NotImplementedError:
        raise

    except Exception as e:
        payout.status = "failed"
        payout.metadata["error"] = str(e)
        payout.save()
