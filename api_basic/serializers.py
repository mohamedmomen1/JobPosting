import datetime

from django.utils import timezone
from rest_framework import serializers
from .models import EndUser, JobPosting, ManagerJobPosting, HRRUser, Company, Department, EndUserEmployer, Application, \
    EmploymentHistory
from django.db import models


class EnduserSerializer(serializers.ModelSerializer):
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
        hrruser = HRRUser.objects.create(username=validated_data['username'],
                                         password=validated_data['password'],
                                         first_name=validated_data['first_name'],
                                         last_name=validated_data['last_name'],
                                         end_user=validated_data['end_user'],

                                         )
        return hrruser


class EndUserEmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = EndUserEmployer
        fields = '__all__'

        def create(self, validated_data: dict):
            employer = EndUserEmployer.objects.create(user=validated_data['user'],
                                                      company=validated_data['company'],
                                                      begin_date=validated_data['begin_date'],

                                                      )
            if employer.objects.create():
                EmploymentHistory.objects.create(
                    begin_date=validated_data[EndUserEmployer.begin_date],
                    end_date=validated_data[timezone.now()],
                    position=validated_data[1],
                    user=validated_data[EndUserEmployer.user],
                    company=validated_data[EndUserEmployer.company]
                )

            return employer


class CompanySerializer(serializers.ModelSerializer):
    department = serializers.IntegerField(required=False)

    class Meta:
        model = Company
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

        def create(self, validated_data: dict):
            department = Department.objects.create(
                company=Company,
                department_id=validated_data['department']
            )
            return department


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

        def create(self, validated_data: dict):
            application = Application.objects.create(job_posting=validated_data['job_posting'],
                                                     user=validated_data['user'],
                                                     apply_date=validated_data['apply_date'],
                                                     resume=validated_data['resume'],
                                                     university=validated_data['university'],
                                                     program=validated_data['program'],
                                                     gpa=validated_data['gpa'],
                                                     standing=validated_data['standing'],
                                                     num_days=validated_data['num_days'],
                                                     )
            return application


class Job_postingSerializer(serializers.ModelSerializer):
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
                                                minimum_days=validated_data.get('minimum_days', None),
                                                kind=validated_data['kind'])

        if job_posting.kind == 'manager':
            ManagerJobPosting.objects.create(
                job_posting=job_posting,
                department_id=validated_data['department']
            )

        return job_posting
