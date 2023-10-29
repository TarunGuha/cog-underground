from uuid import UUID
from datetime import datetime 
from pydantic import BaseModel
from typing import List, Optional, Dict, Any

class TelegramWebhook(BaseModel):
    update_id:  int
    message: dict | None = None
    callback_query: dict | None = None