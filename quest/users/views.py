#from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from .forms import UserCreationForm


class Register(View):
        template_name = 'registration/register.html'
        def get(self,request):

                context = {
                        'form': UserCreationForm()
                }
                return render(request,self.template_name,context)
        def post(self,request):
                form = UserCreationForm(request.POST)
                if(form.is_valid()):
                        form.save()
                        return HttpResponseRedirect(reverse('home'))
                        #return render(request, 'main/index.html')
                context = {
                        'form' : form
                }
                return render(request,self.template_name,context)
@login_required
def profile(request):
        return render(request,'registration/profile.html')
# Create your views here.
