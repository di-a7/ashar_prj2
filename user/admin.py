from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as UA
# Register your models here.
class UserAdmin(UA):
   fieldsets = (
         (None, {"fields": ("username", "password")}),
         (("Personal info"), {"fields": ("first_name", "last_name", "email","phone")}),
         (
            ("Permissions"),
            {
                  "fields": (
                     "is_active",
                     "is_staff",
                     "is_superuser",
                     "groups",
                     "user_permissions",
                  ),
            },
         ),
         (("Important dates"), {"fields": ("last_login", "date_joined")}),
      )
   list_display = ('id', 'username', 'email', 'is_staff', 'is_active')
   search_fields = ('username', 'email')
   list_filter = ('is_staff', 'is_active')
   
admin.site.register(User, UserAdmin)