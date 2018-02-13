from django.contrib import admin
from school_mgmt.models import *
# Register your models here.


class UniversityAdmin(admin.ModelAdmin):
    fieldsets = (
           ('University data', {'fields': ('name', 'logo', 'website')}),
           ('Date', {'fields': ('created_at','modified_at')}),
	        ('Permission', {'fields': ('is_active', )}),
    	)

class SchoolAdmin(admin.ModelAdmin):
    fieldsets=(
        ('School data',{'fields':('owner','university','name','logo','website')}),
        ('Date',{'fields':('created_at','modified_at')}),
        ('Permission', {'fields': ('is_active', )}),
    )

class AddressAdmin(admin.ModelAdmin):
    fieldsets=(
        ('School data',{'fields':('street_1','street_2','city','state','country','zip_code','mobile_no')}),
    )

class StudentAdmin(admin.ModelAdmin):
    fieldsets=(
        ('School data',{'fields':('school','first_name','last_name','roll_no','email','date_of_birth','address')}),
        ('Date',{'fields':('created_at','modified_at')}),
        ('Permission', {'fields': ('is_active', )}),
    )

admin.site.register(University,UniversityAdmin)
admin.site.register(School,SchoolAdmin)
admin.site.register(Address,AddressAdmin)
admin.site.register(Student,StudentAdmin)

