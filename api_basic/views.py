from django.http import HttpResponse, HttpResponseNotFound
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView
from .models import EndUser, JobPosting, HRRUser, Company, Department, Employer, Application,EmploymentHistory
from .serializers import EndUserSerializer, JobPostingSerializer, HRRUserSerializer, CompanySerializer, \
    DepartmentSerializer, ApplicationSerializer, EmployerSerializer,EmploymentHistorySerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.utils import timezone



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
    model = Employer
    fields = '__all__'


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

    def create(self, request, *args, **kwargs):
        EmploymentHistory.objects.create(begin_date=[Employer.begin_date],
                                         end_date=[timezone.now],
                                         position=["print"],
                                         user=[Employer.user],
                                         company=[Employer.company]

                                         )

    def delete(self, request, *args, **kwargs):
        employees = Employer.objects.filter(id=self.kwargs['username'])
        employees.delete()
        return Response({"result": "employees delete"})


class EmployerList(ListAPIView):
    serializer_class = EmployerSerializer
    queryset = Employer.objects.all()
