from dataclasses import dataclass


@dataclass(frozen=True)
class NotificationInput:
    contact_id: str
    message: str


class NotifierTool:
    def send(self, payload: NotificationInput) -> None:
        return None
