from datetime import timedelta

from backend.domain.silence_policy import SilencePolicy


class SilencePolicyProvider:
    def get(self) -> SilencePolicy:
        return SilencePolicy(
            when_to_not_reply=("negative",),
            max_silence_time=timedelta(hours=24),
            silence_is_final=True,
        )
