from fastapi import APIRouter, HTTPException
from app.models import Group
from typing import List

router = APIRouter(prefix="/api/v1/group", tags=["groups"])

groups_db = []
next_id = 1

@router.post("/")
async def create_group(group_data: dict):
    global next_id
    
    if 'title' not in group_data:
        raise HTTPException(status_code=400, detail="Title is required")
    
    new_group = Group(
        id=next_id,
        title=group_data['title'],
        description=group_data.get('description', ''),
        contacts=group_data.get('contacts', [])
    )
    
    groups_db.append(new_group)
    next_id += 1
    return new_group.to_dict()

@router.get("/", response_model=List[dict])
async def get_groups():
    return [group.to_dict() for group in groups_db]

@router.get("/{group_id}")
async def get_group(group_id: int):
    group = next((g for g in groups_db if g.id == group_id), None)
    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    return group.to_dict()