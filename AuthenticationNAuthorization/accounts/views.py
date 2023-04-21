from django.shortcuts import render
from .models import User,UserManager
# from django.contrib.auth.models import User as usr
from .serializers import UserSerializer, SignUpSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework import status



# Create your views here.
@api_view(['GET'])
def get_all_user(request):
    data=User.objects.all()
    print("This is User",data)
    serializer=UserSerializer(data, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def register(request):
    data = request.data

    user = SignUpSerializer(data=data)

    if user.is_valid():
        if not User.objects.filter(username=data['email']).exists():
            user = User.objects.create(
                first_name = data['first_name'],
                last_name = data['last_name'],
                username = data['email'],
                email = data['email'],
                password = make_password(data['password'])
            )
            

            return Response({
                'message': 'User registered successfully'},
                status=status.HTTP_200_OK
            ) 
        else:
            return Response({
                'error': 'User already exists'},
                status=status.HTTP_400_BAD_REQUEST
            ) 
    else:
        return Response(user.errors)  

   
    
    
    



