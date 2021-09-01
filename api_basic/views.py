from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView

from .models import EndUser, JobPosting

from .serializers import EnduserSerializer, Job_postingSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class UserDetailsView(RetrieveAPIView):
    serializer_class = EnduserSerializer
    queryset = EndUser.objects.all()
    # kwarg = key word argument


class UsersView(ListAPIView):
    serializer_class = EnduserSerializer
    queryset = EndUser.objects.all()


class ChangeUserAPIView(UpdateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = EnduserSerializer
    queryset = EndUser.objects.all()


class Job_postingDetailsView(RetrieveAPIView):
    serializer_class = Job_postingSerializer
    queryset = JobPosting.objects.all()

    # kwarg = key word argument


class Job_postingView(ListAPIView):
    serializer_class = Job_postingSerializer
    queryset = JobPosting.objects.all()


class ChangeJob_postingAPIView(UpdateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = Job_postingSerializer
    queryset = JobPosting.objects.all()
    # kwarg = key word argument
