from abc import ABC, abstractmethod, abstractproperty
from enum import Enum
from typing import Type, TypeVar
from client.pages.pages import Pages
import utils.console_utils as console_utils


EnumGenericType = TypeVar("EnumGenericType", bound=Enum)


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

    def _handle_input(
        self, options_labels: list[str], options_enum: Type[EnumGenericType]
    ) -> EnumGenericType:
        options = [
            f"{option.value} - {options_labels[i]}"
            for i, option in enumerate(options_enum)
        ]

        self.__show_input_options(options)

        return self.__get_user_input(options_enum)

    def __show_input_options(self, options: list[str]) -> None:
        print()
        print(console_utils.center("Digite o número de uma das opções abaixo:"))

        print()

        print(console_utils.itemize(options))

        print()

    def __get_user_input(self, options_enum: Type[EnumGenericType]) -> EnumGenericType:
        first_invalid = True

        while True:
            try:
                return options_enum(int(input(console_utils.tab + "Opção desejada: ")))
            except ValueError:
                console_utils.clear_line()

                if not first_invalid:
                    console_utils.clear_line()

                first_invalid = False

                print(
                    console_utils.tab
                    + "Opção inválida. Digite o número de uma das opções disponíveis."
                )
