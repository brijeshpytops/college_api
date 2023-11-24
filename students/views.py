from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import studentSerializers
from .models import student

@api_view(['GET', 'POST'])
def studentList(request):
    if request.method == 'GET':
        queryset = student.objects.all()
        serializer = studentSerializers(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = studentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

       

@api_view(['GET', 'PATCH'])
def studentDetails(request, id):
    try:
        queryset = student.objects.get(pk=id)
    except student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = studentSerializers(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PATCH':
        serializer = studentSerializers(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)