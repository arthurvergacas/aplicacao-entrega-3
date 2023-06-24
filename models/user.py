from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    email: Optional[str] = None
    cpf: Optional[str] = None
    name: Optional[str] = None
    birth_date: Optional[str] = None
    sexuality: Optional[str] = None
    gender: Optional[str] = None
    blindness_degree: Optional[str] = None
    description: Optional[str] = None
    audio_url: Optional[str] = None
    img_url: Optional[str] = None
