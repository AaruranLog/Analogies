"""
    Generates a word2vec model trained on categories from nltk's Brown corpus
"""
import datetime
import gensim.models.word2vec
from nltk.corpus import brown

class CustomCorpus():
    """Implements iterator protocol to yield sentences from brown corpus"""
    def __init__(self, categories=["humor", "lore", "adventure",
                                   "fiction", "learned", "news", "reviews"]):
        self.permitted_categories = categories
        self.__usable_categories = self.permitted_categories
        self.corpus = brown
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        for category in self.__usable_categories:
            try:
                result = brown.sents(categories=category)[self.index]
                self.index += 1
                return result
            except IndexError:
                self.__usable_categories.remove(category)
                continue
        raise StopIteration

def main():
    """
        Entry point
    """
    model = gensim.models.word2vec.Word2Vec(sentences=CustomCorpus())
    todays_date = datetime.date.today().strftime("%Y%m%d")
    model_name = "brown-" + todays_date + ".model"
    model.save("/Users/fxf231/Documents/git-repos/Analogies/notebooks/" + model_name)
    print("Model saved")

    print("=" * 20)
    print("Tests")
    print("=" * 20)
    print("expected: girl")
    print("Actual: ")
    print(model.doesnt_match("man boy girl".split(" ")))

    print("expected: fish")
    print("Actual: ")
    model.doesnt_match("balance account interest fish".split(" "))


if __name__ == "__main__":
    main()
