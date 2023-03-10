from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MaxValueValidator
# from cal.models import Event
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.exceptions import ObjectDoesNotExist

class MyAccountManager(BaseUserManager):
	def create_user(self, email,first_name,last_name, password=None):
		if not email:
			raise ValueError('Users must have an email address')

		user = self.model(
			email=self.normalize_email(email),
			first_name = first_name,
			last_name = last_name,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email,first_name,last_name, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			first_name=first_name,
			last_name=last_name,
		)
		user.is_patient=False
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class Account(AbstractBaseUser):
	email 					= models.EmailField(verbose_name="email", max_length=60, unique=True)
	first_name				= models.CharField(max_length=20,blank=True)
	last_name 				= models.CharField(max_length=20,blank=True)
	date_joined				= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name='last login', auto_now=True)
	is_teacher			    = models.BooleanField(default=False)
	phone_number			= models.IntegerField(null=True , blank=True)
	location				= models.CharField(max_length=100, blank=True,null=True)
	is_admin				= models.BooleanField(default=False)
	is_active				= models.BooleanField(default=True)
	is_staff				= models.BooleanField(default=False)
	is_superuser			= models.BooleanField(default=False)


	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name','last_name']

	objects = MyAccountManager()

	def __str__(self):
		return self.email

	def full_name(self):
		return self.last_name+" "+self.first_name

	# For checking permissions. to keep it simple all admin have ALL permissons
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
	def has_module_perms(self, app_label):
		return True

# Create your models here.
