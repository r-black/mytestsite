from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from tree.models import Tree

class TreeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    children = serializers.ListField(read_only=True, source='get_children', child=RecursiveField())