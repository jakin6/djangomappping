import re
from django.views.generic import View
from django.shortcuts import render
from .models import *
# Create your views here.
class HomeView(View):
    def get(self,request,*args,**kwargs):
        # getting all person
        # allPersons=Person.objects.all()
        # person=Person.objects.get(id=1)

        # person with its interests
        # for interest in person.interests.all():
        #     print(interest)
        # persons with his city  
        # addressP=person.personaddress
        # print (addressP.city,addressP.street_address)    
       
        # person in a specific city
        # city=City.objects.get(id=2)
        # print(city)
        # because we don't have  attribute person in city model u need to use _set.all()in order to access person name
        # all_persons_address=city.personaddress_set.all()
        # if you do not need to use _set.all()
        # all_persons_address=city.person_city.all()
        # for address in all_persons_address:
        #     print(address.person)
        
        # get people with on interest
        interest=Interest.objects.get(id=1)
        print(interest)
        # interest_persons=interest.person_set.all()
        # interest_persons=interest.person_set.all()
        # for interest in interest_persons:
        #print(interest)
        context={}
        return render(request,'home.html',context)
    