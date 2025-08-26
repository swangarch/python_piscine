#!/usr/bin/python3

import time
from datetime import datetime

timestamp = time.time()

fmt = f"{timestamp:,.4f}"
scientific_fmt = f"{timestamp:.2e}"

date = datetime.now()

head = "Seconds since January 1, 1970:"
end = "in scientific notation"

print(head, fmt, "or", scientific_fmt, end)
print(date.strftime("%b %d %Y"))
