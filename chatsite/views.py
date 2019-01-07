from django.contrib import auth
from chatsite.models import user
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
class users(View):
    form_class=user
    template_name="chatsite/site.html"

    def get(self,request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            username=form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username ,password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('user/index')

        return render(request, self.template_name, {'form': form})


class login_form(View):
    template_name='chatsite/login_form.html'
    form_class=user

    def post(self, request):
        form = self.form_class(None)
        username = request.POST.get('username')
        password=request.POST.get('password')
        #data=Member.objects.get(username)
        user=authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            return render(request, self.template_name, {'form': form,  'userpassunmatch': True})




    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form,'p':False})