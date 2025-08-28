# ft_package

A simple Python package that provides a utility function for counting occurrences of an element in a list.

---

## Installation

You can install the package after building it locally:

```bash
pip install dist/ft_package-0.0.1-py3-none-any.whl
or
pip install dist/ft_package-0.0.1.tar.gz
```
---

## Usage

from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto")) # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu")) # output: 0

## License

This project is licensed under the MIT License - see the LICENSE