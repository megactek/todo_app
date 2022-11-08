from rest_framework.viewsets import ModelViewSet
from .serializer import TodoSerializer, Todo


class TodoView(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    