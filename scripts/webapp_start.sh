#!/usr/bin/env bash

# Activate the Pipenv environment and run FastAPI with Uvicorn
pipenv run uvicorn src.web_app:app --host 0.0.0.0 --port 8000 --reload
