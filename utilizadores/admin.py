from django.contrib import admin
from .models import Perfil
from django.utils.html import format_html

class PerfilAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width:200px; max-height:200px"/>'.format(obj.imagem.url))

    list_display = ['utilizador', 'image_tag', 'discord_id','pontuacao']

admin.site.register(Perfil, PerfilAdmin)