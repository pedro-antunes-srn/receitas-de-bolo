from django.contrib import admin
from bolo.models import Bolo

admin.site.site_header = "administração de bolos"
admin.site.site_title = "administração de bolos"
admin.site.index_title = "administração de bolos"

class BoloAdmin(admin.ModelAdmin):
    list_display = ['criador', 'bolo', 'preco', ]
    list_filter = ['criador','bolo' ,'preco']
    search_fields = ['criador', 'bolo',]
    prepopulated_fields = {'slug': ['bolo']}
    fields = ('criador',('bolo', 'slug'),'ingredientes','calda','preparo','preparo_calda','preco','immagem', )
    
      

admin.site.register(Bolo, BoloAdmin)

