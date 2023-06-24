from client.pages.page import Page
from client.pages.pages import Pages
from models.user import User
import utils.console_utils as console_utils


class CreateUserPage(Page):
    @property
    def title(self):
        return (super().title if type(super().title) is list else [super().title]) + [
            "NOVO USUÁRIO",
            "",
        ]  # type: ignore

    def run_page(self) -> Pages:
        new_user = self.__read_new_user()

        return Pages.CREATE_USER

    def __read_new_user(self) -> User:
        print()
        print(console_utils.center("Preencha os campos abaixo para criar o usuário."))

        new_user = User()

        new_user.email = input(console_utils.tab + "E-mail: ")
        new_user.cpf = input(console_utils.tab + "CPF: ")
        new_user.name = input(console_utils.tab + "Nome: ")
        new_user.description = input(console_utils.tab + "Descrição: ")
        new_user.birth_date = input(console_utils.tab + "Data de nascimento: ")
        new_user.sexuality = input(console_utils.tab + "Sexualidade: ")
        new_user.gender = input(console_utils.tab + "Genêro: ")
        new_user.blindness_degree = input(
            console_utils.tab + "Grau de deficiência visual: "
        )
        new_user.audio_url = input(console_utils.tab + "Áudio de descrição (url): ")
        new_user.img_url = input(console_utils.tab + "Imagem (url): ")

        return new_user
