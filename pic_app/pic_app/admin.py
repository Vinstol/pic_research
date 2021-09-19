from django.contrib import admin

from pic_app.models import Picture_colour


class Picture_colourAdmin(admin.ModelAdmin):
    list_display = ('pk', 'image', 'b_w_trigger', 'colour_hex',
                    'colour_cnt', 'pub_date')
    search_fields = ('b_w_trigger', 'colour_hex', 'pub_date')
    empty_value_display = '-пусто-'


admin.site.register(Picture_colour, Picture_colourAdmin)
