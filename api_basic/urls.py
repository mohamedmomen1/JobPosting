from django.urls import path

from .views import UserDetailsView, ChangeUserAPIView, UsersView, Job_postingDetailsView, ChangeJob_postingAPIView, \
    Job_postingView, HRRsView, HRRDetailsView, ChangeHRRAPIView, CompanyView, ChangeCompanyAPIView, CompanyDetailsView, \
    Job_postings_for_companyView, remove, create_hrrView, addEndUserEmployer,addApplication,Enduserlist

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

    path('user/<int:pk>/change', ChangeUserAPIView.as_view()),

    path('HRR/<int:pk>', HRRDetailsView.as_view()),
    path('HRR/', HRRsView.as_view()),
    path('HRR/<int:pk>/change', ChangeHRRAPIView.as_view()),

    path('Company/<int:pk>', CompanyDetailsView.as_view()),
    path('Company/', CompanyView.as_view()),
    path('Company/<int:pk>/change', ChangeCompanyAPIView.as_view()),

    path('addEndUserEmployer/',addEndUserEmployer.as_view()),
    path('Enduserlist',Enduserlist.as_view()),
    path('removeEmployer/<int:username>', remove.as_view()),

    path('createHRR', create_hrrView.as_view()),
    path('addapplication',addApplication.as_view()),

    path('Job/<int:pk>', Job_postingDetailsView.as_view()),
    path('Job/', Job_postingView.as_view()),
    path('Job/<int:pk>/change', ChangeJob_postingAPIView.as_view()),
    path('Job_postings_for_company/<int:company>', Job_postings_for_companyView.as_view())

]
