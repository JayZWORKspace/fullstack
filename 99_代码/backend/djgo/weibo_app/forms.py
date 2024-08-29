from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        # 第二个密码是用于覆盖第一个密码的
        fields = ('email', 'name','password1','password2')