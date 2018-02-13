
from rest_framework import serializers
from school_mgmt.models import *
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from random import randint


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')



class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name','username', 'email', 'password')


#add
class UniversityCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        exclude = ('created_at')

class SchoolCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        exclude = ('created_at','modified_at')

class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        #exclude = ('created_at','modified_at')


#list
class SchoolListSerializer(serializers.ModelSerializer):
    class Meta:
        model = School

class SchoolListforUniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ('id','name','university')     

class UniversityListSerializer(serializers.ModelSerializer):
    # school = SchoolListSerializer()
    # school_count = serializers.SerializerMethodField()

    class Meta:
        model = University

    # def get_school_count(self,University):
    #     return School.objects.filter(University=university).count()



class UniversityWithSchoolsListSerializer(serializers.ModelSerializer):
    school_name = serializers.SerializerMethodField()

    class Meta:
        model = University
        fields = ('id','name','school_name')

    def get_school_name(self, obj):
        print obj.id
        return SchoolListforUniversitySerializer(School.objects.filter(university__id=obj.id),many=True).data
