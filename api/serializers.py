from rest_framework import serializers
from api.models import company
#create  Serializers here

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=company
        fields="__all__"
