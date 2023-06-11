from contextlib import suppress
from .entities import Activity, Certificate, Event, Student
from typing import List
from abc import (
    ABC,
    abstractmethod,
)
import openpyxl
from string import ascii_uppercase

# ABC = abstract base classes

# Padrão strategy


class BaseExtractor(ABC):
    @abstractmethod
    def extract(self, file_path, identifier) -> List[Certificate]:
        pass


# ...


class NormalFileExtractor(BaseExtractor):
    def extract(self, file_path: str, identifier) -> List[Certificate]:
        wb = openpyxl.load_workbook(file_path)

        sheet = wb.worksheets[0]
        event = sheet["C1"].value
        if isinstance(event, str):
            event = event.strip().lstrip("Evento: ")
        rows = sheet.rows
        certs = []

        with suppress(StopIteration):
            row = next(rows)
            # skip lines between top of sheet and data header
            while row[0].value != "Ano":
                row = next(rows)

            # skip blank line between header and data
            next(rows)

            for row in rows:
                cleaned = clean_row(row)
                if identifier == cleaned["F"]:
                    certs.append(
                        Certificate(
                            student=Student(
                                name=cleaned["G"], registration=cleaned["F"]
                            ),
                            activity=Activity(
                                event=Event(name=event, year=cleaned["A"]),
                                hours_granted=cleaned["E"],
                                kind=cleaned["C"],
                                name=cleaned["D"],
                            ),
                        )
                    )

        return certs


def clean_row(row) -> dict[str, str]:
    cells = (str(cell.value).strip() for cell in row)
    return dict(zip(ascii_uppercase, cells))
