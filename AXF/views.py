from django.shortcuts import render

# Create your views here.
from AXF.models import Wheel, Nav, Mustbuy, Shop, Mainshow, Foodtypes, Goods


def home(request):
    wheels = Wheel.objects.all()
    navs = Nav.objects.all()
    mustbuys = Mustbuy.objects.all()
    shoplist = Shop.objects.all()
    shophead = shoplist[0]
    shoptabs = shoplist[1:3]
    shopclasses = shoplist[3:7]
    shopcommands = shoplist[7:]
    mainshows=Mainshow.objects.all()

    data = {'wheels': wheels,
            'navs': navs,
            'mustbuys': mustbuys,
            'shophead': shophead,
            'shoptabs': shoptabs,
            'shopclasses': shopclasses,
            'shopcommands': shopcommands,
            'mainshows':mainshows

            }

    return render(request, 'home/home.html', context=data)


def market(request,categoryid):
    foodtypes=Foodtypes.objects.all()
    typeIndex=int(request.COOKIES.get('typeIndex',0))
    categoryid=foodtypes[typeIndex].typeid
    goodlists=Goods.objects.filter(categoryid=categoryid)
    data={
        'foodtypes':foodtypes,
        'goodlists':goodlists
    }
    return render(request, 'market/market.html',context=data)


def cart(request):
    return render(request, 'cart/cart.html')


def mine(request):
    return render(request, 'mine/mine.html')


def registe(request):
    if request.method=='GET':
        pass
    elif request.method=='POST':
        pass

