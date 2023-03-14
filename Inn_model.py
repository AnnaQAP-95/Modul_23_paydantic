from pydantic import BaseModel


class Inn_Model(BaseModel):

    query: int
    kpp: int | None = None