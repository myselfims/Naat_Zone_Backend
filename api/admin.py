from django.contrib import admin
from api.models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Benefit)
admin.site.register(Like)
admin.site.register(Naat)
admin.site.register(NaatKhwan)
admin.site.register(Subscription)