from SensorFilters import SMAFilter
import random

random.seed(42)

sma = SMAFilter(window_size=3)
true_temp = 25.0

for _ in range(10):
    noisy = true_temp + random.uniform(-2, 2)
    print(f"Raw: {noisy:.2f} -> Filtered: {sma.update(noisy):.2f}")
