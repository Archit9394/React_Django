from django.shortcuts import render
import requests
import json 
# Create your views here.
def login(request):
    return render(request, 'signup_1.html')

def submitUser(request):
    email=request.GET['email']
    password=request.GET['password']
    name=request.GET['username']
    print (email,password,name,"this is me")
    url = "http://127.0.0.1:8000/api/login/"

    payload = {"email":email,"password":password,"name":name}
    payload=json.dumps(payload)
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data = payload)
    data=response.text
    return render(request,'success.html',{'data':data})