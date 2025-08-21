from fastapi import APIRouter


from src.core.payment import capture_paypal_order, create_paypal_order


router = APIRouter(prefix="/payment/paypal", tags=["Payment"])

@router.post("/create-order")
async def create_order(amount: str):
    order = await create_paypal_order(amount)
    approve_url = next(link.href for link in order.links if link.rel == "approve")
    return {"id": order.id, "status": order.status, "approve_url": approve_url}


@router.post("/capture-order/{order_id}")
async def capture_order(order_id: str):
    capture = await capture_paypal_order(order_id)
    return {"status": capture.status}