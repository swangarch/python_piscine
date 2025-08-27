import setuptools

with open("./README.md", "r") as rd:
	long_description = rd.read()

setuptools.setup(
	name="ft_package",
	version="0.0.1",
	description="A sample test package",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/swangarch/ft_package",
	author="shuwang",
	author_email="shuwang@42.fr",
	license="MIT",
	packages=setuptools.find_packages(),
)