from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


def index(request):
    return render(request, 'rootapp/index.html')


# @api_view()
# def index(request):
#     return Response({"Message": "This view is for api testing."}, status=status.HTTP_200_OK)
