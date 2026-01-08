# app/drop_table.py
from .database import engine, Base
from sqlalchemy import text

# Drop old table if it exists
with engine.connect() as conn:
    conn.execute(text("DROP TABLE IF EXISTS repo;"))
    conn.commit()

# Recreate tables according to models
Base.metadata.create_all(bind=engine)

print("Table recreated successfully")
