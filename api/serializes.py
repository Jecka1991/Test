from rest_framework import serializers
from django.contrib.auth.models import User


from .models import Worker


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user


class WorkerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Worker
        fields = ('first_name', 'middle_name', 'last_name',
                  'position', 'worker_date', 'salary', 'salary_paid',
                  'big_boss_id', 'company_level')