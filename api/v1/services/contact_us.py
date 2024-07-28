from fastapi import Depends
from sqlalchemy.orm import Session
from typing import Annotated
from api.core.base.services import Service
from api.v1.routes.contact_us import get_db
from api.v1.schemas.contact_us import CreateContactUs
from api.v1.models import ContactUs  # noqa: F403


class ContactUsService(Service):
    """Contact Us Service."""

    def __init__(self) -> None:
        super().__init__()

    # ------------ CRUD functions ------------ #
    # CREATE
    def create(self, db: Annotated[Session, Depends(get_db)], data: CreateContactUs):
        """Create a new contact us message."""
        contact_message = ContactUs(
            full_name=data.full_name,
            email=data.email,
            title=data.title,
            message=data.message,
        )
        db.add(contact_message)
        db.commit()
        db.refresh(contact_message)
        print(contact_message)
        return contact_message

    # READ
    def fetch(self, db: Annotated[Session, Depends(get_db)], contact_id: int):
        """Read a single contact us message."""
        pass

    def fetch_all(self, db: Annotated[Session, Depends(get_db)]):
        """Read all contact us messages."""
        pass

    # UPDATE
    def update(self, db: Annotated[Session, Depends(get_db)], contact_id: int, data: CreateContactUs):
        """Update a single contact us message."""
        pass

    # DELETE
    def delete(self, db: Annotated[Session, Depends(get_db)], contact_id: int):
        """Delete a single contact us message."""
        pass

contact_service = ContactUsService()
