from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models,serializers
from rest_framework import viewsets
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.pagination import PageNumberPagination


@api_view(['GET','POST'])
def index(request):

    courses = {
        'course_name': 'Python',
        'learning' : ['Python', 'Django', 'Flask'],
        'Course_Provider': 'Guhan',
    }

    return Response(courses)


class PersonAPI(APIView):

    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self,request):
        objs = models.Person.objects.all()
        # objs = models.Person.objects.filter(color__isnull = False)
        paginator = PageNumberPagination()
        paginator.page_size = 5  # You can set this or use global setting
        result_page = paginator.paginate_queryset(objs, request)
        serializer = serializers.PeaopleSerializer(result_page , many = True)
        # return Response(serializer.data)
        return paginator.get_paginated_response(serializer.data)

    def post(self,request):
        data = request.data
        serializer = serializers.PeaopleSerializer(data = data)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    def put(self, request):
        data = request.data
        if 'id' not in data:
            return Response({'error': 'ID is required for update'}, status=400)
        
        try:
            obj = models.Person.objects.get(id=data['id'])
            serializer = serializers.PeaopleSerializer(obj, data=data, partial=True)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            
            return Response(serializer.errors)
        
        except models.Person.DoesNotExist:
            return Response({'error': 'Person not found'}, status=404)
    
    def delete(self,request):
        data = request.data
        obj = models.Person.objects.get(id = data['id'])
        obj.delete()
        return Response({'msg':'Deleted Successfully'})

@api_view(['GET','POST','PUT','DELETE'])
def person(request):

    if request.method == 'GET':

        objs = models.Person.objects.all()
        # objs = models.Person.objects.filter(color__isnull = False)
        serializer = serializers.PeaopleSerializer(objs , many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':

        data = request.data
        serializer = serializers.PeaopleSerializer(data = data)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'PUT':

        data = request.data
        obj = models.Person.objects.get(id = data['id'])
        serializer = serializers.PeaopleSerializer(obj , data = data , partial = True)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'PATCH':

        data = request.data
        obj = models.Person.objects.get(id = data['id'])
        serializer = serializers.PeaopleSerializer(obj , data = data , partial = True)

        if serializer.is_valid():

            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors)
    
    elif request.method == 'DELETE':
            
        data = request.data
        obj = models.Person.objects.get(id = data['id'])
        obj.delete()
        return Response({'msg':'Deleted Successfully'})


@api_view(['POST'])
def login(request):

    data = request.data
    serializer = serializers.LoginSerializer(data = data)

    if serializer.is_valid():
        return Response({'message':'success'})
    
    return Response(serializer.errors)

class Peopleviewset(viewsets.ModelViewSet):
    serializer_class = serializers.PeaopleSerializer
    queryset = models.Person.objects.all()



class RegisterAPI(APIView):
    
    def post(self, request):
        
        data = request.data
        serializer = serializers.RegisterSerializer(data=data)

        if not serializer.is_valid():
            return Response({
                'status': False,
                'message': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        
        return Response({
            'status': True,
            'message': 'User Created'
        }, status=status.HTTP_201_CREATED)

class LoginAPI(APIView):
    def post(self,request):
        data = request.data
        serializer = serializers.LoginSerializer(data = data)
        if not serializer.is_valid():
            print('*'*20)
            print("Not valid")
            print('*'*20)
            return Response({
                'status': False,
                'message': serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(username = serializer.data['username'],password = serializer.data['password'])
        token,_ = Token.objects.get_or_create(user = user)
        if not user:
            return Response({
                'status': False,
                'message': 'not valid credentials'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        return Response({
            'status': True,
            'message': 'User Login',
            'token':str(token)
        }, status=status.HTTP_201_CREATED)