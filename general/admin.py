from django.contrib import admin
from .models import Category, Testimony, Enquiry, Website

# Register your models here.
admin.site.register(Testimony)
admin.site.register(Enquiry)
admin.site.register(Website)
admin.site.register(Category)