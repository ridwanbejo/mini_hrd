from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

import os

# Create your models here.
class Divisi (models.Model):
	nama = models.CharField(max_length=100)
	keterangan =models.TextField(blank=True)

	def __unicode__(self):
		return self.nama

class Jabatan (models.Model):
	nama = models.CharField(max_length=100)
	keterangan = models.TextField(blank=True)

	def __unicode__(self):
		return self.nama

class Karyawan (models.Model):
	JENIS_KELAMIN_CHOICES = (
		('pria', 'Pria'),
		('wanita', 'Wanita'),
	)

	JENIS_KARYAWAN_CHOICES = (
		('magang', 'Magang'),
		('kontrak', 'Kontrak'),
		('tetap', 'Tetap'),
	)

	nama = models.CharField(max_length=100)
	alamat = models.TextField(blank=True)
	jenis_kelamin = models.CharField(max_length=10, choices=JENIS_KELAMIN_CHOICES)
	jenis_karyawan = models.CharField(max_length=10, choices=JENIS_KARYAWAN_CHOICES)
	no_telepon = models.CharField(max_length=30, blank=True)
	email = models.CharField(max_length=100, blank=True)
	no_rekening = models.CharField(max_length=100)
	pemilik_rekening = models.CharField(max_length=100)
	divisi = models.ForeignKey(Divisi)
	jabatan = models.ForeignKey(Jabatan)
	foto = models.ImageField(upload_to=os.path.join(settings.MEDIA_ROOT,"upload"), blank=True)

	def __unicode__(self):
		return self.nama

class Akun (models.Model):
	JENIS_AKUN_CHOICES = (
		('karyawan', 'Karyawan'),
		('admin', 'Administrator'),
	)

	akun = models.ForeignKey(User)
	karyawan = models.ForeignKey(Karyawan)
	jenis_akun = models.CharField(max_length=20, choices=JENIS_AKUN_CHOICES)

	def __unicode__(self):
		return self.karyawan.nama