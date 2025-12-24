from dataclasses import dataclass


@dataclass(frozen=True)
class Contact:
    id: str
    name: str
    phone: str
