from django import forms
from alunos.models import CustomUser, Vinculacao
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

class UserLoginForm(AuthenticationForm):
      username = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'autofocus': True}))

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'cpf', 'nome']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError('Este email já está em uso.')
        return email

    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        if CustomUser.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError('Este CPF já está em uso.')
        return cpf




class MatriculaForm(forms.ModelForm):
    
    class Meta:
        model = Vinculacao
        fields = ['nome', 'cpf', 'email', 'dataNascimento', 'curso', 'foto', 'ingresso']
        widgets = {
            'dataNascimento': forms.DateInput(attrs={'type': 'date'}),
        }
    

    def clean(self):
        cleaned_data = super().clean()
        cpf = cleaned_data.get('cpf')
        
        if Vinculacao.objects.filter(cpf=cpf).exists():
            raise forms.ValidationError('CPF já cadastrado.')

        return cleaned_data
    

class SituacaoForm(forms.ModelForm):
    class Meta:
        model = Vinculacao
        fields = ['situacao']
      



      
    
