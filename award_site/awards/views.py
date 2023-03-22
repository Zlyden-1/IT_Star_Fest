from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
import re

from .models import Award


class IndexView(generic.ListView):
    template_name = 'awards/index.html'
    context_object_name = 'award_list'

    def get_queryset(self):
        award_list = Award.objects.all()
        return award_list


def search(request):
    query = request.GET.get('q', '')
    if query:
        results = Award.objects.filter(name__icontains=query)
    else:
        results = Award.objects.none()

    context = {'results': results, 'query': query}
    return render(request, 'awards/search.html', context)


class AwardVew(generic.DetailView):
    model = Award
    template_name = 'awards/award.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['linked_awards'] = Award.objects.filter(name=context['award'].name)
        return context
