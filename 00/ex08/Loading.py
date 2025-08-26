#!/usr/bin/pyton3

import time
import shutil
import sys

def format_time(time) -> str:
	"""    Convert a time in second to the format of 00:00"""

	return f"{int(time % 3600 // 60):02}:{int(time % 60):02}"


def ft_tqdm(lst: range) -> None:
	"""    Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested."""

	length = len(lst)
	bar_width = shutil.get_terminal_size().columns - 50 + len(str(length)) * 2
	
	startTime = time.time()
	currTime = startTime
	for i, element in enumerate(lst):
		
		# sys.stdout.write("\r" + " " * bar_width + "\r")
		sys.stdout.flush()
		deltaTime = time.time() - startTime

		if i < 19:
			print(f"{0: 3d}%|", end="")
			for j in range(bar_width):
				print(" ", end="")
			print(f"| {i + 1}/{length} [{format_time(0)}<{format_time(0)}, 0it/s]\r", end="", flush=True)
		elif (i + 1) % 20 == 0:
			print(f"{(int((i + 1) * 100 / length)): 3d}%|", end="")
			for j in range(bar_width):
				if j == 0:
					print("█", end="")
				elif j <= (i + 1) * bar_width / length:
					print("█", end="")
				else:
					print(" ", end="")
			rate = 0
			if (deltaTime != 0 and i > 1):
				rate = (i + 1) / deltaTime
			restTime = deltaTime / (i / length) - deltaTime
			print(f"| {i + 1}/{length} [{format_time(deltaTime)}<{format_time(restTime)}, {rate:.2f}it/s]\r", end="", flush=True)
		elif i == length - 1:
			print(f"100%|", end="")
			for j in range(bar_width):
				print("█", end="")
			rate = 0
			if (deltaTime != 0 and i > 1):
				rate = (i + 1) / deltaTime
			print(f"| {length}/{length} [{format_time(deltaTime)}<00:00, {rate:.2f}it/s]\r", flush=True)
		yield element
