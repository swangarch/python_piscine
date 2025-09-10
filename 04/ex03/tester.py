from new_student import Student


def main():
    """Test the data class Student"""

    student = Student(name="Edward", surname="agle")
    print(student)

    try:
        student2 = Student(name="Edward", surname="agle", id="toto")
        print(student2)
    except TypeError as e:
        print("TypeError:", e)
    except Exception as e:
        print("Error:", e)

    print()
    print("--------------My test---------------------")
    print()

    try:
        student2 = Student(name="Edward", surname="agle", login="test")
        print(student2)
    except TypeError as e:
        print("TypeError:", e)
    except Exception as e:
        print("Error:", e)

    print(student.__dict__)
    print(student.__repr__())
    print(student.__str__())


if __name__ == "__main__":
    main()
