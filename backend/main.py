from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
import importlib.metadata

import crud
from database import create_db_and_tables
from models import Preset, PresetMetadata

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


@app.get("/presets/catalog", response_model=List[PresetMetadata], operation_id="get_presets_catalog")
def read_catalog():
    return crud.get_all_presets()


@app.get("/presets", response_model=List[Preset], operation_id="get_all_presets")
def read_presets():
    return crud.get_all_presets()


@app.get("/presets/{preset_id}", response_model=Preset, operation_id="get_preset")
def read_preset(preset_id: int):
    db_preset = crud.get_preset(preset_id=preset_id)
    if db_preset is None:
        raise HTTPException(status_code=404, detail="Preset not found")
    return db_preset
