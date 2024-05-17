from sqlmodel import SQLModel


class Status(SQLModel):
    name: str
    version: str
    database_server: str
    database_port: int
    database_name: str
