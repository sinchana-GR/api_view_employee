from django.shortcuts import render
from rest_framework.response import Response
from app.models import *
from app.serializers import *
# Create your views here.
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def employeedata(request):
    EMPDATA=Employee.objects.all()
    EMPJSONDATA=EmployeeModelSerializers(EMPDATA,many=True)
    return Response(EMPJSONDATA.data)