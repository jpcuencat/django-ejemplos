from django.shortcuts import render
from logins.forms import UserForm,UserProfileInfoForm

# Create your views here.
def index(request):
    #my_dict = {'insert_me':"Hola estoy desde la app proyecto1/aplicacion1"}
    return render(request,'logins/index.html')

def login(request):
    #my_dict = {'insert_me':"Hola estoy desde la app proyecto1/aplicacion1"}
    return render(request,'logins/login.html')


def registro(request):
    registrado = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'portfolio_pic' in request.FILES:
                profile.portfolio_pic = request.FILES['portfolio_pic']                
            profile.save()

            registrado = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'logins/registro.html',
    {'user_form':user_form,'profile_form':profile_form,'registrado':registrado})
