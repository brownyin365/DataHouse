from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.core.files.storage import FileSystemStorage




from account.forms import SignUpForm, EditProfileForm

# Create your views here.

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sendText:index')
    else:
        form = SignUpForm()
    return render(request, 'account/signup.html', {'form': form})

def login_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			#Log in the User
			user = form.get_user()
			login(request, user)
			return redirect('sendText:select')
	else:
		form = AuthenticationForm()	
	return render(request, 'account/login.html', {'form':form})


def logout_view(request):
	if request.method == 'POST':
		logout(request)
		return redirect('sendText:index')
	

def profile_view(request):
	args = {'user': request.user}
	return render(request, 'account/profile.html', args)


def edit_profile(request):
	if request.method =='POST':
		form = EditProfileForm(request.POST, request.FILES, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('account:edit_profile')

	else:
		form = EditProfileForm(instance=request.user)
		args = {'form':form}
		return render(request, 'account/edit_profile.html', args)			

def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('account:profile')
		else:
			return redirect('account:change-password')	

	else:
		form = PasswordChangeForm(user=request.user)
		args = {'form':form}
		return render(request, 'account/change_password.html', args)		


# def simple_upload(request):
#     if request.method == 'POST' and request.FILES['myfile']:
#         myfile = request.FILES['myfile']
#         fs = FileSystemStorage()
#         filename = fs.save(myfile.name, myfile)
#         uploaded_file_url = fs.url(filename)
#         return render(request, 'account/simple_upload.html', {
#             'uploaded_file_url': uploaded_file_url
#         })
#     return render(request, 'account/simple_upload.html')
