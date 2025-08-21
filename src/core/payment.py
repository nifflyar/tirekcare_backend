from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment
from paypalcheckoutsdk.orders import OrdersCreateRequest, OrdersCaptureRequest


from src.db.config import settings


client_id = settings.PAYPAL_CLIENT_ID
client_secret = settings.PAYPAL_SECRET_KEY
environment = SandboxEnvironment(client_id=client_id, client_secret=client_secret)
paypal_client = PayPalHttpClient(environment)





async def create_paypal_order(amount: str, currency: str = "USD"):
    request = OrdersCreateRequest()
    request.prefer("return=representation")
    request.request_body({
        "intent": "CAPTURE",
        "purchase_units": [
            {
                "amount": {
                    "currency_code": currency,
                    "value": amount
                }
            }
        ]
    })
    response = paypal_client.execute(request)
    return response.result



async def capture_paypal_order(order_id: str):
    request = OrdersCaptureRequest(order_id)
    request.request_body({})
    response = paypal_client.execute(request)
    return response.result