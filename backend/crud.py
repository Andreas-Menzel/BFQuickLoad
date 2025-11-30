from typing import List

from sqlmodel import Session, select

from database import engine
from models import Preset, SearchFilter


def get_preset(preset_id: int) -> Preset | None:
    with Session(engine) as session:
        return session.get(Preset, preset_id)


def get_all_presets(limit: int = 128) -> List[Preset]:
    with Session(engine) as session:
        statement = select(Preset).limit(limit)
        return list(session.exec(statement).all())


def create_preset(preset: Preset) -> Preset:
    with Session(engine) as session:
        session.add(preset)
        session.commit()
        session.refresh(preset)
        return preset


def get_search_filter(filter_id: int) -> SearchFilter | None:
    with Session(engine) as session:
        return session.get(SearchFilter, filter_id)


def get_all_search_filters(limit: int = 128) -> List[SearchFilter]:
    with Session(engine) as session:
        statement = select(SearchFilter).limit(limit)
        return list(session.exec(statement).all())
