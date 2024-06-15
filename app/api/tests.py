from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import TbDplanificacion


# Create your tests here.
class TbDplanificacionTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = 'api/planificacion/'

    def test_crear_planificacion(self):
        data = {'id_planificacion': '100', 'nombre_planificacion': 'Prueba', 'fecha_inicio': '2024-06-08', 'fecha_fin': '2024-06-09', 'id_region_guardia': '100'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TbDplanificacion.objects.count(), 1)
        self.assertEqual(TbDplanificacion.objects.get().nombre_planificacion, 'Prueba')

    def test_listar_planificaciones(self):
        TbDplanificacion.objects.create(id_planificacion='100', nombre_planificacion='Prueba', fecha_inicio='2024', fecha_fin='2024-06', id_region_guardia='100')
        response = self.client.get(self.url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id_planificacion'], '100')

    def test_retrieve_planificacion(self):
        model = TbDplanificacion.objects.create(id_planificacion='101', nombre_planificacion='Prueba 2', fecha_inicio='2024', fecha_fin='2024-06', id_region_guardia='100')
        response = self.client.get(f'{self.url}{model.id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id_planificacion'], '101')

    def test_update_planificacion(self):
        model = TbDplanificacion.objects.create(id_planificacion='102', nombre_planificacion='Prueba 3', fecha_inicio='2024', fecha_fin='2024-06', id_region_guardia='100')
        data = {'id_planificacion': '102', 'nombre_planificacion': 'Prueba 3'}
        response = self.client.put(f'{self.url}{model.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        model.refresh_from_db()
        self.assertEqual(model.id_planificacion, '102')

    def test_delete_my_model(self):
        model = TbDplanificacion.objects.create(id_planificacion='103', nombre_planificacion='Prueba 4')
        response = self.client.delete(f'{self.url}{model.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(TbDplanificacion.objects.count(), 0)


