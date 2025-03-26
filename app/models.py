from datetime import date
from typing import List

class Phone:
    def __init__(self, type_id: int, country_code: int, operator: int, number: int):
        self.type_id = type_id
        self.country_code = country_code
        self.operator = operator
        self.number = number

    def to_dict(self):
        return {
            'type_id': self.type_id,
            'country_code': self.country_code,
            'operator': self.operator,
            'number': self.number
        }

    
class Contact:
    def __init__(self, id: int, username: str, given_name: str, family_name: str, phone: List[Phone] = None, email: List[str] = None,
        birthdate: date = None):
        self.id = id
        self.username = username
        self.given_name = given_name
        self.family_name = family_name
        self.phone = phone if phone is not None else []
        self.email = email if email is not None else []
        self.birthdate = birthdate

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'given_name': self.given_name,
            'family_name': self.family_name,
            'phone': [p.to_dict() for p in self.phone],
            'email': self.email,
            'birthdate': str(self.birthdate) if self.birthdate else None
        }

class Group:
    def __init__(self, id: int, title: str, description: str, contacts: List[int] = None):
        self.id = id
        self.title = title
        self.description = description
        self.contacts = contacts if contacts is not None else []

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'contacts': self.contacts
        }