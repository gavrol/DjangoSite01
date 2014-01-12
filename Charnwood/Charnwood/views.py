from django.http import HttpResponse, Http404
from django.shortcuts import render
#from ASXstocks.models import Stock
from forms import ContactForm
from django.http import HttpResponseRedirect

#def Charnwood(request,template_name):
#    return render(request,'/'+template_name+'/')
    
def CharnwoodInfo(request):
    return render(request,'CharnwoodInfo.html')    
 
def RBCSgrievances(request):
    return render(request,'RBCSgrievances.html')    

def SpecialGeneralMeeting(request):
    return render(request,'SpecialGeneralMeeting.html')    
   

from django.core.mail import send_mail

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['djex1@mopi.com.au'],
            )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm(
            initial={'subject': '',
                     'message': 'Your message here'}
        )
    return render(request, 'contact_form.html', {'form': form})
 
