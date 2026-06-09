"""Practice tasks for Python beginners.

Run tests with:

    python -m unittest discover tests
"""


def double_number(number):
    """Return the number multiplied by 2."""
    return number * 2


def is_even(number):
    """Return True when number is even, otherwise False."""
    return number % 2 == 0


def count_items(items):
    """Return how many items are in a list."""
    return len(items)


def get_passing_scores(scores, pass_mark=50):
    """Return only scores greater than or equal to pass_mark."""
    passing_scores = []

    for score in scores:
        if score >= pass_mark:
            passing_scores.append(score)

    return passing_scores


def build_profile(name, age, skills):
    """Return a dictionary describing a person."""
    return {
        "name": name,
        "age": age,
        "skills": skills,
        "skill_count": len(skills),
    }

