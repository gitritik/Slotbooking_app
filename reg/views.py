from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect, HttpResponse
from reg.models import Booking
from reg.models import Day
from reg.models import slTime
from reg.models import Sport
from .forms import BookKaro
def index(request):
    booking=Booking.objects.all()
    slots=slTime.objects.all()
    days=Day.objects.all()
    sports=Sport.objects.all()
    sllist=list(slots)
    
        

    return render(request,"home.html",{'sports':sports, 'days':days,'slots':slots})

# Create your views here.
def forming(request):
    submitted=False
    if request.method=="POST":
        form=BookKaro(request.POST)
        day=request.POST['bookday']
        sport=request.POST['booksport']
        slot=request.POST['bookslot']
        if form.is_valid():
            if Booking.objects.filter(bookday=day,booksport=sport,bookslot=slot).exists():
                return render(request,'error.html')


            else:    
                form.save()
                return render(request,'posted.html')
    else:
        form=BookKaro
        if submitted in request.GET:
            submitted=True

    return render(request,'form.html',{"form":form,"submitted":submitted})

def posted(request):
    return render(request,'posted.html')