#!/bin/bash

gunicorn app.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind="${API_HOST_PORT}"