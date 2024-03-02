from django.urls import path

from quotes.views import GetQuoteID, GetRandomQuote

urlpatterns = [
    path("", GetRandomQuote.as_view(), name="random"),
    path("<int:pk>/", GetQuoteID.as_view(), name="quote"),
]