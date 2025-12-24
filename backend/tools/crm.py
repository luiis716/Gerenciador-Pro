from dataclasses import dataclass


@dataclass(frozen=True)
class LeadUpdateInput:
    lead_id: str
    payload: dict


class CRMTool:
    def update_lead(self, payload: LeadUpdateInput) -> None:
        return None
