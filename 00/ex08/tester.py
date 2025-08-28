#!/usr/bin/pyton3

from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm


def main():
    """A script to test the ft_tqdm function, in comparision with tqdm."""

    for elem in ft_tqdm(range(333)):
        sleep(0.005)
    print()

    for elem in tqdm(range(333)):
        sleep(0.005)
    print()


if __name__ == "__main__":
    main()
