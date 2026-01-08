from sqlmodel import Session
from app.models import Repo
from app.schemas import RepoCreate
from datetime import datetime


def create_repo(db: Session, repo: RepoCreate, github_data: dict):
    db_repo = Repo(
        name=github_data["name"],
        full_name=github_data["full_name"],
        description=github_data["description"],
        stars=github_data["stars"],
        language=github_data["language"],
        url=github_data["url"],
        created_at=datetime.utcnow(),
    )
    db.add(db_repo)
    db.commit()
    db.refresh(db_repo)
    return db_repo
