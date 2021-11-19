
from datetime import datetime
from django.db import models

# Create your models here.

class TbUserInfo(models.Model):
    user_id = models.CharField(primary_key=True, max_length=60)
    user_pwd = models.CharField(max_length=60)
    user_name = models.CharField(max_length=20)
    user_email = models.CharField(max_length=100)
    user_phone = models.CharField(max_length=20)
    user_join_date = models.DateTimeField(default=datetime.now,blank=True)

    class Meta:
        managed = False
        db_table = 'tb_user_info'
    
    def __str__(self):
        return self.user_id

    def as_dict(self):
        return {'user_id':self.user_id}    
        