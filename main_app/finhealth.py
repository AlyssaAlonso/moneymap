from .models import Bills, User, Income, Expenses, FinancialHealth
from django.shortcuts import render, redirect

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

  needs_percent = (yearly_bills + yearly_expenses) / yearly_income * 100
  savings_percent = ((yearly_income - (yearly_bills + yearly_estimated_expenses)) / yearly_income) * 100
  nonessential_percent = (sum(expense.amount for expense in expenses) / yearly_income) * 100
  bill_spending_percent = (sum(bill.amount for bill in bills) / yearly_income) * 100

  
  return render(request, 'finhealth/index.html', {
    'finhealth': finhealth, 
    'bills': bills, 
    'monthly_bills': monthly_bills, 
    'yearly_bills': yearly_bills, 
    'income': income, 
    'yearly_income': yearly_income, 
    'monthly_income': monthly_income, 
    'rounded_monthly_income': rounded_monthly_income,
    'expenses': expenses, 
    'total_expenses': total_expenses, 
    'yearly_estimated_expenses': yearly_estimated_expenses,
    'needs_percent': needs_percent,
    'savings_percent': savings_percent,
    'nonessential_percent': nonessential_percent,
    'bill_spending_percent': bill_spending_percent,
    'financial_health_grade': financial_health_grade, 
    },
)
