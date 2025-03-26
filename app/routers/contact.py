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