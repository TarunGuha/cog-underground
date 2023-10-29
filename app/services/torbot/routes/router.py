from fastapi.responses import JSONResponse
from fastapi import APIRouter, status, Response, Depends, Query

from app.services.torbot.routes.models import TelegramWebhook
from app.services.torbot.interactions.catch_incoming_messages import (
    catch_incoming_messages,
)


router = APIRouter(prefix="/torbot", tags=["Telegram Bot"])


@router.post(
    "/webhook",
    # response_model=GetEmailWorkflowResponse,
    # status_code=status.HTTP_200_OK,
)
def catch_incoming_webhook_from_telegram(TelegramWebhook: TelegramWebhook):
    catch_incoming_messages(TelegramWebhook)
