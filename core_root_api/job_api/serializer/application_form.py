from core_root_api.job_api.models import ApplicationForm
from rest_framework import serializers

class ApplicationFormSerializer(serializers.ModelSerializer):
    class Meta:
        model=ApplicationForm
        exclude=['user']