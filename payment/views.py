from django.shortcuts import render

def pay(request,pk):
    return render(request, 'payment/payment.html')