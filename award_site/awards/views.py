from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets
from rest_framework import permissions, generics

import re

from .models import Award
from .serializers import AwardSerializer


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
        context['linked_awards'] = Award.objects.filter(name=context['award'].name).exclude(pk=context['award'].pk)
        return context


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def api_awards(request):
    if request.method == 'GET':
        try:
            query = request.GET.get('q', '')
            if query:
                results = Award.objects.filter(name__icontains=query)
                serializer = AwardSerializer(results, many=True)
                return Response(serializer.data)
            else:
                results = Award.objects.all()
                serializer = AwardSerializer(results, many=True)
                return Response(serializer.data)
        except AttributeError:
            results = Award.objects.all()
            serializer = AwardSerializer(results, many=True)
            return Response(serializer.data)


class AwardsDetailAPIView(generics.RetrieveAPIView):
    queryset = Award.objects.all()
    serializer_class = AwardSerializer

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset.get(pk=self.request.query_params.get('id'))
        return obj


