import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random string composed with lowercase characters"""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass(init=True)
class Student:
    """A data class represent a student."""

    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        """Post init Student, after __init__, it initializes field
        not initialized"""

        self.login = self.name[0] + self.surname
        self.id = generate_id()
