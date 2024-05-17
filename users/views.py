from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from building.models import House
from .models import Testimonials


class LandingPageView(View):
    def get(self, request):
        return render(request, 'main/index.html')


class ContactListView(View):
    def get(self, request):
        return render(request, 'main/contact.html')


class PropertyListView(View):
    def get(self, request):
        return render(request, 'main/property-grid.html')


class BlogListView(View):
    def get(self, request):
        return render(request, 'main/blog-grid.html')


class AboutListView(View):
    def get(self, request):
        return render(request, 'main/about.html')


class TestimonialView(View):
    def get(self, request):
        testimonials = Testimonials.objects.all()
        context = {
            'testimonials': testimonials
        }
        return render(request, 'main/testimonial.html', context)
