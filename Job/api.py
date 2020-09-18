##  views 
from .models import job
from .serializers import jobSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics


@api_view(['GET'])
def job_list_api(request):
    all_jobs = job.objects.all()
    data = jobSerializer(all_jobs,many=True).data
    return Response({'data':data})

@api_view(['GET'])
def job_detail_api(request,id):
    job_detail = job.objects.get(id=id)
    data = jobSerializer(job_detail).data
    return Response({'data':data})



class Job_List_Api(generics.ListCreateAPIView):
    queryset = job.objects.all()
    serializer_class =  jobSerializer

class Job_Detail_Api(generics.RetrieveUpdateDestroyAPIView):
    queryset = job.objects.all()
    serializer_class =  jobSerializer
    lookup_field = 'id'