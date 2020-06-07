from rest_framework_mongoengine import serializers
from django.contrib.auth import get_user_model
from mongoengine.queryset.visitor import Q
from django_mongoengine import fields
from django_mongoengine.mongo_auth.models import MongoUser

#User = get_user_model()

class UserCreateSerializer(serializers.DocumentSerializer):
    email2 = fields.EmailField(label='Confirm Email')
    class Meta:
        model=MongoUser
        fields = ('username','email','password')
        extra_kwargs={
                        "password":{"write_only": True}
        }

    def validate_email(self,value):
        data = self.get_initial()
        email1 = data.get("email")
        email2 = value
        if email1 != email2:
            raise ValidationError("Emails must match.")

        user_qs = MongoUser.objects.filter(email=email2)
        if user_qs:
            raise ValidationError("This user has already registered.")
        return value

    def create(self,validated_data):
        username = validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user_obj = MongoUser(
                username = username,
                email = email,
                password=password
        )
        #user_obj.set_password(password)
        user_obj.save()
        return validated_data


class UserLoginSerializer(serializers.DocumentSerializer):
    username = fields.StringField(max_length=50,blank=True)
    email = fields.EmailField(label="Email Address",blank=True)
    class Meta:
        model = MongoUser
        fields = ('username','email','password')
        extra_kwargs={
                        "password":{"write_only": True}
        }


    def validate_data(self,data):
        user_obj = None
        email = data.get("email",None)
        username = data.get("username",None)
        password = data["password"]
        if not email and not username:
            raise ValidationError("A Username or email is required to login.")

        user = MongoUser.objects.filter(
            Q(email=email) |
            Q(username=username)
        )
        if user and user.count() == 1:
            user_obj=user.first()
        else:
            raise ValidationError("This Username/Email is not valid!")

        if user_obj:
            if not user_obj.password==password:
                raise ValidationError("Incorrect credentials please try again.")
        return data
