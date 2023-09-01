from django.contrib import admin
from Code_mantra_app.models import *
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
  list_display = ("first_name", "last_name", "email",)
  
admin.site.register(Contact_us, ContactAdmin)