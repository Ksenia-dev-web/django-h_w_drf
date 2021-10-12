from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    context = dict()

    if request.GET.get('sort'):
        sort = request.GET.get('sort')
        if sort == 'name':
            context['phones'] = Phone.objects.all().order_by('name')
        elif sort == 'price_from_min_to_max':
            context['phones'] = Phone.objects.all().order_by('price')
        elif sort == 'price_from_max_to_min':
            context['phones'] = Phone.objects.all().order_by('-price')
        else:
            context['phones'] = Phone.objects.all()
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    product = Phone.objects.all().filter(slug=slug)
    context = {'product': product}
    return render(request, template, context)