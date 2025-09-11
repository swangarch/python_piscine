from statistics import ft_statistics


def main():
    """Main function to test ft_statistics"""

    ft_statistics(1, 42, 360, 11, 64, toto="mean",
                  tutu="median", tata="quartile")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                  hello="std", world="var")
    print("-----")
    ft_statistics(5, 75, 450, 18, 597, 27474, 48575,
                  ejfhhe="heheh", ejdjdejn="kdekem")
    print("-----")
    ft_statistics(toto="mean", tutu="median", tata="quartile")

    print("-------------my error handle test------------")
    #  string positional args
    ft_statistics(123, "string", toto="mean", tutu="median", tata="quartile")
    #  keyword args not string
    ft_statistics(1, toto=123123, tutu="median", tata="quartile")

    print("-------------my test------------")
    ft_statistics(12, 123, 4124, 1244, 8888, 1240, 123, 12131, toto="mean",
                  tutu="median", tata="quartile", hello="std", world="var")
    print("--------------Correct answer------------")
    print("mean : 3485.625")
    print("median : 1242.0")
    print("quartile : [123.0, 6506.0]")
    print("std : 4316.884957278223")
    print("var : 18635495.734375")


if __name__ == "__main__":
    main()
