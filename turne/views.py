from rest_framework import viewsets, generics
from turne.models import Cantor, Pais, Turne
from turne.serializer import CantorSerializer, PaisSerializer, TurneSerializer, TurneCantorSerializer, TurnesPaisSerializer
from rest_framework.authentication import BasicAuthentication #autenticar quem consome api
from rest_framework.permissions import IsAuthenticated #garantir que está autenticado


class CantorViewSet(viewsets.ModelViewSet): #já temos modelo vinculado, por isso usar o ModelViewSet
    queryset = Cantor.objects.all()
    serializer_class = CantorSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class PaisViewSet(viewsets.ModelViewSet):
    """Exibindo todos os paises"""
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class TurneViewSet(viewsets.ModelViewSet):
    """Exibindo todas as turnes cadastradas:"""
    queryset = Turne.objects.all()
    serializer_class = TurneSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListaTurnesCantorViewSet(generics.ListAPIView):
    """Listando as turnes do cantor:"""
    def get_queryset(self): #temos que achar a id do cantor que veremos
        queryset = Turne.objects.filter(cantor_id=self.kwargs['pk'])
        return queryset
    serializer_class = TurneCantorSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class TurnesPaisViewSet(generics.ListAPIView):
    """Listando as turnes que ocorrerão no pais:"""
    def get_queryset(self):
        queryset = Turne.objects.filter(pais_id=self.kwargs['pk'])
        return queryset
    serializer_class = TurnesPaisSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]