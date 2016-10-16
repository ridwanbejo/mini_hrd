from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages

from karyawan.models import Akun, Karyawan
# Create your views here.

def login_view(request):
	if request.POST:
		user = authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			if user.is_active:
				try:
					akun = Akun.objects.get(akun=user.id)
					login(request, user)
					
					request.session['karyawan_id'] = akun.karyawan.id
					request.session['jenis_akun'] = akun.jenis_akun
					request.session['username'] = request.POST['username']
				except:
					messages.add_message(request, messages.INFO, 'Akun ini belum terhubung dengan data karyawan, silahkan hubungi administrator')
				return redirect('/')
			else:	
				messages.add_message(request, messages.INFO, 'User belum terverifikasi')
		else:
			messages.add_message(request, messages.INFO, 'Username atau password Anda salah')

	return render(request, 'new/login.html')

def logout_view(request):
	logout(request)
	return redirect('/login/')