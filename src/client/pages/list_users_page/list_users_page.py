from client.pages.page import Page
from client.pages.pages import Pages
from src.models.user import User
import utils.console_utils as console_utils


class ListUsersPage(Page):
    @property
    def title(self):
        return (super().title if type(super().title) is list else [super().title]) + [
            "BUSCAR USUÁRIOS",
            "",
        ]  # type: ignore

    def run_page(self) -> Pages:
        user_name_filter = self.__get_user_name_filter()

        return Pages.LIST_USERS

    def __get_user_name_filter(self) -> str:
        print()
        print(
            console_utils.center(
                "Digite o nome ou parte do nome do usuário que deseja pesquisar."
            )
        )
        print(
            console_utils.center(
                "Deixe em branco para pesquisar por todos os usuários."
            )
        )

        print()

        return input(console_utils.tab + "Nome: ")

    def __print_users(self, users: list[User]) -> None:
        print("-" * console_utils.console_width)

        for user in users:
            print(user)
            print("-" * console_utils.console_width)
