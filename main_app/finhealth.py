from .models import Bill, User, Income, Expenses, FinancialHealth
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

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

  needs_percent = (yearly_bills + yearly_estimated_expenses) / yearly_income * 100
  savings_percent = ((yearly_income - (yearly_bills + yearly_estimated_expenses)) / yearly_income) * 100
  nonessential_percent = (sum(expense.amount for expense in expenses) / yearly_income) * 100
  bill_spending_percent = (sum(bill.amount for bill in bills) / yearly_income) * 100

  if (
    needs_percent <= 50
    and savings_percent >= 20
    and nonessential_percent <= 15
    and bill_spending_percent <= 30
  ):
    financial_health_grade = 'A+'
  elif (
    50 < needs_percent <= 55
    and 17 <= savings_percent < 20
    and 15 <= nonessential_percent <= 18
    and 30 < bill_spending_percent <= 35
  ):
    financial_health_grade = 'A'
  elif (
    55 < needs_percent <=60
    and 15 <= savings_percent < 17
    and 18 < nonessential_percent <= 20
    and 35 < bill_spending_percent <= 40
  ):
    financial_health_grade = 'B+'
  elif(
    60 < needs_percent <= 65
    and 13 <= savings_percent < 15
    and 21 < nonessential_percent <= 18
    and 40 < bill_spending_percent <= 45
  ):
    financial_health_grade = 'B'
    
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
