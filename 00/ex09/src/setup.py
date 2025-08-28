import setuptools as stp
import sys


def main():
    """A script allow to make the ft_package package."""

    try:
        with open("./README.md", "r") as rd:
            long_description = rd.read()

        stp.setup(
            name="ft_package",
            version="0.0.1",
            description="A sample test package",
            long_description=long_description,
            long_description_content_type="text/markdown",
            url="https://github.com/swangarch/ft_package",
            author="shuwang",
            author_email="shuwang@42.fr",
            license="MIT",
            packages=stp.find_packages(),
        )
    except Exception as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()
