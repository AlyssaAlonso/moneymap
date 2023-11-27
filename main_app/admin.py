from django.contrib import admin
from .models import Income, Bills, Expenses, FinancialHealth
# Register your models here.
admin.site.register(Bills)
admin.site.register(Income)
admin.site.register(Expenses)
admin.site.register(FinancialHealth)