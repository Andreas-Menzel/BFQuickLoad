from typing import Optional, List

from pydantic import BaseModel
from sqlalchemy import Column
from sqlmodel import Field, SQLModel, JSON


class Preset(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(default="")
    description: str = Field(default="")
    tags: List[str] = Field(default_factory=list, sa_column=Column(JSON))
    author: str = Field(default="unknown")
    content: str = Field(default="")


class PresetMetadata(SQLModel):
    id: int
    name: str
    description: str
    author: str
    tags: List[str]

class PresetsCatalog(BaseModel):
    presets_metadata: List[PresetMetadata]
    authors: List[str]
    tags: List[str]


class SearchFilter(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    search_query: str
    author: str
    tags: List[str] = Field(sa_column=Column(JSON))
