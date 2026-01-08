from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app import models, schemas
from app.services.github_service import fetch_repo

router = APIRouter(prefix="/repos", tags=["repos"])

# POST: Create a repo
@router.post("/", response_model=schemas.RepoRead, status_code=status.HTTP_201_CREATED)
def create_repo(payload: schemas.RepoCreate, db: Session = Depends(get_db)):
    data = fetch_repo(payload.owner, payload.name)
    repo = models.Repo(**data)
    db.add(repo)
    db.commit()
    db.refresh(repo)  # ensures repo.id is populated
    return repo

# GET: Get a repo by ID
@router.get("/{repo_id}", response_model=schemas.RepoRead)
def get_repo(repo_id: int, db: Session = Depends(get_db)):
    repo = db.query(models.Repo).filter(models.Repo.id == repo_id).first()
    if not repo:
        raise HTTPException(status_code=404, detail="Repo not found")
    return repo

# PUT: Update a repo (stars)
@router.put("/{repo_id}", response_model=schemas.RepoRead)
def update_repo(repo_id: int, payload: schemas.RepoUpdate, db: Session = Depends(get_db)):
    repo = db.query(models.Repo).filter(models.Repo.id == repo_id).first()
    if not repo:
        raise HTTPException(status_code=404, detail="Repo not found")

    repo.stars = payload.stars
    db.commit()
    db.refresh(repo)
    return repo

# DELETE: Delete a repo
@router.delete("/{repo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_repo(repo_id: int, db: Session = Depends(get_db)):
    repo = db.query(models.Repo).filter(models.Repo.id == repo_id).first()
    if not repo:
        raise HTTPException(status_code=404, detail="Repo not found")

    db.delete(repo)
    db.commit()
