from .models import Bill, User, Income, Expense, FinancialHealth
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def finhealth_index(request):
  finhealth= FinancialHealth.objects.filter(user=request.user)
  bills= Bill.objects.filter(user=request.user)
  monthly_bills = sum(bill.amount for bill in bills)
  yearly_bills = monthly_bills * 12
  essential_bills = Bill.objects.filter(user = request.user, category='Essential')
  nonessential_bills = Bill.objects.filter(user = request.user, category = 'Nonessential')
  total_essential_bills = sum(bill.amount for bill in essential_bills)
  total_nonessential_bills = sum(bill.amount for bill in nonessential_bills)

  income= Income.objects.filter(user=request.user)
  yearly_income= sum(income.amount for income in income)
  monthly_income= yearly_income / 12
  rounded_monthly_income = round(monthly_income, 2)

  expenses= Expense.objects.filter(user=request.user)
  total_expenses = sum(expense.amount for expense in expenses)
  yearly_estimated_expenses = total_expenses * 12
  essential_expenses = Expense.objects.filter(user = request.user, category='Essential')
  nonessential_expenses = Expense.objects.filter(user = request.user, category = 'Nonessential')
  total_essential_expenses = sum(expense.amount for expense in essential_expenses)
  total_nonessential_expenses = sum(expense.amount for expense in nonessential_expenses)

  needs_percent = (yearly_bills + yearly_estimated_expenses) / yearly_income * 100
  savings_percent = ((yearly_income - (yearly_bills + yearly_estimated_expenses)) / yearly_income) * 100
  nonessential_percent = ((total_nonessential_bills + total_nonessential_expenses) / yearly_income) * 100
  essential_percent = ((total_essential_bills + total_essential_expenses) / yearly_income) * 100

  

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
    'financial_health_grade': financial_health_grade,
    'financial_health_score' : financial_health_score,
    'needs_score' : needs_score ,
    'savings_score' : savings_score,
    'nonessential_score' : nonessential_score,
    'essential_score' : essential_score,
    },
)
