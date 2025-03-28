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

@router.put("/{group_id}")
async def update_group(group_id: int, group_data: dict):
    global groups_db
    
    if 'title' not in group_data:
        raise HTTPException(status_code=400, detail="Title is required")
    
    group_index = next((i for i, g in enumerate(groups_db) if g.id == group_id), None)
    if group_index is None:
        raise HTTPException(status_code=404, detail="Group not found")
    
    updated_group = Group(
        id=group_id,
        title=group_data['title'],
        description=group_data.get('description', groups_db[group_index].description),
        contacts=group_data.get('contacts', groups_db[group_index].contacts)
    )
    
    groups_db[group_index] = updated_group
    return updated_group.to_dict()

@router.delete("/{group_id}")
async def delete_group(group_id: int):
    global groups_db
    
    group_index = next((i for i, g in enumerate(groups_db) if g.id == group_id), None)
    if group_index is None:
        raise HTTPException(status_code=404, detail="Group not found")
    
    deleted_group = groups_db.pop(group_index)
    return {"message": "Group deleted successfully", "deleted_group": deleted_group.to_dict()}



# if __name__ == '__main__':
    
    #create_group 
#    new_group = create_group(
#       "title": "Developers",
#       "description": "Backend-team",
#       "contacts": [1, 2, 3]
# )
 #  if new_group:
    #     group_id = new_group["id"]
        # # Update_group
        # update_group(group_id, title="brother", description="My brother")
        # # Get all list groups
        # get_groups()

        # # Delete group 
        # delete_group(group_id)
        # get_groups()