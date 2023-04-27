from django.views.generic import TemplateView, ListView
from .models import Thing

class HomePageView(ListView):
    template_name = "pages/home.html"
    model = Thing
    context_object_name = 'things'


class AboutPageView(TemplateView):
    template_name = "pages/about.html"
