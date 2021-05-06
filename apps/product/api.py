from rest_framework import generics
from rest_framework.response import Response
from .serializers import EmployeeSerializer,ItemSerializer,TeamSerializer,AssignItemSerializer,CatagorySerializer
from .models import *

class EmployeeCreateApi(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeApi(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeDeleteApi(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class ItemCreateApi(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemApi(generics.ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ItemDeleteApi(generics.DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class TeamCreateApi(generics.CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamApi(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TeamDeleteApi(generics.DestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class AssignItemCreateApi(generics.CreateAPIView):
    queryset = AssignItem.objects.all()
    serializer_class = AssignItemSerializer

class AssignItemApi(generics.ListAPIView):
    queryset = AssignItem.objects.all()
    serializer_class = AssignItemSerializer

class AssignItemUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = AssignItem.objects.all()
    serializer_class = AssignItemSerializer

class AssignItemDeleteApi(generics.DestroyAPIView):
    queryset = AssignItem.objects.all()
    serializer_class = AssignItemSerializer

class CatagoryCreateApi(generics.CreateAPIView):
    queryset = Catagory.objects.all()
    serializer_class = CatagorySerializer

class CatagoryApi(generics.ListAPIView):
    queryset = Catagory.objects.all()
    serializer_class = CatagorySerializer

class CatagoryUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Catagory.objects.all()
    serializer_class = CatagorySerializer

class CatagoryDeleteApi(generics.DestroyAPIView):
    queryset = Catagory.objects.all()
    serializer_class = CatagorySerializer