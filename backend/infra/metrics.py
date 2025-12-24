from collections import Counter


class Metrics:
    def __init__(self) -> None:
        self._counters = Counter()

    def increment(self, key: str) -> None:
        self._counters[key] += 1

    def snapshot(self) -> dict[str, int]:
        return dict(self._counters)
