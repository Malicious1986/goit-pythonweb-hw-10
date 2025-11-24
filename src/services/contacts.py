from sqlalchemy.ext.asyncio import AsyncSession

from src.database.models import Contact
from src.repository.contacts import ContactsRepository
from src.schemas import ContactModel


class ContactsService:
    def __init__(self, db: AsyncSession):
        self.contacts_repo = ContactsRepository(db)

    async def get_contacts(
        self,
        skip: int = 0,
        limit: int = 100,
        name: str | None = None,
        last_name: str | None = None,
        email: str | None = None,
    ) -> list[Contact]:
        return await self.contacts_repo.get_contacts(
            skip, limit, name, last_name, email
        )

    async def get_contact_by_id(self, contact_id: int) -> Contact | None:
        return await self.contacts_repo.get_contact_by_id(contact_id)

    async def create_contact(self, body: ContactModel) -> Contact:
        return await self.contacts_repo.create_contact(body)

    async def update_contact(
        self, contact_id: int, body: ContactModel
    ) -> Contact | None:
        return await self.contacts_repo.update_contact(contact_id, body)

    async def remove_contact(self, contact_id: int) -> Contact | None:
        return await self.contacts_repo.remove_contact(contact_id)

    async def get_upcoming_birthdays(self, days: int = 7) -> list[Contact]:
        return await self.contacts_repo.get_upcoming_birthdays(days)
