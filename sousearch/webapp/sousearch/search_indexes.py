# -*- coding: utf-8 -*-
import datetime
from haystack import indexes
from sousearch.models import Betankande


class BetankandeIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    number = indexes.CharField(model_attr='number')
    updated_at = indexes.DateTimeField(model_attr='updated_at')

    def get_model(self):
        return Betankande

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(updated_at__lte=datetime.datetime.now())

