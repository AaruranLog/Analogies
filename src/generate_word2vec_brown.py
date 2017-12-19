import gensim.models.word2vec
from nltk.corpus import brown
import datetime

class my_sentences():
    """Implements iterator protocol to yield sentences from brown corpus"""
    def __init__(self):
        self.permitted_categories = ["humor", "lore", "adventure"]
        self.corpus = brown
        self.index = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        
        for c in self.permitted_categories:
            try:
                result = brown.sents(categories=c)[self.index]
                self.index += 1
                return result
            except IndexError:
                continue
        raise StopIteration

def main():
    """
        Entry point
    """
    model = gensim.models.word2vec.Word2Vec(sentences = my_sentences())
    todays_date = datetime.date.today().strftime("%Y%m%d")
    model_name = "brown-" + todays_date + ".model"
    model.save("/Users/fxf231/Documents/git-repos/Analogies/notebooks/" + model_name)

    print("=" * 20)
    print("Tests")
    print("=" * 20)
    print("expected: girl")
    print("Actual: ")
    print(model.doesnt_match("man boy girl".split(" ")))

    print("expected: fish")
    print("Actual: ")
    model.doesnt_match("balance account interest fish".split(" "))
