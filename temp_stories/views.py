from django.shortcuts import render
from faker import Faker
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

# Create your views here.
def story():
    fake = Faker()
    mystory = (
                f"In a(n) {fake.company()} a young {fake.language_name()}" 
                f"stumbles across a(n) {fake.domain_word()} which spurs him into conflict with {fake.name() }"
                f"an {fake.catch_phrase()} with the help of a(n) {fake.job()} and her {fake.file_name()}"
                f" culminating in a struggle at {fake.company()} where someone shouts {fake.bs()}"
                )
    return mystory


def index(request):
    mystory = story()
    
    return render(request, 'temp_stories/index.html', {'story': mystory})


def temp(request):
    converted_t = None
    temp = None
    p1 = None
    p2= None
    if request.method== "POST":
        temp = int(request.POST.get('temp',))
        temp_from = request.POST.get('temp_from','')
        temp_to = request.POST.get('temp_to','')
       
        if temp_from == temp_to:
            messages.add_message(request, messages.INFO, "Please enter a valid conversion type, check if you selected Fahreinheit or celsius twice")
            return HttpResponseRedirect(reverse('temp'))
        
        elif temp_from == "F" and temp_to =="C":
            converted_t = round((temp-32)*0.5556, 2)
            p1 = "F"
            p2 = "C"
        else:
            converted_t = (temp*1.8)+32
            p1= "C"
            p2= "F"

    return render(request, 'temp_stories/temp.html', {'converted_t': converted_t, 'temp':temp, 'p1':p1, 'p2':p2})