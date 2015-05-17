#coding=utf-8
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.template.context import RequestContext
from AutoTest.form import LoginForm, ChangepwdForm


def Index(request):
	return render_to_response("index.html")

def TestCase(request):
	return render_to_response("testcase.html")

#登录
from django.contrib.auth import authenticate, login

def LoginView(request):
	if request.method == 'GET':
		form = LoginForm()
		return render_to_response('login.html', RequestContext(request, {'form': form,}))
	else:
		form = LoginForm(request.POST)
		if form.is_valid():
			username = request.POST.get('username', '')
			password = request.POST.get('password', '')
			user = auth.authenticate(username=username, password=password)
			if user is not None and user.is_active:
				auth.login(request, user)
				return render_to_response('index.html', RequestContext(request,{'username':username}))
			else:
				return render_to_response('login.html', RequestContext(request, {'postform': form,'password_is_wrong':True}))
		else:
			return render_to_response('login.html', RequestContext(request, {'form': form,}))

#登出
@login_required
def LogoutView(request):
	auth.logout(request)
	return HttpResponseRedirect("/logout/")


def ChangepwdView(request):
	if request.method == 'GET':
		form = ChangepwdForm()
		return render_to_response('reset-password.html', RequestContext(request, {'form': form,}))
	else:
		form = ChangepwdForm(request.POST)
		if form.is_valid():
			username = request.user.username
			oldpassword = request.POST.get('oldpassword', '')
			user = auth.authenticate(username=username, password=oldpassword)
			if user is not None and user.is_active:
				newpassword = request.POST.get('newpassword1', '')
				user.set_password(newpassword)
				user.save()
				return render_to_response('index.html', RequestContext(request,{'changepwd_success':True}))
			else:
				return render_to_response('reset-password.html', RequestContext(request, {'form': form,'oldpassword_is_wrong':True}))
		else:
			return render_to_response('reset-password.html', RequestContext(request, {'form': form,}))