import unittest

from exercises.practice import (
    build_profile,
    count_items,
    double_number,
    get_passing_scores,
    is_even,
)


class PracticeTests(unittest.TestCase):
    def test_double_number(self):
        self.assertEqual(double_number(4), 8)
        self.assertEqual(double_number(-3), -6)

    def test_is_even(self):
        self.assertTrue(is_even(10))
        self.assertFalse(is_even(7))

    def test_count_items(self):
        self.assertEqual(count_items(["a", "b", "c"]), 3)
        self.assertEqual(count_items([]), 0)

    def test_get_passing_scores(self):
        self.assertEqual(get_passing_scores([40, 50, 80]), [50, 80])
        self.assertEqual(get_passing_scores([60, 70, 75], pass_mark=70), [70, 75])

    def test_build_profile(self):
        profile = build_profile("Ari", 22, ["Python", "SQL"])

        self.assertEqual(profile["name"], "Ari")
        self.assertEqual(profile["age"], 22)
        self.assertEqual(profile["skills"], ["Python", "SQL"])
        self.assertEqual(profile["skill_count"], 2)


if __name__ == "__main__":
    unittest.main()

