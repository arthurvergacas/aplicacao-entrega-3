import sys
from client.pages.home_page.enums.home_page_options import HomePageOptions
from client.pages.page import Page
from client.pages.pages import Pages
import utils.console_utils as console_utils


class HomePage(Page):
    @property
    def title(self):
        return (super().title if type(super().title) is list else [super().title]) + [
            "Aplicação desenvolvida para o trabalho final da disciplina SCC0240 - Bases de Dados",
            "",
            "Desenvolvido por:",
            f"{'Arthur Vergaças':<22} | 12542672",
            f"{'Guilherme Panza':<22} | 12543519",
            f"{'Henrique Bovo':<22} | 12542539",
            f"{'Maria Júlia De Grandi':<22} | 12542501",
            f"{'Théo Bruno Riffel':<22} | 12547812",
            "",
        ]  # type: ignore

    def run_page(self) -> Pages:
        self._show_input_options(["1 - Buscar usuários", "2 - Criar novo usuário"])

        option = self.__handle_input()

        match option:
            case HomePageOptions.SEARCH_USERS:
                return Pages.LIST_USERS
            case HomePageOptions.CREATE_USER:
                return Pages.CREATE_USER

    def __handle_input(self) -> HomePageOptions:
        first_invalid = True

        while True:
            try:
                return HomePageOptions(
                    int(input(console_utils.tab + "Opção desejada: "))
                )
            except ValueError:
                console_utils.clear_line()

                if not first_invalid:
                    console_utils.clear_line()

                first_invalid = False

                print(
                    console_utils.tab
                    + "Opção inválida. Digite o número de uma das opções disponíveis."
                )
