from django.conf.urls import url
from .views import *
urlpatterns = [
    url(r'news/$', NewsView.as_view()),
    url(r'enterprise/$', EnterpriseView.as_view()),
    url(r'employee/$', EmployeeView.as_view()),
    url(r'enterprise/index/$', IndexEnterpriseView.as_view()),
    url(r'employee/partner/$', EmployeePartnerView.as_view()),
    url(r'employee/global/$', EmployeeGlobalView.as_view()),
    url(r'employee/manager/$', EmployeeManagerView.as_view()),
    url(r'employee/adviser/$', EmployeeAdviserView.as_view()),
    url(r'employee/post_investment/$', EmployeePostView.as_view()),
    url(r'employee/legal/$', EmployeeLegalView.as_view()),
    url(r'employee/operation/$', EmployeeOperationView.as_view()),
    url(r'search/$', SearchView.as_view()),
]
