import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from app.database.db import engine
from app.database.models import Base

Base.metadata.create_all(bind=engine)

print("Database tables created successfully.")