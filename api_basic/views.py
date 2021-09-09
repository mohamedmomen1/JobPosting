from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
from django.shortcuts import redirect
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, get_object_or_404
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.reverse import reverse

from .models import EndUser, JobPosting, HRRUser, Company, Department, EndUserEmployer, Application
from rest_framework.response import Response
from rest_framework import generics, viewsets

from .serializers import EnduserSerializer, Job_postingSerializer, HRRUserSerializer, CompanySerializer, \
    DepartmentSerializer, EndUserEmployerSerializer, ApplicationSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics, permissions
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


class addEndUserEmployer(CreateView):
    queryset = EndUserEmployer.objects.all()
    serializer_class = EndUserEmployerSerializer

    def get(self, request, *args, **kwargs):
        serializer = EndUserEmployerSerializer({EndUser, Company})
        return Response(serializer.data)


# def get_form_kwargs(self):
#   kwargs = super(addEndUserEmployer, self).get_form_kwargs()
#  kwargs.update({'user': self.request.user})
# return kwargs


#  lookup_url_kwarg = 'username'
# lookup_field = 'username'

# def get_queryset(self):
#   return EndUserEmployer.objects.filter(username=self.kwargs['username'])


class HRRDetailsView(RetrieveAPIView):
    serializer_class = HRRUserSerializer
    queryset = HRRUser.objects.all()
    # kwarg = key word argument


class HRRsView(ListAPIView):
    serializer_class = HRRUserSerializer
    queryset = HRRUser.objects.all()


class create_hrrView(CreateView):
    serializer_class = HRRUserSerializer
    queryset = HRRUser.objects.all()
    fields = ['username', 'password', 'first_name', 'last_name', 'end_user']

    def post(self, request, *args, **kwargs):
        return super(create_hrrView, self).post(request, *args, **kwargs)


class DepartmentDetailsView(RetrieveAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class create_department_for_company(CreateView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    fields = '__all__'

    def post(self, *args, **kwargs):
        super().post(*args, **kwargs)
        return redirect('create_department_for_company')


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


class addApplication(CreateView):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()
    fields = ['JobPosting', 'EndUser', 'apply_date', 'resume', 'university', 'program', 'gpa', 'standing', 'num_days']


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


class Job_postings_for_companyView(ListAPIView):
    serializer_class = Job_postingSerializer
    queryset = JobPosting.objects.all()
    # queryset = JobPosting.objects.filter(company__name=Company)
    lookup_url_kwarg = 'company'
    lookup_field = 'company'

    def get_queryset(self):
        return JobPosting.objects.filter(company_id=self.kwargs['company'])
    # def get_queryset(self):
    #   qs = super().get_queryset()
    #  return qs.filter(company_id=self.kwargs['company'])


class remove_employee(APIView):
    serializer_class = EndUserEmployerSerializer
    queryset = EndUserEmployer.objects.all()

    def delete(self, request, *args, **kwargs):
        employees = EndUserEmployer.objects.filter(user_id=self.kwargs['username'])

        employees.delete()

        return Response({"result": "employees delete"})

# class Enduserlist(ListAPIView):
#   serializer_class = EndUserEmployerSerializer
#   queryset = EndUserEmployer.objects.all()


# def delete(self, request, *args, **kwargs):
#   employees = EndUserEmployer.objects.filter(user_id=self.kwargs['username'])

#  if employees.count() > 0:
#     employees.delete()
#    return Response("Employer deleted", status=status.HTTP_204_NO_CONTENT)
