from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField, ValidationError


class RegistrationSerializer(ModelSerializer):
    re_password = CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 're_password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            },
        }

    def save(self):
        password = self.validated_data['password']
        re_password = self.validated_data['re_password']
        if password != re_password:
            raise ValidationError({'error': 'password mismatch!'})

        if User.objects.filter(email=self.validated_data['email']).exists():
            raise ValidationError({'error': 'email already exists!'})

        user = User(email=self.validated_data['email'], username=self.validated_data['username'])
        user.set_password(password)
        user.save()
        return user
