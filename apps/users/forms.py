from django.contrib.auth.forms import UserCreationForm
from . models import User, UserType
from django import forms


class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Номер телефона')
    photo = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}), required=False, label='Фото')
    user_type = forms.ChoiceField(choices=UserType.choices,
                                  widget=forms.Select(attrs={'class': 'form-control'}),
                                  label='Тип пользователя')
    tg_username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label='Юзернейм из тг')

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'phone_number',
            'photo',
            'user_type',
            'tg_username',
        )


