from django.contrib.auth import get_user_model ,login , logout , authenticate 
from django.shortcuts import redirect, render

client = get_user_model()
# Create your views here.
def log(req):
    if req.method == 'POST':
        nom=req.POST['nom']
        password=req.POST['password']
        verif = authenticate(username=nom,password=password)
        if verif:
            login(req,verif)
            return redirect('index')
        else:
            return render(req,'acounts/login2.html',{'alert':1})


        print(req.POST)

    
    return render(req,'acounts/login2.html')


def inscription(req):
    if req.method == 'POST':
        # print(req.POST)
        email=req.POST['email']
        password=req.POST['password']
        nom=req.POST['nom']
        prenom=req.POST['prenom']
        verif = authenticate(username=nom,password=password)
        if not verif:
            user=client.objects.create_user(username=nom,
                                    password=password)

            login(req, user)
            return redirect('index')
    
    return render(req,'acounts/inscription.html')

def deco(req):
    logout(req)
    return redirect('index')