from dataclasses import dataclass


@dataclass(frozen=True)
class SheetAppendInput:
    sheet_id: str
    values: list[str]


class GoogleSheetsTool:
    def append_row(self, payload: SheetAppendInput) -> None:
        return None
