from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(UserMaster)
class AdminUserMaster(admin.ModelAdmin):
    user_list_display = [
        field for field in UserMaster._meta.get_fields()]

@admin.register(CompanyMaster)
class AdminCompanyMaster(admin.ModelAdmin):
    user_list_display = [
        field for field in CompanyMaster._meta.get_fields()]
    
@admin.register(RoomMaster)
class AdminRoomMaster(admin.ModelAdmin):
    user_list_display = [
        field for field in RoomMaster._meta.get_fields()]
    
@admin.register(RoomDetail)
class AdminRoomDetail(admin.ModelAdmin):
    user_list_display = [
        field for field in RoomDetail._meta.get_fields()]
    
@admin.register(RoomContent)
class AdminRoomDetail(admin.ModelAdmin):
    user_list_display = [
        field for field in RoomContent._meta.get_fields()]
    
@admin.register(PayMaster)
class AdminPayMaster(admin.ModelAdmin):
    user_list_display = [
        field for field in PayMaster._meta.get_fields()]

@admin.register(PayDetail)
class AdminPayDetail(admin.ModelAdmin):
    user_list_display = [
        field for field in PayDetail._meta.get_fields()]