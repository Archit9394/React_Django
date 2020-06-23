from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from .models import UserAPI
from .serializers import UserApiSerializer
class UserAPIView(APIView):
    def get(self,request):
        print(request.data)
        queryset=UserAPI.objects.filter(email=request.data.get('email'))
        print (queryset)
        if queryset:
            if queryset.values('password').first()['password']==request.data.get('password'):
                return Response("You are successfully logged in ")
            else:
                return Response ("Password Incorrect")
        else:
            return Response("User is not registered")

    def post(self,request):
        queryset=request.data
        serializer=UserApiSerializer(data=queryset)
        if serializer.is_valid(raise_exception=True):
            save_data=serializer.save()
        return Response({"Success":"User '{}' created successfully".format(save_data.name)})