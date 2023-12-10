from datetime import datetime, timezone

import uvicorn
from fastapi import FastAPI
from loguru import logger
from starlette.middleware.cors import CORSMiddleware

from config import Config

from core.api import router as api_router

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Including routers

app.include_router(api_router)


@app.on_event('startup')
async def on_startup():
    logger.success('Application startup complete at {time}', time=datetime.now(tz=timezone.utc))


if __name__ == '__main__':
    uvicorn.run('main:app', host=str(Config.host), port=Config.port, reload=True)
