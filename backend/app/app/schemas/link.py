from uuid import uuid4

from pydantic import BaseModel, Field


class LinkBase(BaseModel):
    title: str
    url: str


class Link(LinkBase):
    id: str = Field(default_factory=uuid4, alias="_id")


class LinkCreate(LinkBase):
    ...


class LinkRead(LinkBase):
    id: str = Field(alias="_id")


class LinkUpdate(BaseModel):
    title: str | None = None
    url: str | None = None