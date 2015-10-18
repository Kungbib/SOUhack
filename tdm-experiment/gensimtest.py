# -*- coding: utf-8 -*-
import sys
from os import listdir
from os.path import isfile, join
import os
import re
import gensim, logging


if __name__ == '__main__':

    filename = sys.argv[1] # t.ex. gensim2.model

    model = gensim.models.Word2Vec.load(filename)

    # experiment
    model.most_similar(positive=['skola', 'vuxen'], negative=['elev'])

    # enklast är att testa detta via python på kommandoraden
