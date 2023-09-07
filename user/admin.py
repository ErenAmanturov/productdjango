from django.contrib import admin
from .models import (User,
                     Phone,
                     WalletFill,
                     WalletReduction)

admin.site.register(User)
admin.site.register(Phone)
admin.site.register(WalletReduction)
admin.site.register(WalletFill)
