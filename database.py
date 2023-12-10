import json

import asyncpg
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, create_async_engine, async_sessionmaker
from config import Config
from loguru import logger


class Base(AsyncAttrs, DeclarativeBase):
    pass


engine = create_async_engine(str(Config.postgres_url), pool_size=20, max_overflow=0)

Session = async_sessionmaker(engine, expire_on_commit=False)

