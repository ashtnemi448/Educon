from django.shortcuts import render, get_object_or_404
from auth.models import User,Student

def dashboard(request):
    studentIterator=Student.objects.all()
    context={
        'page': 'dashboard',
        'studentIterator':'studentIterator',
    }
    return render(request, 'administrator/adminPortal.html')


def studentApproval(request):
    context = {
        'page': 'studentApproval',
    }
    return render(request, 'administrator/studentApproval.html')
