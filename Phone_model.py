from pydantic import BaseModel, ValidationError


class Phone_Model(BaseModel):
    source: int | None = None
    type: str | None = None
    phone: str | None = None
    country_code: int | None = None
    city_code: int | None = None
    number: int | None = None
    extension: str | None = None
    provider: str | None = None
    country: str | None = None
    region: str | None = None
    city: str | None = None
    timezone: str | None = None
    qc_conflict: int | None = None
    qc: int | None = None

