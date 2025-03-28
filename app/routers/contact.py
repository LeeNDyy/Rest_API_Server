from fastapi import APIRouter, HTTPException
from app.models import Contact, Phone
from typing import List
import json

router = APIRouter(prefix="/api/v1/contact", tags=["contacts"])

contacts_db = []
next_id = 1

@router.post("/")
async def create_contact(contact_data: dict):
    global next_id
    
    # Валидация данных
    required_fields = ['username', 'given_name', 'family_name']
    if not all(field in contact_data for field in required_fields):
        raise HTTPException(status_code=400, detail="Missing required fields")
    
    # Создание телефонов
    phones = [
        Phone(**phone_data) 
        for phone_data in contact_data.get('phone', [])
    ]
    
    new_contact = Contact(
        id=next_id,
        username=contact_data['username'],
        given_name=contact_data['given_name'],
        family_name=contact_data['family_name'],
        phone=phones,
        email=contact_data.get('email', []),
        birthdate=contact_data.get('birthdate')
    )
    
    contacts_db.append(new_contact)
    next_id += 1
    return new_contact.to_dict()

@router.get("/", response_model=List[dict])
async def get_contacts():
    return [contact.to_dict() for contact in contacts_db]

@router.get("/{contact_id}")
async def get_contact(contact_id: int):
    contact = next((c for c in contacts_db if c.id == contact_id), None)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact.to_dict()

@router.put("/{contact_id}")
async def update_contact(contact_id: int, contact_data: dict):
    global contacts_db
    
    # Валидация данных
    required_fields = ['username', 'given_name', 'family_name']
    if not all(field in contact_data for field in required_fields):
        raise HTTPException(status_code=400, detail="Missing required fields")
    
    # Поиск контакта
    contact_index = next((i for i, c in enumerate(contacts_db) if c.id == contact_id), None)
    if contact_index is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    
    # Создание телефонов
    phones = [
        Phone(**phone_data) 
        for phone_data in contact_data.get('phone', contacts_db[contact_index].phone)
    ]
    
    # Обновление контакта
    updated_contact = Contact(
        id=contact_id,
        username=contact_data['username'],
        given_name=contact_data['given_name'],
        family_name=contact_data['family_name'],
        phone=phones,
        email=contact_data.get('email', contacts_db[contact_index].email),
        birthdate=contact_data.get('birthdate', contacts_db[contact_index].birthdate)
    )
    
    contacts_db[contact_index] = updated_contact
    return updated_contact.to_dict()

@router.delete("/{contact_id}")
async def delete_contact(contact_id: int):
    global contacts_db
    
    contact_index = next((i for i, c in enumerate(contacts_db) if c.id == contact_id), None)
    if contact_index is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    
    deleted_contact = contacts_db.pop(contact_index)
    return {
        "message": "Contact deleted successfully",
        "deleted_contact": deleted_contact.to_dict()
    }


# def main():

    # Create new contact
    # new_contact = create_contact(
    #     username="Arsenij",
    #     given_name="Kullikov",
    #     family_name="Ildarovich",
    #     phone="89777777777",
    #     email="superdupermops@gmail.com",
    #     birthdate="15.06.2007"
    # )

    # if new_contact: 
        # contact_id = new_contact["id"]
        # Обновление контакта
        # update_contact(
        #     contact_id,
        #     phone="79999998888",
        #     email="opopop@gmail.com"
        # )
        # # get_all_contacs
        # get_contacts()
        
        # # Delete_contact
        # delete_contact(contact_id)
        # Get list contacts after delete contatc
        # get_contacts()

# if __name__ == "__main__":
#     main()