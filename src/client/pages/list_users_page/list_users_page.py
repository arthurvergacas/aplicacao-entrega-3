from client.pages.page import Page
from client.pages.pages import Pages
from core.services.user_service import UserService
from models.user import User
from client.pages.list_users_page.enums.list_users_page_options import (
    ListUsersPageOptions,
)

import utils.console_utils as console_utils


class ListUsersPage(Page):
    @property
    def title(self):
        return (super().title if type(super().title) is list else [super().title]) + [
            "",
            "BUSCAR USUÁRIOS",
        ]  # type: ignore

    def run_page(self) -> Pages:
        user_name_filter = self.__get_user_name_filter()

        try:
            users = UserService.search_users(
                user_name_filter if user_name_filter != "" else None
            )
        except Exception as e:
            console_utils.print_error_msg("Erro na busca de usuários.", e)
        else:
            self.__print_users(users)

        option = self._handle_input(
            ["Nova busca", "Voltar para a tela inicial"], ListUsersPageOptions
        )

        match option:
            case ListUsersPageOptions.SEARCH_AGAIN:
                return Pages.LIST_USERS
            case ListUsersPageOptions.RETURN_HOME:
                return Pages.HOME

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
        if len(users) == 0:
            print()
            print(console_utils.center("Nenhum usuário encontrado"))
            print()

            return

        print("-" * console_utils.console_width)

        for user in users:
            print(user)
            print("-" * console_utils.console_width)
