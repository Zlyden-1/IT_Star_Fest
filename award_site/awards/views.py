from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Award


class IndexView(generic.ListView):
    template_name = 'awards/index.html'
    context_object_name = 'award_list'

    def get_queryset(self):
        items_in_row = 4
        award_list = Award.objects.all()
        return [award_list[i:i + items_in_row] for i in range(0, len(award_list), items_in_row)]
