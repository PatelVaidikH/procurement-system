from django.db import models
import datetime

# Create your models here. 

class CompanyMaster(models.Model):
    company_name = models.CharField(max_length=122, null=False)
    company_desc = models.CharField(max_length=255)
    class Meta:
        db_table = 'company_master'

class UserMaster(models.Model):
    USER_TYPE = [
        ('0',"Super Admin"),
        ('1',"Admin"),
        ('2',"Staff"),
        ('3',"Client"),
    ]
    user_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=122, unique=True, null=False,default="")
    password = models.CharField(max_length=100,default="")
    username = models.CharField(max_length=50,default="")
    user_full_name = models.CharField(max_length=122,default="")
    contact_number = models.CharField(null=True,max_length=10)
    company_id = models.CharField(max_length=5,null=True,blank=True)
    user_type = models.CharField(max_length=2,default=3,choices=USER_TYPE)
    company_name = models.CharField(max_length=122, null=True,blank=True)
    token = models.CharField(max_length=100,null=True,blank=True)
    class Meta:
        db_table = 'user_master'

class RoomMaster(models.Model):
    chat_room_id = models.AutoField(primary_key=True)
    chat_room_name = models.CharField(max_length=200, null=False)
    date_creation = models.DateTimeField(auto_now=True,null=False)
    last_message = models.CharField(max_length=255,null=True,blank=True)
    date_deletion = models.DateField(null=True)
    class Meta:
        db_table = 'chat_room_master'

class RoomDetail(models.Model):
    chat_room_id = models.ForeignKey(RoomMaster, on_delete=models.CASCADE,default=1)
    user_id = models.ForeignKey(UserMaster, on_delete=models.CASCADE,default=1)
    class Meta:
        db_table = 'chat_room_detail'

class PayMaster(models.Model):
    chat_room_id = models.IntegerField(null=False)
    payment_date = models.DateField(null=False)
    transaction_id = models.CharField(max_length=99)
    sender_user_id = models.IntegerField(null=False)
    amount = models.IntegerField(null=False)
    mode_of_payment = models.CharField(max_length=30)
    class Meta:
        db_table = 'payment_sheet'

class RoomContent(models.Model):
    chat_room_id = models.ForeignKey(RoomMaster, on_delete=models.RESTRICT,default=1)
    sender_id = models.ForeignKey(UserMaster, on_delete=models.RESTRICT,default=1)
    username = models.CharField(max_length=50,default="")
    message = models.CharField(max_length=1000,null=True)
    timestamp = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'chat_room_content'

class PayDetail(models.Model):
    ifsc = models.CharField(max_length=15,unique=True, null=False,default="")
    acc_num = models.CharField(max_length=20,unique=True, null=False,default="")
    acc_name = models.CharField(max_length=255,null=False, default="")
    bank_name = models.CharField(max_length=255,null=False, default="")
    branch_name = models.CharField(max_length=255,null=False, default="")
    user_id = models.ForeignKey(UserMaster, on_delete=models.RESTRICT,default="1")
    c_id = models.ForeignKey(CompanyMaster, on_delete=models.RESTRICT,default="1")
    qr = models.ImageField(upload_to='',max_length=255,null=True,blank=True)
    class Meta:
        db_table = 'payment_details'