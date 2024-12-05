from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from core_root_api.job_api.models import ApplicationForm
from core_root_api.job_api.serializer.application_form import ApplicationFormSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated

class ApplicationFormViewset(viewsets.ModelViewSet):
    queryset=ApplicationForm.objects.all()
    serializer_class=ApplicationFormSerializer
    permission_classes=[IsAuthenticated]
    parser_classes=[MultiPartParser,FormParser]

    def create(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            print("ok")
            serializer.save(user=request.user)
            return Response({"status":True,"message":"Recieved your job application, you will hear from us regarding your application soon","data":serializer.data},status=status.HTTP_200_OK)
        # return Response({"status":True,"message":""},status=status.HTTP_200_OK)