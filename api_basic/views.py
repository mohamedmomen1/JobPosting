import username as username
from rest_framework import request, serializers
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView
from rest_framework.mixins import CreateModelMixin

from .models import EndUser, JobPosting, HRRUser, Company, Department, Employer, Application
from .serializers import EndUserSerializer, JobPostingSerializer, HRRUserSerializer, CompanySerializer, \
    DepartmentSerializer, ApplicationSerializer, EmployerSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User


class UserDetailsView(RetrieveAPIView):
    serializer_class = EndUserSerializer
    queryset = EndUser.objects.all()
    # kwarg = key word argument


class UsersView(ListAPIView):
    serializer_class = EndUserSerializer
    queryset = EndUser.objects.all()


class ChangeUserAPIView(UpdateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = EndUserSerializer
    queryset = EndUser.objects.all()


class AddEmployer(CreateAPIView):
    serializer_class = EmployerSerializer


    # model = EndUserEmployer
    # fields = '__all__'


# def perform_create(self, serializer):
#   user = serializer.validated_data.get('user_id'),
#  company = serializer.validated_data.get('company_id')
# begin_date = serializer.validated_data.get('begin_date')
# Employer.objects.update_or_create(
#    user=user,
#   company=company,
#  begin_date={"begin_date": begin_date}
# )


# def get_form_kwargs(self):
#   kwargs = super(addEndUserEmployer, self).get_form_kwargs()
#  kwargs.update({'user': self.request.user})
# return kwargs


#  lookup_url_kwarg = 'username'
# lookup_field = 'username'

# def get_queryset(self):
#   return EndUserEmployer.objects.filter(username=self.kwargs['username'])


class HrrDetailsView(RetrieveAPIView):
    serializer_class = HRRUserSerializer
    queryset = HRRUser.objects.all()
    # kwarg = key word argument


class HrrView(ListAPIView):
    serializer_class = HRRUserSerializer
    queryset = HRRUser.objects.all()


class CreateHrrView(CreateAPIView):
    serializer_class = HRRUserSerializer
    model = HRRUser
    fields = '__all__'

    # def perform_create(self, serializer):
    #     serializer.save(name=self.request.user)


class DepartmentDetailsView(RetrieveAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()


class CreateDepartment(CreateAPIView):
    serializer_class = DepartmentSerializer
    model = Department
    fields = '__all__'


class ChangeHrrAPIView(UpdateAPIView):
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


class AddApplication(CreateAPIView):
    serializer_class = ApplicationSerializer
    model = Application
    # fields = '__all__'


class JobPostingDetailsView(RetrieveAPIView):
    serializer_class = JobPostingSerializer
    queryset = JobPosting.objects.all()

    # kwarg = key word argument


class JobPostingView(ListAPIView):
    serializer_class = JobPostingSerializer
    queryset = JobPosting.objects.all()


class ChangeJobPostingAPIView(UpdateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = JobPostingSerializer
    queryset = JobPosting.objects.all()
    # kwarg = key word argument


class JobPostingsForCompanyView(ListAPIView):
    serializer_class = JobPostingSerializer
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
    serializer_class = EmployerSerializer
    queryset = Employer.objects.all()

    def delete(self, request, *args, **kwargs):
        employees = Employer.objects.filter(id=self.kwargs['username'])
        employees.delete()
        return Response({"result": "employees delete"})


class EmployerList(ListAPIView):
    serializer_class = EmployerSerializer
    queryset = Employer.objects.all()
