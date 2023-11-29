from django.contrib import admin
from .models import Income, Bill, Expense, FinancialHealth
# Register your models here.
admin.site.register(Bill)
admin.site.register(Income)
admin.site.register(Expense)
admin.site.register(FinancialHealth)