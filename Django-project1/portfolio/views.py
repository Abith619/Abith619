from django.shortcuts import render,redirect
from portfolio.models import person
from portfolio.forms import personform
# Create your views here.
def home(request):

    if request.method == "POST":  
        form=personform(request.POST)
        if form.is_valid():   
            form.save()
            return redirect('portfolio:show')
        else:
            print(form.errors)
    else:  
        form = personform() 
    data={'form':form}
    return render(request, 'home.html',data) 
def show(request):
     persons = person.objects.all()  
     print(persons)
     return render(request,"show.html",{'persons':persons})  

def edit(request, pk): 
    print('pk',pk) 
    instance = person.objects.get(id=pk)
    form = personform(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('portfolio:show')
    return render(request,'edit.html', {'form':form})  

def destroy(request,pk):  
    persons = person.objects.get(id=pk)  
    persons.delete()  
    return redirect("portfolio:show")  

def normalform(request):
    if (request.POST):
        print(request.POST)
        firstname=request.POST.get('firstname')
        print('f',firstname)
        lastname=request.POST.get('lastname')
        print('l',lastname)
        email=request.POST.get('email')
        print('e',email)
        phone_number=request.POST.get('phone_number')
        print('p',phone_number)
        createperson=person.objects.create(first_name=firstname,last_name=lastname,email=email,phone_number=phone_number)
    return render(request,'form1.html')  


    # return render(request,"form1.html")

    