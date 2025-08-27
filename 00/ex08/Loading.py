#!/usr/bin/pyton3

import time
import shutil


def format_time(time: int) -> str:
    """    Convert a time in second to the format of 00:00"""

    return f"{int(time % 3600 // 60):02}:{int(time % 60):02}"


def progress_bar(i: int, length: int, bar_width: int) -> str:
    """    Return the progress bar with current iteration and full length,
    and bar width as formatted string."""

    pg_bar = ""
    for j in range(bar_width):
        if j <= (i + 1) * bar_width / length:
            pg_bar += "█"
        else:
            pg_bar += " "
    return pg_bar


def progress_t(deltaTime: int, restTime: int) -> str:
    """    Return the time current progress takes and the estimated time to
    finish as a string."""

    return f'{format_time(deltaTime)}<{format_time(restTime)}'


def last_info(i: int, deltaT: int, length: int) -> str:
    """    Return the right part of the infomation, formatted as string."""

    if i != 0:
        rate = (i + 1) / deltaT
        restT = deltaT / (i / length) - deltaT
    else:
        rate = 0
        restT = 0
    return f"| {i + 1}/{length} [{progress_t(deltaT, restT)}, {rate:.2f}it/s]"


def print_percentage(i: int, length: int) -> None:
    """    Print the percentage of current progress."""

    if i == length - 1:
        print("\033[?25l100%|", end="")
    else:
        percentage = (int((i + 1) * 100 / length))
        print(f"\033[?25l{percentage: 3d}%|", end="")


def ft_tqdm(lst: range) -> None:
    """    Decorate an iterable object, returning an iterator which acts
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested."""

    try:
        length = len(lst)
        screen_width = shutil.get_terminal_size().columns
        step = 20
        startTime = time.time()
        for i, element in enumerate(lst):
            deltaTime = time.time() - startTime
            info = last_info(i, deltaTime, length)
            bar_width = screen_width - 5 - len(info)

            if (i + 1) % step == 0 or i == length - 1:
                print_percentage(i, length)
                print(progress_bar(i, length, bar_width), end="")
                if i == length - 1:
                    print(info, "\033[?25h", sep="")
                elif (i + 1) % step == 0:
                    print(info, end="\r", flush=True)
            yield element
    except Exception as e:
        print("Error:", e)
        return None
