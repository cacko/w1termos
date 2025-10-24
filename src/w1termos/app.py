from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from w1termos.api import router as api_router

def create_app():

    origins = ['*']

    app = FastAPI(title="w1termos@cacko.net")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router, prefix="/api")
    return app

