from datetime import datetime

from pydantic import BaseModel


class Schema(BaseModel):
    input_start: datetime


class FilteredResponse(BaseModel):
    filtered_counts: int
    state_id: int | None = None
