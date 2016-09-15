from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "intro.html")
    # return HttpResponse("Resultado de pruebas")


from rest_framework import viewsets, mixins
from serializers import GanttTasksSerializer, GanttLinksSerializer
from models import Gantt_links, Gantt_tasks


class GantTasksViewSet(viewsets.ModelViewSet):
    """
    ## Gantt Tasks
    Tareas de Gantt
    """
    queryset = Gantt_tasks.objects.all()
    serializer_class = GanttTasksSerializer
    ordering_fields = '__all__'


class GantLinksViewSet(viewsets.ModelViewSet):
    """
    ## Gantt Links
    Enlaces entre tareas de Gantt
    """
    queryset = Gantt_links.objects.all()
    serializer_class = GanttLinksSerializer
    ordering_fields = '__all__'