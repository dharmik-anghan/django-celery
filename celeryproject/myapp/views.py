from django.shortcuts import render, HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from myapp.tasks import add
from celeryproject.celery import sub
from celery.result import AsyncResult

class IndexView(APIView):
    def get(self, request):
        print("Index: ")
        result1 = add.apply_async(args=[10,20])
        print("Result 1...", result1)
        result2 = sub.apply_async(args=[10,110])
        print("Result 2...", result2)

        return HttpResponse(f"Result 1..., {result1} <br>Result 2..., {result2}")
    
class CheckResult(APIView):
    def get(self, request, task_id):
        result = AsyncResult(task_id)
        print("Check Result...",result.status)
        results = f"""
            "result_id" : {result.id},<br>
            "task_id" : {result.task_id},<br>
            "state" : {result.state},<br>
            "status" : {result.status},<br>
            "value" : {result.result},<br>
            "ready" : {result.ready()},<br>
            "successful" : {result.successful()},<br>
            "failed" : {result.failed()},<br>
        """
        print("Check Results...",results)
        return HttpResponse(results)


class AboutView(APIView):
    def get(self, request):
        print("About: ")
        return Response({"about": "this is about views"}, status=200)


class ContactView(APIView):
    def get(self, request):
        print("Contact: ")
        return Response({"contact": "this is contact views"}, status=200)
