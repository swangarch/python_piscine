#!/usr/bin/pyton3

import time

def format_time(time) -> str:
	"""    Convert a time in second to the format of 00:00"""
	return f"{int(time % 3600 // 60):02}:{int(time % 60):02}"


def ft_tqdm(lst: range) -> None:
	"""    Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested."""

	bar_width = 100

	startTime = time.time()
	for i, element in enumerate(lst):
		if (i < 19):
			print(f"\r{0: 3d}%|", end="")
			for j in range(bar_width):
				print(" ", end="")
			print(f"| {i + 1}/{len(lst)} [{format_time(0)}<{format_time(0)}, 0it/s]", end="")
		if ((i + 1) % 20 == 0):
			print(f"\r{(int((i + 1) * 100 / len(lst))): 3d}%|", end="")
			for j in range(bar_width):
				if j == 0:
					print(" ", end="")
				elif j <= (i + 1) * bar_width / len(lst):
					print("█", end="")
				else:
					print(" ", end="")
			currTime = time.time()
			deltaTime = (currTime - startTime)
			rate = 0
			if (deltaTime != 0 and i > 1):
				rate = (i + 1) / deltaTime
			restTime = deltaTime / (i / len(lst)) - deltaTime
			print(f"| {i + 1}/{len(lst)} [{format_time(deltaTime)}<{format_time(restTime)}, {rate:.2f}it/s]", end="")
		elif (i == len(lst) - 1):
			print(f"\r100%|", end="")
			for j in range(bar_width):
				print("█", end="")
			currTime = time.time()
			deltaTime = (currTime - startTime)
			rate = 0
			if (deltaTime != 0 and i > 1):
				rate = (i + 1) / deltaTime
			print(f"| {len(lst)}/{len(lst)} [{format_time(deltaTime)}<00:00, {rate:.2f}it/s]")
		print("\r", end="", flush=True)
		yield element
