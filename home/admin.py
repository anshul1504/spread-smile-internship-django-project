from django.contrib import admin
from home.models import Contact,Contribute,Joinus
# Register your models here.
models=[Contact,Contribute,Joinus]
admin.site.register(models)