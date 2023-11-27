from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about' ),
  path('finhealth/', views.finhealth_index, name='finhealth_index'),
  path('bills/', views.bills_index, name='bills_index'),    
  path('bills/create/', views.BillsCreate.as_view(), name='bills_create'),   
  path('bills/<int:pk>/update/', views.BillsUpdate.as_view(), name='bills_update'),
  path('bills/<int:pk>/delete/', views.BillsDelete.as_view(), name='bills_delete'),
  path('expenses/', views.expenses_index, name='expenses_index'),
  path('expenses/create/', views.ExpenseCreate.as_view(), name='expenses_create'),
  path('expenses/<int:pk>/update/', views.ExpensesUpdate.as_view(), name='expenses_update'),
  path('expenses/<int:pk>/delete/', views.ExpensesDelete.as_view(), name='expenses_delete'),
  path('income/', views.income_index, name='income_index'),
  path('income/create/', views.IncomeCreate.as_view(), name='income_create'),
  path('income/<int:pk>/update/', views.IncomeUpdate.as_view(), name='income_update'),
  path('income/<int:pk>/delete/', views.IncomeDelete.as_view(), name='income_delete'),
  path('accounts/signup/', views.signup, name='signup'),
]