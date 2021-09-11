from django.contrib import admin
# from .models import hRRs
from .models import EndUser
from .models import Company
from .models import HRRUser
# from .models import Eu_emails
from .models import EmploymentHistory
from .models import EndUserEmployer
from .models import JobPosting
from .models import Department

# from .models import Manager_job_posting
from .models import Application

# from .models import CoursesForInterShipApps
# from .models import InternshipJobPosting

# Register your models here...
admin.site.register(HRRUser)
admin.site.register(EndUser)
admin.site.register(Company)
admin.site.register(Department)
# admin.site.register(Eu_emails)
admin.site.register(EmploymentHistory)
admin.site.register(EndUserEmployer)
admin.site.register(JobPosting)
# admin.site.register(Manager_job_posting)
admin.site.register(Application)
# admin.site.register(CoursesForInterShipApps)
# admin.site.register(InternshipJobPosting)
