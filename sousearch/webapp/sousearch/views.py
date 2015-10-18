from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from sousearch.models import *
from haystack.query import SearchQuerySet
from haystack.inputs import AutoQuery, Exact, Clean


def index(request):
    return render_to_response('index.html', locals())


def show(request, number):
    sou = get_object_or_404(Betankande, number=number)
    return render_to_response('show.html', locals())


def about(request):
    return render_to_response('about.html', locals())
