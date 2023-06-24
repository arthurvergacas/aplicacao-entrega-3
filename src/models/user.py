from dataclasses import dataclass
from typing import Optional
import utils.console_utils as console_utils


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

    def __str__(self) -> str:
        result = ""
        result += console_utils.tab + f"E-mail: {self.email}" + "\n"
        result += console_utils.tab + f"CPF: {self.cpf}" + "\n"
        result += console_utils.tab + f"Nome: {self.name}" + "\n"
        result += console_utils.tab + f"Descrição: {self.description}" + "\n"
        result += console_utils.tab + f"Data de nascimento: {self.birth_date}" + "\n"
        result += console_utils.tab + f"Sexualidade: {self.sexuality}" + "\n"
        result += console_utils.tab + f"Genêro: {self.gender}" + "\n"
        result += (
            console_utils.tab
            + f"Grau de deficiência visual: {self.blindness_degree}"
            + "\n"
        )
        result += (
            console_utils.tab + f"Áudio de descrição (url): {self.audio_url}" + "\n"
        )
        result += console_utils.tab + f"Imagem (url): {self.img_url}"

        return result
