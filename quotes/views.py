# Create your views here.

from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views import generic

from quotes.models import Quote
from rest_framework import permissions, viewsets

from random import randrange

# from tutorial.quickstart.serializers import GroupSerializer, UserSerializer
from quotes.serializers import QuoteSerializer


class QuoteViewSet(viewsets.ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = [permissions.AllowAny]

class GetQuoteID(generic.DetailView):
    model = Quote
    template_name = "quotes/quote.html"

class GetRandomQuote(generic.DetailView):
    model = Quote
    template_name = "quotes/quote.html"

    def get_object(self, queryset: QuerySet[Any] | None = ...) -> Model:
        # Eventually return a random object

        x = randrange(Quote.objects.count())
        return Quote.objects.get(
            id = x
        )


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated]


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.