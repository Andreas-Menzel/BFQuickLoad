from typing import Optional, List

from sqlalchemy import Column
from sqlmodel import Field, SQLModel, JSON


class Preset(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    tags: List[str] = Field(sa_column=Column(JSON))
    author: str
    content: str


class PresetMetadata(SQLModel):
    id: int
    name: str
    description: str
    tags: List[str]
    author: str