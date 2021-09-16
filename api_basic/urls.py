from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UserDetailsView, ChangeUserAPIView, UsersView, JobPostingDetailsView, ChangeJobPostingAPIView, \
    JobPostingView, HrrView, HrrDetailsView, ChangeHrrAPIView, CompanyView, ChangeCompanyAPIView, CompanyDetailsView, \
    remove_employee, CreateHrrView, AddEmployer, AddApplication, \
    DepartmentDetailsView, CreateDepartment, EmployerList

#
# urlpatterns = [
#   path('ViewSet/', include(router.urls)),
#  path('ViewSet/<int:pk>/', include(router.urls)),

# path('enduser/', enduser_list),
#   path('enduser/', EnduserAPIView.as_view()),
# path('detail/<int:pk>/',enduser_detail),
#  path('detail/<int:id>/', EnduserDetails.as_view()),
# path('generic/enduser/<int:id>', GenericsAPIView.as_view()),

# ]

urlpatterns = [
    # slug for string
    # int for int
    # Company
    path('user/<int:pk>', UserDetailsView.as_view()),
    path('user/', UsersView.as_view()),
    path('user/add', AddEmployer.as_view()),

    path('user/<int:pk>/change', ChangeUserAPIView.as_view()),
    path('HRR/create/', CreateHrrView.as_view()),
    path('HRR/<int:pk>', HrrDetailsView.as_view()),
    path('HRR/', HrrView.as_view()),
    path('HRR/<int:pk>/change', ChangeHrrAPIView.as_view()),

    path('company/<int:pk>', CompanyDetailsView.as_view()),
    path('company/', CompanyView.as_view()),
    path('company/<int:pk>/change', ChangeCompanyAPIView.as_view()),

    # path('Enduserlist', Enduserlist.as_view()),
    path('Employer/remove/<int:username>', remove_employee.as_view()),
    path('Employer/List/', EmployerList.as_view()),

    path('Department/create', CreateDepartment.as_view()),
    path('Department/<int:pk>', DepartmentDetailsView.as_view()),
    path('application/add', AddApplication.as_view()),

    path('Job/<int:pk>', JobPostingDetailsView.as_view()),
    path('Job/', JobPostingView.as_view()),
    path('Job/<int:pk>/change', ChangeJobPostingAPIView.as_view()),
    # path('Job/company/<int:company>', Job_postings_for_companyView.as_view())

]
