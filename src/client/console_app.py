from client.pages.create_user_page.create_user_page import CreateUserPage
from client.pages.home_page.home_page import HomePage
from client.pages.list_users_page.list_users_page import ListUsersPage
from client.pages.page import Page
from client.pages.pages import Pages
from core.infra.connection import DBConnection
import utils.console_utils as console_utils


class ConsoleApp:
    def __init__(self) -> None:
        console_utils.clear_terminal()

        self.page_dict = self.__create_page_dict()

        self.current_page: Page = self.page_dict[Pages.HOME]

    def run(self) -> None:
        running = True
        try:
            if not self.__initialize_db_connection():
                self.__exit()

            while running:
                next_page = self.current_page.run()
                self.current_page = self.page_dict[next_page]

        except KeyboardInterrupt:
            running = False
            self.__exit()

    def __initialize_db_connection(self) -> bool:
        print()
        print(console_utils.center("Conectando ao banco..."))
        print()

        try:
            DBConnection.create()
            return True
        except Exception as e:
            print(console_utils.center("Não foi possível se conectar ao banco."))
            print()
            print(console_utils.tab + "Mensagem de erro:")

            error_msg_lines = str(e).split("\n")

            for error_msg_line in error_msg_lines:
                print(console_utils.tab * 2 + error_msg_line)

            print()

            return False

    def __exit(self) -> None:
        print("\n")
        print(console_utils.center("Encerrando aplicação..."))
        print()
        exit()

    def __create_page_dict(self) -> dict[Pages, Page]:
        return {
            Pages.HOME: HomePage(),
            Pages.LIST_USERS: ListUsersPage(),
            Pages.CREATE_USER: CreateUserPage(),
        }
