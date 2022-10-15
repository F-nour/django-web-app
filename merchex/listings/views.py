from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Listings


def index(request):
    return render(request, 'index.html')


def band(request):
    bands = Band.objects.all()
    return render(request, 'bands/bands_list.html', {'bands': bands})


def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    return render(request,
                  'bands/band_detail.html',
                  {
                      'id': band_id,
                      'band': band,
                   })


def listings(request):
    listings = Listings.objects.all()
    return render(request, 'listings/listings_list.html', {'listings': listings})


def listing_detail(request, listing_id):
    listing = Listings.objects.get(id=listing_id)
    return render(request,
                  'listings/listing_details.html',
                  {
                      'id': listing_id,
                      'listing': listing,
                  })

def about(request):
    return HttpResponse('<h1>About my first Django app!</h1>')
