from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer, UserSerializerWithToken


from rest_framework import viewsets
from rest_framework import permissions
from .models import Patient,History,Visit,WorkTimes 
from .serializers import PatientSerializer,HistorySerializer,WorkTimesSerializer,VisitSerializer 


import datetime
from django.utils import timezone
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.parsers import JSONParser



@api_view(['GET'])
def current_user(request):
    """
    Determine the current user by their token, and return their data
    """

    serializer = UserSerializer(request.user)
    return Response(serializer.data)

@permission_classes((AllowAny, ))
class UserList(APIView):
    """
    Create a new user. It's called 'UserList' because normally we'd have a get
    method here too, for retrieving a list of all User objects.
    """

    #permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = UserSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class =PatientSerializer
    search_fields=('firstName','nationalCode','lastName')
    ordering_fields='__all__'
    permission_classes = []
    
class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class =HistorySerializer
    ordering_fields='__all__'
    permission_classes = []

class VisitViewSet(viewsets.ModelViewSet):
    queryset= Visit.objects.all()
    serializer_class =VisitSerializer
    ordering_fields='__all__'
    permission_classes = []

class WorkTimesViewSet(viewsets.ModelViewSet):
    queryset= WorkTimes.objects.all()
    serializer_class =WorkTimesSerializer
    ordering_fields='__all__'
    permission_classes = []

#@permission_classes((IsAuthenticated, ))
@permission_classes((AllowAny, ))
class ReservationView(APIView):
    def get(self , request , format=None):
        limit_date = timezone.now()+ datetime.timedelta(days=30)
        q1 = WorkTimes.objects.filter(startTime__gte=timezone.now())
        q2 = q1.filter(startTime__lte=limit_date)
        q3 = q2.exclude(reserved =True)
        available_times = q3[:20]
        serializer = WorkTimesSerializer(available_times , many=True)
        return Response(serializer.data)

@permission_classes((AllowAny, ))
class makeReservation(APIView):
    def post(self , request , format=None):
        serializer = VisitSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        selected_time = serializer.validated_data['time']
        q=WorkTimes.objects.get(startTime=selected_time)
        q.reserved=True
        q.save()
        serializer.save()
        return Response(serializer.data , status=status.HTTP_201_CREATED)


