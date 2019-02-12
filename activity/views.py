from django.views import generic

from .models import Direction


class ListView(generic.ListView):
    model = Direction
    template_name = 'activity/directions_list.html'
    context_object_name = 'directions'


class DetailView(generic.DetailView):
    model = Direction
    template_name = 'activity/direction_detail.html'
