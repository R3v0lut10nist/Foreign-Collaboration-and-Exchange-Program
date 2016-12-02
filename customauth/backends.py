from .models import MyUser
class Backend(object):
	def authenticate(self,email=None,password=None):
		try:
			user=MyUser.objects.get(email=email)
		except MyUser.DoesNotExist:
			return None
		validate=user.check_password(password)
		if(validate is not None):
			return user
		else:
			return None

	def get_user(self,email):
		try:
			return MyUser.objects.get(email=email)
		except MyUser.DoesNotExist:
			return None