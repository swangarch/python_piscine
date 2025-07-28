#!/usr/bin/python3

import time
from datetime import datetime

timestamp = time.time()

fmt = f"{timestamp:,.4f}"
scientific_fmt = f"{timestamp:.2e}"

date = datetime.now()

print("Seconds since January 1, 1970:", fmt, "or", scientific_fmt, "in scientific notation")
print(date.strftime("%B %d %Y"))