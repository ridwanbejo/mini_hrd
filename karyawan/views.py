from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings

from karyawan.models import Karyawan
# Create your views here.

@login_required(login_url=settings.LOGIN_URL)
def profil(request):
	karyawan = Karyawan.objects.get(id=request.session['karyawan_id'])
	return render(request, 'new/profil.html', {"karyawan":karyawan})

@login_required(login_url=settings.LOGIN_URL)
def ganti_foto(request):
	karyawan = Karyawan.objects.get(id=request.session['karyawan_id'])
	karyawan.foto = request.FILES['files']
	karyawan.save()
	
	return redirect('/')
