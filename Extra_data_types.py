from datetime import datetime, timedelta , time
from uuid import UUID

from fastapi import FastAPI,Body
from pydantic import BaseModel, Field
from typing import Optional


app = FastAPI()


@app.put("/items/{item_id}")
async def update_items(
        item_id: UUID,
        start : Optional[datetime] = Body(None),
        end : Optional[datetime] = Body(None),
        repeat_at : Optional[time] = Body(None),
        process_after : Optional[timedelta] = Body(None)
):
    start_process = start + process_after
    duration = end - start
    return {
        "item_id":item_id,
        "start":start,
        "end":end,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process":start_process,
        "duration": duration
    }

