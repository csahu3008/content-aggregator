from django.contrib.auth.backends import ModelBackend
from django.conf import settings
from .models import MyUser
class CustomBackend:
    def authenticate(self,request,**kwargs):
        try:
            mobile=kwargs['mobile']
            email=kwargs['email']
            password=kwargs['password']
            if mobile and password is not None:
                user=MyUser.objects.get(mobile=mobile)
                if user is not None:
                    user.check_password(password)
                    return user
            else:
                if email and password is not None:
                    user=MyUser.objects.get(email=email)
                    if user is not None:
                        user.check_password(password)
                        return user
                    else:
                        return None
            return user
        except MyUser.DoesNotExist:
                mobile=kwargs['mobile']
                if mobile is not None:
                    user=MyUser(mobile=mobile)
                    user.set_password(password)
                    user.save()
                    print('your account has been successfully created')
                    return user
                else:
                    print('you have not provided us any email')
                    return None

    def get_user(self,user_id):
        try:
            user=MyUser.objects.get(pk=user_id)
            return user
        except MyUser.DoesNotExist:
            return None