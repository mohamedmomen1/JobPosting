from django.db import models


class EndUser(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=300)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    military_service_stat = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class HRRUser(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=300)
    email = models.EmailField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    end_user = models.ForeignKey(EndUser, on_delete=models.PROTECT)

    def __str__(self):
        return self.username


class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class EndUserEmail(models.Model):
    user = models.ForeignKey(EndUser, on_delete=models.PROTECT)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.email


class EmploymentHistory(models.Model):
    begin_date = models.DateTimeField()
    end_date = models.DateTimeField()
    position = models.CharField(max_length=100)
    user = models.ForeignKey(EndUser, on_delete=models.PROTECT)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.beginDate = None

    def __str__(self):
        # TODO beginDate is not defined
        # TODO format the return properly
        return self.beginDate


class EndUserEmployer(models.Model):
    user = models.ForeignKey(EndUser, on_delete=models.PROTECT)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    begin_date = models.DateTimeField()


class JobPosting(models.Model):
    description = models.CharField(max_length=100)
    salary = models.FloatField(max_length=100)
    phone = models.CharField(max_length=100)

    num_openings = models.IntegerField()
    hrr_user = models.ForeignKey(HRRUser, on_delete=models.PROTECT)

    opening_date = models.DateTimeField()
    duration = models.IntegerField()

    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    is_man_or_intern = models.CharField(max_length=100)
    contract_type = models.CharField(max_length=100)

    minimum_days = models.IntegerField(null=True, blank=True)
    kind = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class Department(models.Model):
    name = models.CharField(max_length=100)
    size = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    job_posting = models.ForeignKey(JobPosting, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class ManagerJobPosting(models.Model):
    job_posting = models.ForeignKey(JobPosting, on_delete=models.PROTECT)
    dept_name = models.CharField(max_length=100)
    dept_size = models.IntegerField()
    department = models.ForeignKey('Department', on_delete=models.PROTECT)

    def __str__(self):
        return self.job_posting


class Application(models.Model):
    job_posting = models.ForeignKey(JobPosting, on_delete=models.PROTECT)
    user = models.ForeignKey(EndUser, on_delete=models.PROTECT)
    apply_date = models.DateTimeField()
    resume = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    program = models.CharField(max_length=100)
    gpa = models.FloatField(max_length=100)
    standing = models.CharField(max_length=100)
    num_days = models.IntegerField()

    def __str__(self):
        return self.job_posting


class CoursesForInterShipApps(models.Model):
    name = models.ForeignKey(EndUser, on_delete=models.PROTECT)
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.id


class InternshipJobPosting(models.Model):
    job_posting = models.ForeignKey(JobPosting, on_delete=models.PROTECT)
    minimum_days = models.IntegerField()

    def __str__(self):
        return self.job_posting
