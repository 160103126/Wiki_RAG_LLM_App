from sqlmodel import SQLModel, Field
from datetime import datetime

class QueryHistory(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    question: str
    answer: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    sources: str