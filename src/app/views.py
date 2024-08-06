from django.shortcuts import render, HttpResponse
from app.tasks import test_func
# Create your views here.
def test(request):
    test_func.delay()
    return HttpResponse("Done")