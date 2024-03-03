# Create your views here.

from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views import generic

from quotes.models import Quote
from quotes.apps import QuotesConfig

import random

class GetQuoteID(generic.DetailView):
    model = Quote
    template_name = "quotes/quote.html"

class GetRandomQuote(generic.DetailView):
    model = Quote
    template_name = "quotes/quote.html"

    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        # return a random quote

        n = random.choice(
                Quote.objects.all().values('id')    
            )["id"]
        return Quote.objects.get(id=n)


        # x = randrange(Quote.objects.count())+1
        # return Quote.objects.get(
        #     id = x
        # )