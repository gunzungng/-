from django.db import models


# Create your models here.
class Base(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=100)

    class Meta:
        abstract = True


# 轮播图
class Wheel(Base):
    class Meta:
        db_table = 'axf_wheel'


# 导航
class Nav(Base):
    class Meta:
        db_table = 'axf_nav'


# 每日必购
class Mustbuy(Base):
    class Meta:
        db_table = 'axf_mustbuy'


# 商品部分
class Shop(Base):
    class Meta:
        db_table = 'axf_shop'


# 主体
# insert into axf_mainshow(trackid,name,img,categoryid,brandname,img1,
# childcid1,productid1,longname1,price1,marketprice1,img2,childcid2,
# productid2,longname2,price2,marketprice2,img3,childcid3,productid3,
# longname3,price3,marketprice3)
#
#  values("21782","优选水果","http://img01.bqstatic.com//upload/activity/2017031018205492.jpg@90Q.jpg",
# "103532","爱鲜蜂","http://img01.bqstatic.com/upload/goods/201/701/1916/20170119164159_996462.jpg@200w_200h_90Q",
# "103533","118824","爱鲜蜂·特小凤西瓜1.5-2.5kg/粒","25.80","25.8","http://img01.bqstatic.com/upload/goods/201/611/1617/20161116173544_219028.jpg@200w_200h_90Q",
# "103534","116950","蜂觅·越南直采红心火龙果350-450g/盒","15.3","15.8","http://img01.bqstatic.com/upload/goods/201/701/1916/20170119164119_550363.jpg@200w_200h_90Q",
# "103533","118826","爱鲜蜂·海南千禧果400-450g/盒","9.9","13.8");

class Mainshow(models.Model):
    trackid = models.CharField(max_length=8)
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    categoryid = models.CharField(max_length=8)
    brandname = models.CharField(max_length=100)
    img1 = models.CharField(max_length=100)
    childcid1 = models.CharField(max_length=8)
    productid1 = models.CharField(max_length=8)
    longname1 = models.CharField(max_length=100)
    price1 = models.FloatField()
    marketprice1 = models.FloatField()

    img2 = models.CharField(max_length=100)
    childcid2 = models.CharField(max_length=8)
    productid2 = models.CharField(max_length=8)
    longname2 = models.CharField(max_length=100)
    price2 = models.FloatField()
    marketprice2 = models.FloatField()

    img3 = models.CharField(max_length=100)
    childcid3 = models.CharField(max_length=8)
    productid3 = models.CharField(max_length=8)
    longname3 = models.CharField(max_length=100)
    price3 = models.FloatField()
    marketprice3 = models.FloatField()
    class Meta:
        db_table='axf_mainshow'

class Foodtypes(models.Model):

    typeid = models.CharField(max_length=8)
    typename = models.CharField(max_length=100)
    childtypenames = models.CharField(max_length=200)
    typesort = models.CharField(max_length=100)
    class Meta:
        db_table='axf_foodtypes'

# axf_goods(productid,productimg,productname,productlongname,isxf,pmdesc,specifics,price,marketprice,categoryid,childcid,childcidname,dealerid,storenums,productnum) values("11951","http://img01.bqstatic.com/upload/goods/000/001/1951/0000011951_63930.jpg@200w_200h_90Q","","乐吧薯片鲜虾味50.0g",0,0,"50g",2.00,2.500000,103541,103543,"膨化食品","4858",200,4);
class Goods(models.Model):
    productid=models.CharField(max_length=10)
    productimg=models.CharField(max_length=100)
    productname=models.CharField(max_length=100)
    productlongname=models.CharField(max_length=100)
    isxf=models.BooleanField(default=False)
    pmdesc=models.BooleanField(default=False)
    specifics=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    marketprice=models.DecimalField(max_digits=8,decimal_places=2)
    categoryid=models.IntegerField()
    childcid=models.IntegerField()
    childcidname=models.CharField( max_length=100 )
    dealerid=models.CharField(max_length=100   )
    storenums=models.IntegerField()
    productnum=models.IntegerField()

    class Meta:
        db_table='axf_goods'

class User(models.Model):
    account=models.CharField(max_length=100,unique=True)
    password=models.CharField(max_length=256)
    name=models.CharField(max_length=100,unique=True)
    phone=models.CharField(max_length=20,unique=True)
    addr=models.CharField(max_length=256)
    img=models.CharField(max_length=100)
    rank=models.IntegerField(default=1)
    token=models.CharField(max_length=256)
    class Meta:
        db_table='axf_user'
