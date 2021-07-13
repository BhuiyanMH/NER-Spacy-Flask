import unittest

class TestNERClient(unittest.TestCase):

    def test_get_ents_returns_dictionary_given_empty_string(self):
        """
        This method is to test that the entity client returns a dictionary when an empty string is given as input.
        :return:
        """

        ner = NamedEntityClient()
        ents = ner.get_ents("")
        self.assertIsInstance(ents, dict)