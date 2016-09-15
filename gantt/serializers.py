from models import Gantt_links, Gantt_tasks
from rest_framework import serializers


class GanttLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gantt_links


class GanttTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gantt_tasks