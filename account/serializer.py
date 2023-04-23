from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import Ad


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'is_superuser', 'date_joined', 'last_login', 'is_staff')
        
class UserActivateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('is_active',)
        
class AdSerializer(serializers.ModelSerializer):
    text = serializers.CharField()
    link = serializers.CharField(allow_null=True, default='')
    link_text = serializers.CharField(allow_null=True, default='')
    date_added = serializers.DateTimeField(format="%d.%m.%Y %H:%M:%S", required=False, read_only=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        for field in ['link', 'link_text']:
            if data[field] is None:
                data[field] = ''
        return data
        
    class Meta:
        model = Ad
        fields = ['text', 'link', 'link_text', 'date_added']
        
        


class UserRegistrSerializer(serializers.ModelSerializer):
    # Поле для повторения пароля
    # password2 = serializers.CharField()
    
    # Настройка полей
    class Meta:
        # Поля модели которые будем использовать
        model = User
        # Назначаем поля которые будем использовать
        fields = ['email', 'username', 'password', 'nickname', 'server', 'first_name', 'last_name', 'social_network']
        # fields = '__all__'
 
    # Метод для сохранения нового пользователя
    def save(self, *args, **kwargs):
        # Создаём объект класса User
        user = User(
            email = self.validated_data['email'], # Назначаем Email
            username = self.validated_data['username'], # Назначаем Логин
            nickname = self.validated_data['nickname'],
            server = self.validated_data['server'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
            social_network = self.validated_data['social_network'],
            is_active = False
        )
        # Проверяем на валидность пароль
        password = self.validated_data['password']
        # Сохраняем пароль
        user.set_password(password)
        # Сохраняем пользователя
        user.save()
        # Возвращаем нового пользователя 
        return user

