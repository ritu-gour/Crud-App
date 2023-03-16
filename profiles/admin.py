from django.contrib import admin
from profiles.models import Profile
class ProfileAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','password1','password2')

admin.site.register(Profile,ProfileAdmin)   