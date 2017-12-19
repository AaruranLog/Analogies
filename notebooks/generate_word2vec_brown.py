
# coding: utf-8

# In[3]:

import gensim.models.word2vec
from nltk.corpus import brown


# In[6]:

len(brown.words())


# In[9]:

brown.categories()


# In[10]:

brown.words(categories="humor")


# In[11]:

brown.sents(categories="humor")


# In[63]:

class my_sentences():
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
    


# In[68]:

model = gensim.models.word2vec.Word2Vec(sentences = my_sentences())


# In[87]:

import datetime
todays_date = datetime.date.today().strftime("%Y%m%d")
model_name = "brown-" + todays_date + ".model"


# In[71]:

model.save("/Users/fxf231/Documents/git-repos/Analogies/notebooks/brown")


# In[73]:

model.build_vocab(my_sentences())


# In[85]:

model.doesnt_match("man boy girl".split(" "))


# In[86]:

model.doesnt_match("balance account interest fish".split(" "))


# In[ ]:



