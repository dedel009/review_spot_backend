from django.contrib import admin

import user.models


# Register your models here.


# 사용자 모델
class CustomUser(admin.ModelAdmin):
    # 관리자 페이지에서 사용자 목록에 표시할 필드를 정의
    list_display = ('id', 'username', 'name', 'email', 'is_active', 'is_staff', 'date_joined')
    list_filter = ('is_staff',)
    search_fields = ('username', 'name')
    ordering = ('username',)

    # 사용자 저장 시 비밀번호 해싱
    def save_model(self, request, obj, form, change):
        if form.cleaned_data.get('password'):
            # 비밀번호가 변경되었을 때만 비밀번호 해싱
            obj.set_password(form.cleaned_data['password'])
        super().save_model(request, obj, form, change)


# 관리자 모델
class CustomAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)


admin.site.register(user.models.CustomUser, CustomUser)
admin.site.register(user.models.CustomAdmin, CustomAdmin)
