from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import UserData

# Create your views here.
def index(request):
    # userdata = [{'fullname': 'SAKEEB SHEIKH', 'emailid': 'sakeeb@gmail.com', 'contact': '1234567892', 'address': 'Pune, Maharashtra', 'username':'sakeebhsheikh'},
    # {'fullname': 'AMOL PATIL', 'emailid': 'sakeeb@gmail.com', 'contact': '1234567892', 'address': 'Pune, Maharashtra', 'username':'sakeebhsheikh'},
    # {'fullname': 'VAIBHAV S', 'emailid': 'sakeeb@gmail.com', 'contact': '1234567892', 'address': 'Pune, Maharashtra', 'username':'sakeebhsheikh'},
    # {'fullname': 'SHIVANI S', 'emailid': 'sakeeb@gmail.com', 'contact': '1234567892', 'address': 'Pune, Maharashtra', 'username':'sakeebhsheikh'}]

    alldata = UserData.objects.all()

    return render(request, 'index.html', context={'data': alldata})

def register(request):

    return render(request, 'register.html')

def deleteme(request, id):
    obj = UserData.objects.get(id=id)
    obj.delete()

    # alldata = UserData.objects.all()

    # return render(request, 'index.html', context={'data': alldata})

    index(request)

"""
def registerme(request):

    #obj = UserData(fullname='Amol Patil', emailid='amol@gmail.com', contact='1234567897', address='pune, maharashtra', username='amol123', password='Amol@123')
    obj.save()
    return render()
"""