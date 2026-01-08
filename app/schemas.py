from pydantic import BaseModel, ConfigDict

# Request body when creating a repo
class RepoCreate(BaseModel):
    owner: str
    name: str

# Request body when updating a repo
class RepoUpdate(BaseModel):
    stars: int

# Response model for returning repo info
class RepoRead(BaseModel):
    id: int
    owner: str
    name: str
    stars: int
    url: str

    # This allows converting SQLAlchemy ORM objects to Pydantic models
    model_config = ConfigDict(from_attributes=True)
