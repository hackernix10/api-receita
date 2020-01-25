from django.shortcuts import render
from rest_framework import generics, filters
from .models import Cpf
from .serializers import CpfSerializer


class CpfList(generics.ListAPIView):
    serializer_class = CpfSerializer
    model= CpfSerializer.Meta.model
    paginate_by = 50

    def get_queryset(self):
        id = self.kwargs['NUM_CPF']
        queryset = self.model.objects.filter(NUM_CPF=id)
        return queryset
