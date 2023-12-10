import importlib
from pathlib import Path
from database import Base


def get_db_files():
    p = Path('core/models')
    return [str(file) for file in p.rglob('**/db.py')]


__all__ = [importlib.import_module(filename.replace('.py', '').replace('/', '.')) for filename in get_db_files()]
