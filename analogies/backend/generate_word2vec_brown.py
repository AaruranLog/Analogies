#!/usr/bin/env python3
"""
    Generates a word2vec model trained on categories from nltk's Brown corpus
"""
import datetime
import gensim.models.word2vec
from nltk.corpus import brown


class CustomCorpus():
    """Implements iterator protocol to yield sentences from brown corpus"""

    category_selection = {0: ["humor"],
                          1: ["humor", "lore", "adventure",
                              "fiction", "learned", "news", "reviews"],
                          2: ["humor", "lore", "adventure",
                              "fiction", "learned", "news", "reviews",
                              "belles_lettres", "editorial", "government",
                              "hobbies", "learned", "mystery", "news",
                              "religion", "romance", "science_fiction"]}

    def __init__(self, corpora_choice=0):
        categories = self.category_selection[corpora_choice]
        self.permitted_categories = categories
        self.__usable_categories = self.permitted_categories
        self.corpus = brown
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.__usable_categories:
            try:
                category = self.__usable_categories[0]
                result = brown.sents(categories=category)[self.index]
                self.index += 1
                return result
            except IndexError:
                print(f"Emptied category: {category}")
                self.__usable_categories.remove(category)
                self.index = 0
                continue
        raise StopIteration

    def empty(self):
        """Checks if self has finished"""
        return not self.__usable_categories

    @property
    def categories(self):
        """Returns all categories from init"""
        return self.permitted_categories


def main():
    """
        Entry point
    """
    text = CustomCorpus()
    model = gensim.models.word2vec.Word2Vec(sentences=text)
    todays_date = datetime.date.today().strftime("%Y%m%d")
    model_name = "brown-" + todays_date + ".vec"
    model.wv.save_word2vec_format(model_name, binary=True)
    print("Model saved")
    print("=" * 20)
    print("Tests")
    print("=" * 20)
    print("expected: girl")
    print("Actual: ")
    print(model.doesnt_match("man boy girl brother father".split(" ")))

if __name__ == "__main__":
    main()
