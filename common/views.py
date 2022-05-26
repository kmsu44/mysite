from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.shortcuts import render, redirect
from common.forms import UserForm
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from . forms import editInfoForm
from django.http import HttpResponse



def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('/pybo/')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})


def editinfo(request):
    if request.method == 'POST':
        form = editInfoForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/pybo')
    else:
        form = editInfoForm(instance=request.user)
        context = {'form': form}
        return render(request, 'common/editinfo.html', context)


def editpw(request):
    if request.method == 'POST':
        pwform = PasswordChangeForm(data=request.POST, user=request.user)
        if pwform.is_valid():
            pwform.save()
            return redirect('/pybo')
    else:
        pwform = PasswordChangeForm(user=request.user)
        context = {'form': pwform}
        return render(request, 'common/editpw.html', context)

