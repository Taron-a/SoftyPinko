from django.contrib import admin
from .models import (
    HeaderText, FeatureItem,  About, WorkProcess , WorkProcessItem,
    ContactUs , Row , Team_content , Pricing_Plans , Price , Counter , Blog , Blog_list
)

@admin.register(HeaderText)
class HeaderTextModelAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title', 'text']
    list_display_links = ['id' , 'title', 'text']

@admin.register(FeatureItem)
class FeatureItemModelAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title', 'text' , 'img_preview']
    list_display_links = ['id' , 'title', 'text' , 'img_preview']


@admin.register(About)
class AboutModelAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title', 'text' , 'img_preview']
    list_display_links = ['id' , 'title', 'text' , 'img_preview']


@admin.register(WorkProcessItem)
class WorkProcessItemModelAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title', 'text' , 'img_preview']
    list_display_links = ['id' , 'title', 'text' , 'img_preview']

@admin.register(ContactUs)
class ContactUsModelAdmin(admin.ModelAdmin):
    list_display = ['id' , 'name' , 'email' ,  'message']
    list_display_links = ['id' , 'name' , 'email' , 'message']
    search_fields = ['name' , 'email' , 'message']


admin.site.register(WorkProcess)

@admin.register(Row)
class RowModelAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title', 'text']
    list_display_links = ['id' , 'title', 'text']

@admin.register(Team_content)
class Team_contentModelAdmin(admin.ModelAdmin):
    list_display = ['id' , 'message' , 'user_name' , 'job']
    list_display_links = ['id' , 'message' , 'user_name' , 'job']

@admin.register(Pricing_Plans)
class Pricing_PlansModelAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title', 'text']
    list_display_links = ['id' , 'title', 'text']

@admin.register(Price)
class PriceModelAdmin(admin.ModelAdmin):
    list_display = ['id' , 'pricing_header' , 'currency' , 'price' , 'period']
    list_display_links = ['id' , 'pricing_header' , 'currency' , 'price' , 'period']

@admin.register(Counter)
class CounterModelAdmin(admin.ModelAdmin):
    list_display = ['id' , 'projects', 'happy_clients' , 'awards_wins' , 'countries']
    list_display_links = ['id' , 'projects', 'happy_clients' , 'awards_wins' , 'countries']

@admin.register(Blog)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title', 'text']
    list_display_links = ['id' , 'title', 'text']

@admin.register(Blog_list)
class Blog_listModelAdmin(admin.ModelAdmin):
    list_display = ['id' , 'title']
    list_display_links = ['id' , 'title']



