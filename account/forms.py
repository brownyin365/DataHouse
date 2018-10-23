from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User



#Form extension to the signup page
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    # def save(self, commit=True):
    # 	user = super(SignUpForm, self).save(commit=False)
    # 	user.email = self.cleaned_data['email']

    # 	if commit:
    # 		user.save()

    # 	return user	

#Form extension to the edit profile page
class EditProfileForm(UserChangeForm):

	
	class Meta:
		model = User
		fields = ('email', 'first_name', 'last_name', 'password')
		# exclude = ('username','password',)    

