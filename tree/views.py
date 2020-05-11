from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404

from tree.models import Tree
from tree.serializers import TreeSerializer

class TreeList(APIView):
    """
    List all trees
    """
    def get(self, request, format=None):
        trees = Tree.objects.filter(level=0)
        serializer = TreeSerializer(trees, many=True)
        return Response(serializer.data)

class TreeDetail(APIView):
    """
    Retrieve a tree instance.
    """
    def get_object(self, pk):
        try:
            return Tree.objects.get(pk=pk)
        except Tree.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        tree = self.get_object(pk)
        serializer = TreeSerializer(tree)
        return Response(serializer.data)