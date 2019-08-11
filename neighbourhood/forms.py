from django import forms
from .models import NeighbourHood,Post,Profile

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')


class NewNeighbourHoodForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        fields = ('neighbourhood_name', 'image', 'location', 'occupants')
        exclude = ['pub_date']


class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('post',)
        exclude = ['pub_date']


class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profession','status', 'image', 'contact', 'neighbourhood')
        exclude = ['pub_date']
        
        
class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=False)