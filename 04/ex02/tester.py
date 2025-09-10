from callLimit import callLimit


def main():
    """Main function to test callLimit"""

    @callLimit(3)
    def f():
        print("f()")

    @callLimit(1)
    def g():
        print("g()")

    for i in range(3):
        f()
        g()


if __name__ == "__main__":
    main()
