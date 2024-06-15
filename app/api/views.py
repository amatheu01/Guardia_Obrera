from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import action

from .models import *
from .serializers import *


# Create your views here.
class HasViewPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('view_module')


class BaseModelViewSet(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class Planificacion_ViewSet(BaseModelViewSet):
    queryset = TbDplanificacion.objects.all()
    serializer_class = Planificacion_Serializer
    search_fields = ['nombre_planificacion']
    permission_classes = [IsAuthenticated, HasViewPermission]

    @action(detail=False, methods=['get'])
    def get(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return Response({'detail': 'Authentication required.'}, status=status.HTTP_401_UNAUTHORIZED)

        if not user.has_perm('view_module'):
            return Response({'detail': 'Permission denied.'}, status=status.HTTP_403_FORBIDDEN)

        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RegionGuardia_ViewSet(BaseModelViewSet):
    queryset = TbDregionGuardia.objects.all()
    serializer_class = RegionGuardia_Serializer
    search_fields = ['nombre_region_guardia', 'id_planificador', 'id_responsable']


class Posta_ViewSet(BaseModelViewSet):
    queryset = TbDposta.objects.all()
    serializer_class = Posta_Serializer
    search_fields = ['nombre_posta']


class GrupoGuardia_ViewSet(BaseModelViewSet):
    queryset = TbDgrupoGuardia.objects.all()
    serializer_class = GrupoGuardia_Serializer
    search_fields = ['nombre_grupo_guardia']


class TipoIncidencia_ViewSet(BaseModelViewSet):
    queryset = TbNtipoIncidencia.objects.all()
    serializer_class = TipoIncidencia_Serializer
    search_fields = ['nombre_tipo_incidencia']


class Variable_ViewSet(BaseModelViewSet):
    queryset = TbDvariable.objects.all()
    serializer_class = Variable_Serializer
    search_fields = ['nombre_variable']


class Horario_ViewSet(BaseModelViewSet):
    queryset = TbNhorario.objects.all()
    serializer_class = Horario_Serializer
    search_fields = ['nombre_horario']


class Turnos_ViewSet(BaseModelViewSet):
    queryset = TbRregionHorarioTurno.objects.all()
    serializer_class = Turno_Serializer
    search_fields = ['turnos']


class Patrones_ViewSet(BaseModelViewSet):
    queryset = TbDpatron.objects.all()
    serializer_class = Patron_Serializer
    search_fields = ['nombre']


class Asistencia_ViewSet(BaseModelViewSet):
    queryset = TbDasistencia.objects.all()
    serializer_class = Asistencia_Serializer


class Incidencia_ViewSet(BaseModelViewSet):
    queryset = TbDincidencia.objects.all()
    serializer_class = Incidencia_Serializer