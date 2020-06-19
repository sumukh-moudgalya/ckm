from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from basicapp.models import Explores,Hotels
app_name='basicapp'

# Create your views here.
class Baseview(TemplateView):
    template_name='html/basicapp/home_page.html'

class ExploresListView(ListView):
    model=Explores
    def get_queryset(self):
        return Explores.objects.all().order_by('rank')

class ExploresDetailView(DetailView):
    context_object_name='place_detail'
    model=Explores
    template_name='basicapp/explores_detail.html'


class HotelsListView(ListView):
    context_object_name='hotel_list'
    model=Hotels
    def get_queryset(self):
         return Hotels.objects.all().order_by('rank')


class HotelsDetailView(DetailView):
    context_object_name='hotel'
    model=Hotels
    template_name='basicapp/hotels_detail.html'
