import unittest

from tools.slug import slugify


class SlugifyTest(unittest.TestCase):
    def test_replaces_spaces_with_dashes(self):
        self.assertEqual(slugify("Hello World"), "hello-world")


if __name__ == "__main__":
    unittest.main()
