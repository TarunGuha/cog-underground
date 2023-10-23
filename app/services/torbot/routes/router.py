from fastapi.responses import JSONResponse
from fastapi import APIRouter, status, Response, Depends, Query


router = APIRouter(prefix="/torbot", tags=["Telegram Bot"])


@router.get(
    "/webhook",
    # response_model=GetEmailWorkflowResponse,
    # status_code=status.HTTP_200_OK,
)
def catch_incoming_webhook_from_telegram():
    response = {"message": "working"}
    return response
