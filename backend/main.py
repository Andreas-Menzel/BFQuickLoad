import itertools
from typing import List

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

import crud
from database import create_db_and_tables
from models import Preset, PresetMetadata, SearchFilter, PresetsCatalog

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/ping", operation_id="get_ping")
def ping():
    # version = importlib.metadata.version("bfquickload_backend")
    version = "0.1"
    return {"app_name": "BFQuickLoad", "version": version}


@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")


@app.get("/presets/catalog", response_model=PresetsCatalog, operation_id="get_presets_catalog")
def read_catalog():
    presets = crud.get_all_presets()

    return PresetsCatalog(
        presets_metadata=[PresetMetadata(
            id = p.id,
            name = p.name,
            description = p.description,
            author=p.author,
            tags = p.tags
        ) for p in presets],
        authors=sorted(list(set([p.author for p in presets]))),
        tags=sorted(list(set(itertools.chain(*[p.tags for p in presets]))))
    )


@app.get("/presets", response_model=List[Preset], operation_id="get_all_presets")
def read_presets():
    return crud.get_all_presets()


@app.get("/presets/{preset_id}", response_model=Preset, operation_id="get_preset")
def read_preset(preset_id: int):
    db_preset = crud.get_preset(preset_id=preset_id)
    if db_preset is None:
        raise HTTPException(status_code=404, detail="Preset not found")
    return db_preset


@app.get("/search_filters", response_model=List[SearchFilter], operation_id="get_all_search_filters")
def read_search_filters():
    return crud.get_all_search_filters()


@app.get("search_filter/{filter_id}", response_model=SearchFilter, operation_id="get_search_filter")
def read_search_filter(filter_id: int):
    db_preset = crud.get_search_filter(filter_id=filter_id)
