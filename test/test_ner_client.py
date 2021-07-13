import unittest
from ner_client import NamedEntityClient
from test_doubles import NERModelTestDouble

class TestNERClient(unittest.TestCase):

    def test_get_ents_returns_dictionary_given_empty_string(self):
        """
        This method is to test that the entity client returns a dictionary when an empty string is given as input.
        :return:
        """

        model = NERModelTestDouble('eng')
        ner = NamedEntityClient(model)
        ents = ner.get_ents("")
        self.assertIsInstance(ents, dict)

    def test_get_ents_returns_list_given_nonempty_string(self):

        model = NERModelTestDouble("eng")
        ner = NamedEntityClient(model)
        ents = ner.get_ents("Paris is the capital of France!")
        self.assertIsInstance(ents, dict)