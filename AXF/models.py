from django.db import models

# Create your models here.
class Base(models.Model):
    img=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    trackid=models.CharField(max_length=100)
    class Meta:
        abstract=True

#轮播图
class Wheel(Base):
    class Meta:
        db_table='axf_wheel'

#导航
class Nav(Base):
    class Meta:
        db_table='axf_nav'

#每日必购
class Mustbuy(Base):
    class Meta:
        db_table='axf_mustbuy'