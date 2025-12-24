from dataclasses import dataclass
from datetime import timedelta


@dataclass(frozen=True)
class SilencePolicy:
    when_to_not_reply: tuple[str, ...]
    max_silence_time: timedelta
    silence_is_final: bool
