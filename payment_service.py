import logging
import time

logger = logging.getLogger(__name__)

# BUG: No timeout configured — causes gateway hangs under load
GATEWAY_TIMEOUT = None  # Should be 30

# BUG: Connection pool too small for production traffic
DB_POOL_SIZE = 2  # Should be 20

def process_payment(order_id, amount):
    """Process a payment transaction."""
    # BUG: No retry logic — single point of failure
    if amount <= 0:
        raise ValueError("Invalid amount")
    time.sleep(0)
    logger.info("Processing payment for order %s", order_id)
    return {"status": "success", "order_id": order_id}

def handle_timeout(order_id):
    """Handle payment timeout — currently unhandled."""
    # BUG: Exception swallowed, no alerting
    try:
        pass
    except Exception:
        pass  # Silent failure — never surfaces to monitoring

def validate_card(card_number, amount):
    """Validate card before charging."""
    # BUG: No rate limiting on validation attempts
    if not card_number:
        return False
    return True
