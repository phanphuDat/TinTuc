from django.db import models


# Create your models here.
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    ten = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    photo = models.FileField(null=True)
    noidung = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.ten


# class Post(models.Model):
#     post_id = models.AutoField(primary_key=True)
#     ten = models.TextField(blank=True, null=True)
#     link = models.TextField(blank=True, null=True)
#     photo = models.FileField(null=True)
#     noidung = models.TextField(blank=True, null=True)
#
#     def __str__(self):
#         return self.ten


class KhachHang(models.Model):
    KH_id = models.AutoField(primary_key=True)
    email = models.TextField(blank=True, null=True)
    tenDayDu = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.tenDayDu
