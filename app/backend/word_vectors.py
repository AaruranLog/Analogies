"""
	Helper functions for pre-trained model usage
"""

import gensim.models.word2vec as w2v


class Model(object):
    """Class for loading a saved model"""

    def __init__(self, path):
        super(Model, self).__init__()
        self.path = path
        try:
            self.model = w2v.load(path)
        except FileNotFoundError:
            self.model = None
            raise ValueError("File not found at path: {path}")

    def lookup(self, word):
        """Lookup word in model and return embedded vector"""
        
        try:
            return self.model[word]
        except Exception:
            raise ValueError(f"Failed to find: {word} in model vocabulary")

    def analogy(self, word1, target1, word2):
        """Returns the solution to the given analogy"""
        # TODO: include doctests here later
        try:
            target2 = self.model.wv.most_similar_cosmul(
                positive=[word2, target1], negative=[word1])
            return target2
        except Exception:
            statement = f"{word1} is to {target1} as {word2} is to ?"
            raise ValueError("Failed to find solution to analogy: {statement}")
