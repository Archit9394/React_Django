from django.shortcuts import render
import requests
import json 
# Create your views here.
def login(request):
    return render(request, 'signup_1.html')

def signin(request):
    return render(request,'signin.html')

def submitUser(request):
    email=request.GET['email']
    password=request.GET['password']
<<<<<<< HEAD
    username=request.GET['username']
    print (email,password,username,"this is me")
    url = "http://127.0.0.1:3002/api/login/"
=======
    name=request.GET['username']
    print (email,password,name,"this is me")
    url = "http://localhost:5050/api/login/"
>>>>>>> d3af791b7b0f61e87caf164b4d94532806682b83

    payload = {"email":email,"password":password,"username":username}
    payload=json.dumps(payload)
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data = payload)
    data=response.text
    return render(request,'success.html',{'data':data})

def getUser(request):
    email=request.GET['email']
    password=request.GET['password']
    #name=request.GET['username']
    print (email,password,"this is me")
    #print (email,password,name,"this is me")
<<<<<<< HEAD
    url = "http://127.0.0.1:3002/api/login/"
=======
    url = "http://localhost:5050/api/login/"
>>>>>>> d3af791b7b0f61e87caf164b4d94532806682b83

    payload = {"email":email,"password":password,"username":username}
    #payload = {"email":email,"password":password,"name":name}
    payload=json.dumps(payload)
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data = payload)
    data=response.text
    return render(request,'success.html',{'data':data})
