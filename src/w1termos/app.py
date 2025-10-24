import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from w1termos.api import router as api_router
from contextlib import asynccontextmanager
import signal
from w1termos.core import check_pid
import psutil

def shutdown(pid, including_parent=True):
    try:
        parent = psutil.Process(pid)
    except psutil.NoSuchProcess:
        return
    children = parent.children(recursive=True)
    for child in children:
        logging.warning(f"killing child {child}")
        child.kill()
    psutil.wait_procs(children, timeout=5)
    if including_parent:
        logging.warning(f"killing parent {pid}")
        parent.kill()
        parent.wait(5)

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    raise RuntimeError


def create_app():

    origins = ['*']

    app = FastAPI(title="w1termos@cacko.net", lifespan=lifespan)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router, prefix="/api")
    return app


def handler_stop_signals(signum, frame):
    shutdown(check_pid())


signal.signal(signal.SIGINT, handler_stop_signals)
signal.signal(signal.SIGTERM, handler_stop_signals)
