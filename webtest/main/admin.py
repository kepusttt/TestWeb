from django.contrib import admin
from .models import Image, TextIndex, SubImage, CustomUser, productCards, appealFIZ, appealUR, ChillSI, AnimalsSI, PlantsSI, TradeSI
from .models import AnimalsText, AnimalsCard,PlantsText,ChillText,TradeText, News, ImageN, PlantsCard, ProductOrderUr, ProductOrderFiz
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff'),
        }),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

    filter_horizontal = ()






admin.site.register(Image)
admin.site.register(PlantsText)
admin.site.register(TradeText)
admin.site.register(ChillText)
admin.site.register(AnimalsText)
admin.site.register(News)
admin.site.register(PlantsCard)
admin.site.register(AnimalsCard)
admin.site.register(ImageN)
admin.site.register(PlantsSI)
admin.site.register(TradeSI)
admin.site.register(AnimalsSI)
admin.site.register(ChillSI)
admin.site.register(TextIndex)
admin.site.register(SubImage)
admin.site.register(appealFIZ)
admin.site.register(appealUR)
admin.site.register(ProductOrderUr)
admin.site.register(ProductOrderFiz)
admin.site.register(productCards)
admin.site.register(CustomUser, CustomUserAdmin)


# Register your models here.
