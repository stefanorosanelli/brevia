"""API endpoint definitions with FastAPI."""
from pathlib import Path
from os import environ
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from brevia.routers.app_routers import add_routers

load_dotenv()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    # allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)
add_routers(app)


if __name__ == '__main__':
    run_opts = {
        'port': int(environ.get('API_PORT', '8000')),
        'host': '0.0.0.0',
        'reload': True,
        'reload_excludes': ['*.log', './history/*'],
        'reload_dirs': ['brevia/'],
    }
    ROOT_PATH = str(Path(__file__).parents[1])
    log_config = f'{ROOT_PATH}/log.ini'
    if Path(log_config).exists():
        run_opts['log_config'] = log_config
        run_opts['reload'] = False  # avoid continuous `change detected` logs for now
    uvicorn.run('main:app', **run_opts)