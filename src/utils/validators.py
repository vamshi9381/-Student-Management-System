def validate_age(age):

    if age < 1 or age > 100:
        raise ValueError("Age must be between 1 and 100")


def validate_marks(marks):

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100")