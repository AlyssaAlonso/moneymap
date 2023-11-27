from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Bills, User, Income, Expenses, FinancialHealth
from .forms import UserForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def finhealth_index(request):
  finhealth= FinancialHealth.objects.filter(user=request.user)
  bills= Bills.objects.filter(user=request.user)
  monthly_bills = sum(bill.amount for bill in bills)
  yearly_bills = monthly_bills * 12
  income= Income.objects.filter(user=request.user)
  yearly_income= sum(income.yearly_salary + income.other_income for income in income)
  monthly_income= yearly_income / 12
  rounded_monthly_income = round(monthly_income, 2)
  expenses= Expenses.objects.filter(user=request.user)
  total_expenses = sum(expense.amount for expense in expenses)
  yearly_estimated_expenses = total_expenses * 12
  return render(request, 'finhealth/index.html', {'finhealth': finhealth, 'bills': bills, 'monthly_bills': monthly_bills, 'yearly_bills': yearly_bills, 'income': income, 'yearly_income': yearly_income, 'monthly_income': monthly_income, 'rounded_monthly_income': rounded_monthly_income,'expenses': expenses, 'total_expenses': total_expenses, 'yearly_estimated_expenses': yearly_estimated_expenses })

@login_required
def bills_index(request):
  bills= Bills.objects.filter(user=request.user)
  monthly_bills = sum(bill.amount for bill in bills)
  yearly_bills = monthly_bills * 12
  return render(request, 'bills/index.html', {'bills': bills, 'monthly_bills': monthly_bills, 'yearly_bills': yearly_bills})

@login_required
def income_index(request):
  income= Income.objects.filter(user=request.user)
  yearly_income= sum(income.yearly_salary + income.other_income for income in income)
  monthly_income= yearly_income / 12
  rounded_monthly_income = round(monthly_income, 2)
  return render(request, 'income/index.html', {'income': income, 'yearly_income': yearly_income, 'monthly_income': monthly_income, 'rounded_monthly_income': rounded_monthly_income})

@login_required
def expenses_index(request):
  expenses= Expenses.objects.filter(user=request.user)
  total_expenses = sum(expense.amount for expense in expenses)
  yearly_estimated_expenses = total_expenses * 12
  return render(request, 'expenses/index.html', {'expenses': expenses, 'total_expenses': total_expenses, 'yearly_estimated_expenses': yearly_estimated_expenses})

class IncomeCreate(LoginRequiredMixin, CreateView):
    model=Income
    fields = ['yearly_salary', 'other_income']
    success_url = '/expenses/create'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class IncomeUpdate(LoginRequiredMixin, UpdateView):
    model=Income
    fields= ['yearly_salary', 'other_income']
    success_url = '/income'

class IncomeDelete(LoginRequiredMixin, DeleteView):
    model=Income
    success_url = '/income'

class ExpenseCreate(LoginRequiredMixin, CreateView):
    model=Expenses
    fields = ['name', 'category', 'date', 'amount']
    success_url = '/expenses/create'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ExpensesUpdate(LoginRequiredMixin, UpdateView):
    model=Expenses
    fields= ['name', 'category', 'date', 'amount']
    success_url = '/expenses'

class ExpensesDelete(LoginRequiredMixin, DeleteView):
    model=Expenses
    success_url = '/expenses'

class BillsCreate(LoginRequiredMixin, CreateView):
    model=Bills
    fields = ['name', 'frequency', 'category', 'amount']
    success_url = '/bills/create'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class BillsUpdate(LoginRequiredMixin, UpdateView):
    model=Bills
    fields= ['name', 'frequency', 'category', 'amount']
    success_url = '/bills'

class BillsDelete(LoginRequiredMixin, DeleteView):
    model=Bills
    success_url = '/bills'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('/')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

