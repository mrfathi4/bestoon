from json import JSONEncoder

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import User, Expense, Income, Token
from datetime import datetime


# Create your views here.
@csrf_exempt
def submit_expense(request):
    #
    #
    print('we are here')

    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()

    Expense.objects.create(user=this_user, amount=request.POST['amount'], date=date, text=request.POST['text'])

    # print(request.POST)

    return JsonResponse({
        'status': 'OK',
    }, encoder=JSONEncoder)


@csrf_exempt
def submit_income(request):
    #
    #
    print('we are here')

    this_token = request.POST['token']
    this_user = User.objects.filter(token__token=this_token).get()
    if 'date' not in request.POST:
        date = datetime.now()

    Income.objects.create(user=this_user, amount=request.POST['amount'], date=date, text=request.POST['text'])

    # print(request.POST)

    return JsonResponse({
        'status': 'OK',
    }, encoder=JSONEncoder)
