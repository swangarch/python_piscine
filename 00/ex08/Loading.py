from datetime import datetime
import sys

def format_time(time):
	return f"{int(time % 3600 // 60):02}:{int(time % 60):02}"


def ft_tqdm(lst: range) -> None:
	"""    Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested."""

	startTime = datetime.now()
	for i in lst:
		if ((i + 1) % 20 == 0):
			print(f"\r{int((i + 1) * 100 / len(lst))}%|", end="")
			for j in range(100):
				if (j <= (i + 1) * 100 / len(lst)):
					print("██", end="")
				else:
					print("  ", end="")
			currTime = datetime.now()
			deltaTime = (currTime - startTime).seconds
			rate = 0
			if (deltaTime != 0 and i > 1):
				rate = (i + 1) / deltaTime
			restTime = deltaTime / (i / len(lst)) - deltaTime
			print(f"| {i + 1}/{len(lst)} [{format_time(deltaTime)}<{format_time(restTime)}, {rate:.2f}it/s]", end="")
		if (i == len(lst) - 1):
			print(f"\r100%|", end="")
			for j in range(100):
				print("██", end="")
			currTime = datetime.now()
			deltaTime = (currTime - startTime).seconds
			rate = 0
			if (deltaTime != 0 and i > 1):
				rate = (i + 1) / deltaTime
			print(f"| {len(lst)}/{len(lst)} [{format_time(deltaTime)}<00:00, {rate:.2f}it/s]")
		yield i
