from abc import ABC, abstractmethod, abstractproperty
from client.pages.pages import Pages
import utils.console_utils as console_utils


class Page(ABC):
    @abstractproperty
    def title(self) -> list[str] | str:
        return [
            "",
            "GERENCIAMENTO DE DADOS - IRIS",
            "",
        ]

    def run(self) -> Pages:
        console_utils.clear_terminal()

        self.__show_title()

        return self.run_page()

    def __show_title(self) -> None:
        print(console_utils.box(self.title))

    @abstractmethod
    def run_page(self) -> Pages:
        pass
