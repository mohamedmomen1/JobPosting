from rest_framework import serializers
from .models import EndUser, JobPosting, ManagerJobPosting, HRRUser, Company
from django.db import models


class EnduserSerializer(serializers.ModelSerializer):
    class Meta:
        model = EndUser
        # fields = ['id', 'title', 'author', 'email']
        fields = '__all__'


class HRRUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = HRRUser
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


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
