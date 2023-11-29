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

  if (
    needs_percent <= 50 
  ):
    needs_score = 100
  elif (
    50 < needs_percent <= 55
  ):
    needs_score = 95
  elif (
    55 < needs_percent <=60
  ):
    needs_score = 90
  elif(
    60 < needs_percent <= 65
  ):
    needs_score = 85
  elif(
    65 < needs_percent <= 70
  ):
    needs_score = 80
  elif(
    70 < needs_percent <= 75
  ):
    needs_score = 75
  elif(
    75 < needs_percent <= 80
  ):
    needs_score = 70
  elif(
    80 < needs_percent <= 85
  ):
    needs_score = 65
  elif(
    85 < needs_percent <= 90
  ):
    needs_score = 60
  elif(
    90 < needs_percent <= 95
  ):
    needs_score = 55
  elif(
    95 < needs_percent <= 100
  ):
    needs_score = 50

  if (
    nonessential_percent <= 15 
  ):
    nonessential_score = 100
  elif (
    15 <= nonessential_percent <= 17
  ):
    nonessential_score = 95
  elif (
    17 < nonessential_percent <= 19
  ):
    nonessential_score = 90
  elif(
    19 < nonessential_percent <= 21
  ):
    nonessential_score = 85
  elif(
    21 < nonessential_percent <= 23
  ):
    nonessential_score = 80
  elif(
    23 < nonessential_percent <= 25
  ):
    nonessential_score = 75
  elif(
    25 < nonessential_percent <= 27
  ):
    nonessential_score = 70
  elif(
    27 < nonessential_percent <= 29
  ):
    nonessential_score = 65
  elif(
    29 < nonessential_percent <= 30
  ):
    nonessential_score = 60
  elif(
    30 < nonessential_percent <= 32
  ):
    nonessential_score = 55
  elif(
    32 < nonessential_percent <= 35
  ):
    nonessential_score = 50

  if (
    essential_percent <= 30 
  ):
    essential_score = 100
  elif (
    30 < essential_percent <= 33
  ):
    essential_score = 95
  elif (
    33 < essential_percent <= 35
  ):
    essential_score = 90
  elif(
    35 < essential_percent <= 38
  ):
    essential_score = 85
  elif(
    38 < essential_percent <= 41
  ):
    essential_score = 80
  elif(
    41 < essential_percent <= 44
  ):
    essential_score = 75
  elif(
    44 < essential_percent <= 47
  ):
    essential_score = 70
  elif(
    47 < essential_percent <= 50
  ):
    essential_score = 65
  elif(
    50 < essential_percent <= 53
  ):
    essential_score = 60
  elif(
    53 < essential_percent <= 56
  ):
    essential_score = 55
  elif(
    56 < essential_percent <= 59
  ):
    essential_score = 50

  if (
    savings_percent >= 30 
  ):
    savings_score = 100
  elif (
    25 <= savings_percent < 30
  ):
    savings_score = 95
  elif (
    20 <= savings_percent < 25
  ):
    savings_score = 90
  elif(
    17 <= savings_percent < 20
  ):
    savings_score = 85
  elif(
    15 <= savings_percent < 17
  ):
    savings_score = 80
  elif(
    13 <= savings_percent < 15
  ):
    savings_score = 75
  elif(
    11 <= savings_percent < 13
  ):
    savings_score = 70
  elif(
    9 <= savings_percent < 11
  ):
    savings_score = 65
  elif(
    7 <= savings_percent < 9
  ):
    savings_score = 60
  elif(
    4 <= savings_percent < 7
  ):
    savings_score = 55
  elif(
    1 <= savings_percent < 4
  ):
    savings_score = 50

  financial_health_score = (needs_score + savings_score + nonessential_score + essential_score) / 4 

  if financial_health_score == 100:
    financial_health_grade = 'A+'
  elif 95 <= financial_health_score < 100:
    financial_health_grade = 'A'
  elif 90 <= financial_health_score < 95:
    financial_health_grade = 'A-'
  elif 85 <= financial_health_score < 90:
    financial_health_grade = 'B+'
  elif 80 <= financial_health_score < 85:
    financial_health_grade = 'B'
  elif 75 <= financial_health_score < 80:
    financial_health_grade = 'C+'
  elif 70 <= financial_health_score < 75:
    financial_health_grade = 'C'
  elif 65 <= financial_health_score < 70:
    financial_health_grade = 'D+'
  elif 60 <= financial_health_score < 65:
    financial_health_grade = 'D'
  elif 0 <= financial_health_score < 60:
    financial_health_grade = 'F'
  else:
    financial_health_grade = 'Not Specified!'

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

def get_recommendation(needs_score, nonessential_score, essential_score, savings_score):
    recommendations = []

    if needs_score == 100:
        recommendations.append("Congratulations! Your needs spending is well within budget.")
    elif needs_score > 75:
        recommendations.append("Consider optimizing your needs spending. Look for cost-effective alternatives or discounts.")
