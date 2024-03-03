# Create your views here.

from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views import generic

from quotes.models import Quote

from random import randrange


class GetQuoteID(generic.DetailView):
    model = Quote
    template_name = "quotes/quote.html"

class GetRandomQuote(generic.DetailView):
    model = Quote
    template_name = "quotes/quote.html"

    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        # Eventually return a random object

        x = randrange(Quote.objects.count())+1
        return Quote.objects.get(
            id = x
        )