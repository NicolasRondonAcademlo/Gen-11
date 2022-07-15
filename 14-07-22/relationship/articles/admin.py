from django.contrib import admin
from .models import Publication, Article
# Register your models here.

models = [Publication, Article]
register_model = [admin.site.register(model) for model in models]
