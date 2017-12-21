"""
Helper functions for pre-trained model usage
"""

import gensim.models.word2vec as w2v
from gensim.models.keyedvectors import KeyedVectors
import warnings


class Model(object):
    """Class for loading a saved model"""
    def __init__(self, path):
        super(Model, self).__init__()
        self.path = path
        try:
            self.model = KeyedVectors.load_word2vec_format(path, binary=True)
        except FileNotFoundError:
            self.model = None
            raise FileNotFoundError("Model not found at path: {path}")

    def lookup(self, word):
        """Lookup word in model and return embedded vector"""
        try:
            return self.model[word]
        except KeyError:
            warnings.warn(f"Failed to find: {word} in model vocabulary", UserWarning)
            return None

    def analogy(self, word1, target1, word2):
        """Returns the solution to the given analogy"""
        # TODO: include doctests here later
        try:
            target2 = self.model.most_similar_cosmul(positive=[word2, target1], negative=[word1])
            return target2
        except KeyError:
            statement = f"{word1} is to {target1} as {word2} is to ?"
            warnings.warn(f"Failed to find solution to analogy: {statement}", UserWarning)
            return None
