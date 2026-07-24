import lzma
import math
from collections import deque
from typing import Any

class AdaptiveCompressionEmergence:
    def __init__(self, base_window: int = 100):
        self.min_window = 10
        self.base_window = base_window
        self.window = base_window
        self.trace = deque(maxlen=base_window)
        self.bits_per_event = deque(maxlen=10)
        self.variance_history = deque(maxlen=10)
        self.emergence_score = 0.0

    def observe(self, event: Any) -> float:
        self.trace.append(str(event))
        raw = "|".join(self.trace)
        compressed = lzma.compress(raw.encode(), preset=0)
        bpe = len(compressed) * 8 / len(self.trace)
        self.bits_per_event.append(bpe)

        if len(self.bits_per_event) >= 10:
            bpe_arr = list(self.bits_per_event)
            mean = sum(bpe_arr) / len(bpe_arr)
            var = sum((x - mean) ** 2 for x in bpe_arr) / len(bpe_arr)
            self.variance_history.append(var)

            if var > 2.0 and self.window < 10000:
                self.window = min(self.window * 2, 10000)
                self._resize(self.window)
            elif var < 0.5 and self.window > self.min_window:
                self.window = max(self.window // 2, self.min_window)
                self._resize(self.window)

            baseline = self._shuffled_baseline()
            self.emergence_score = baseline - bpe if baseline > 0 else 0.0

        return self.emergence_score

    def _shuffled_baseline(self) -> float:
        if len(self.trace) < 10:
            return 0.0
        shuffled = list(self.trace)
        import random; random.shuffle(shuffled)
        raw = "|".join(shuffled)
        return len(lzma.compress(raw.encode(), preset=0)) * 8 / len(shuffled)

    def _resize(self, new_size: int):
        items = list(self.trace)
        self.trace = deque(maxlen=new_size)
        self.trace.extend(items[-new_size:])