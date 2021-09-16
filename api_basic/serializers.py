from django.utils import timezone
from rest_framework import serializers, status
from rest_framework.fields import empty
from django.contrib.auth.models import User
from rest_framework.response import Response

from .models import EndUser, JobPosting, ManagerJobPosting, HRRUser, Company, Department, Employer, \
    Application, EmploymentHistory, InternshipJobPosting


class EndUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EndUser
        # fields = ['id', 'title', 'author', 'email']
        fields = '__all__'

    def create(self, validated_data: dict):
        endUser = EndUser.objects.create(username=validated_data['username'],
                                         password=validated_data['password'],
                                         first_name=validated_data['first_name'],
                                         last_name=validated_data['last_name'],
                                         end_user=EndUser.username

                                         )
        return endUser


class EmploymentHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploymentHistory
        fields = '__all__'


class HRRUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = HRRUser
        fields = '__all__'

    def create(self, validated_data: dict):
        hrrUser = HRRUser.objects.create(username=validated_data['username'],
                                         password=validated_data['password'],
                                         first_name=validated_data['first_name'],
                                         last_name=validated_data['last_name'],
                                         end_user=validated_data['end_user'],

                                         )
        return hrrUser


class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = '__all__'

    def post(self, request):
        serialized = EmployerSerializer(data=request.data)
        if serialized.is_valid():
            u = User.objects.filter(user=serialized.data['user'])
            user = User.objects.get(username=serialized.data['user'])
            if len(u) > 0:
                employer, created = Employer.objects.get_or_create(user=user)
                return Response({'Employer': employer.key}, status=status.HTTP_200_OK)


#  def update(self, instance, validated_data):
# validated data doesn't have email here, that's why getting value from self.initial_data
#     if self.initial_data.get("user"):

#           instance.user.user = self.initial_data.get("user")
#            instance.user.save()

#      instance.save()
#     return instance
# user = serializers.CharField(required=False)


# if not Employer.objects.filter(user=user).exists():
#    class Meta:
#       model = Employer
#      fields = '__all__'
# else:
#   print('this is alredy exists')


class CompanySerializer(serializers.ModelSerializer):
    department = serializers.IntegerField(required=False)

    class Meta:
        model = Company
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'


class JobPostingSerializer(serializers.ModelSerializer):
    department = serializers.IntegerField(required=False)

    class Meta:
        model = JobPosting
        fields = '__all__'

    def create(self, validated_data: dict):
        job_posting = JobPosting.objects.create(description=validated_data['description'],
                                                salary=validated_data['salary'], phone=validated_data['phone'],
                                                num_openings=validated_data['num_openings'],
                                                hrr_user=validated_data['hrr_user'],
                                                opening_date=validated_data['opening_date'],
                                                duration=validated_data['duration'],
                                                company=validated_data['company'],
                                                is_man_or_intern=validated_data['is_man_or_intern'],
                                                contract_type=validated_data['contract_type'],
                                                kind=validated_data['kind'])

        if job_posting.kind == 'manager':
            ManagerJobPosting.objects.create(
                job_posting=job_posting,
                department_id=validated_data['department']
            )
        if job_posting.kind == 'Intern':
            InternshipJobPosting.objects.create(
                job_posting=job_posting,
                minimum_days=validated_data.get('minimum_days')
            )

        return job_posting
