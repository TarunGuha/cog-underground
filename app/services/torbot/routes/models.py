from uuid import UUID
from datetime import datetime 
from pydantic import BaseModel
from typing import List, Optional

class Sample(BaseModel):
    input_param:  str | None = None