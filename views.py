from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView

from .models import EndUser, JobPosting, HRRUser, Company

from .serializers import EnduserSerializer, Job_postingSerializer, HRRUserSerializer, CompanySerializer
from django_filters import rest_framework as filters

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


class HRRDetailsView(RetrieveAPIView):
    serializer_class = HRRUserSerializer
    queryset = HRRUser.objects.all()
    # kwarg = key word argument


class HRRsView(ListAPIView):
    serializer_class = HRRUserSerializer
    queryset = HRRUser.objects.all()


class ChangeHRRAPIView(UpdateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = HRRUserSerializer
    queryset = HRRUser.objects.all()


class CompanyDetailsView(RetrieveAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    # kwarg = key word argument


class CompanyView(ListAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


class ChangeCompanyAPIView(UpdateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = CompanySerializer
    queryset = Company.objects.all()


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


class Job_postingDetailsView1(ListAPIView):
    serializer_class = Job_postingSerializer
    queryset = JobPosting.objects.all()
    # queryset = JobPosting.objects.filter(company__name=Company)
    lookup_url_kwarg = 'company'
    lookup_field = 'company'

    def get_queryset(self):
        # original qs
        qs = super().get_queryset()
        # filter by a variable captured from url, for example
        return qs.filter(company_id=self.kwargs['company'])

