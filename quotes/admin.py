from django.contrib import admin

# Register your models here.
# from loader.models import Exchange, ExchangePrice, PriceError, ExchangeSplit

# class ExchangeAdmin(admin.ModelAdmin):
#     pass
# admin.site.register(Exchange, ExchangeAdmin)

from quotes.models import Quote

class QuoteAdmin(admin.ModelAdmin):
    list_display = ['quote', 'tag_list']

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())
    
admin.site.register(Quote, QuoteAdmin)