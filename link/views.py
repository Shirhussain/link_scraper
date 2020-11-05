from django.shortcuts import render, HttpResponseRedirect
from bs4 import BeautifulSoup
import requests 

from . models import  Link


def scrape(request):
    if request.method == 'POST':
        site = request.POST.get('site')
        page = requests.get(site)
        soup = BeautifulSoup(page.text,'html.parser')


        for link in soup.find_all('a'):
            link_address = link.get('href')
            link_text = link.string
            Link.objects.create(name =link_text, address= link_address)
        return HttpResponseRedirect('/')
    else:
        data = Link.objects.all()

    context = {
        'data': data
    }
    return render(request, "link/scrape.html", context)



def clear(request):
    Link.objects.all().delete()
    return render(request,"link/scrape.html")