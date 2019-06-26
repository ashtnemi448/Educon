from django.conf.urls import url, include
from . import views


app_name = 'administrator'

urlpatterns = [
    url(r'^dashboard/$', views.dashboard, name="dashboard"),
    url(r'^studentApproval/$', views.studentApproval, name="studentApproval"),
]
