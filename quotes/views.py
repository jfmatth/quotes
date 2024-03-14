# Create your views here.

from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views import generic

from quotes.models import Quote
from quotes.apps import QuotesConfig

import random

import logging 

logger = logging.getLogger(__name__)

class GetQuoteID(generic.DetailView):
    model = Quote
    template_name = "quotes/quote.html"

class GetRandomQuote(generic.DetailView):
    model = Quote
    template_name = "quotes/quote.html"

    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        # return a random quote

        logger.info(f'Getting random quote')

        n = random.choice(
                Quote.objects.all().values('id')    
            )["id"]
        
        logger.info(f'returning object {n} from DB')
        return Quote.objects.get(id=n)


        # x = randrange(Quote.objects.count())+1
        # return Quote.objects.get(
        #     id = x
        # )