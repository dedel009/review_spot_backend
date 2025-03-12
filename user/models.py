import uuid

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models


# Create your models here.


# 유저 모델을 관리하는 커스텀 매니저 클래스
class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        """
        일반 유저 생성 메소드
        """
        if not username:
            raise ValueError('아이디를 입력해주세요.')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


# 커스텀 유저 모델
class CustomUser(AbstractBaseUser):
    """
    리뷰 스팟 서비스에서 사용할 유저 및 관리자(장고 어드민 X) 계정 모델
    """
    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='유저 아이디',
    )
    name = models.CharField(
        max_length=30,
        null=False,
        verbose_name='유저 이름',
    )
    nickname = models.CharField(
        max_length=30,
        blank=True,
        verbose_name='유저 닉네임',
        null=True,
    )
    email = models.EmailField(
        blank=True,
        verbose_name='유저 이메일',
        null=True,
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name='유저 사용 유무',
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name='유저 관리자 유무',
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
        verbose_name='생성 일자',
    )

    # Django의 ORM(Object-Relational Mapping)에서 모델 매니저를 지정
    objects = CustomUserManager()

    USERNAME_FIELD = 'username'  # 로그인 시 사용할 필드
    REQUIRED_FIELDS = []  # create_superuser에 필요한 추가 필드

    class Meta:
        db_table = 'user_user'
        verbose_name_plural = '유저 및 관리자 계정'


# 장고 어드민 계정을 관리하는 매니저
class CustomAdminManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('사용자 이름은 필수 항목입니다.')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(username, password, **extra_fields)


# 장고 어드민 계정 모델
class CustomAdmin(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='유저 아이디',
    )
    first_name = models.CharField(max_length=30, blank=True, verbose_name='성')
    last_name = models.CharField(max_length=30, blank=True, verbose_name='이름')
    email = models.EmailField(unique=True, blank=True, verbose_name='이메일')
    is_staff = models.BooleanField(default=True, verbose_name='관리자 유무')
    date_joined = models.DateTimeField(
        auto_now_add=True,
        verbose_name='생성 일자',
    )

    objects = CustomAdminManager()

    USERNAME_FIELD = 'username'  # 로그인 시 사용할 필드
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']  # create_superuser에 필요한 추가 필드

    class Meta:
        db_table = 'user_django_admin'
        verbose_name_plural = '장고 어드민 계정'
