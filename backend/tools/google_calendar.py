from dataclasses import dataclass


@dataclass(frozen=True)
class CalendarEventInput:
    contact_id: str
    datetime: str
    title: str


@dataclass(frozen=True)
class CalendarEventOutput:
    event_id: str
    confirmed: bool


class GoogleCalendarTool:
    def create_event(self, payload: CalendarEventInput) -> CalendarEventOutput:
        return CalendarEventOutput(event_id="event-id", confirmed=True)
