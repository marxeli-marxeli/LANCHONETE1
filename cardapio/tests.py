from django.contrib import admin
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Categoria, Produto


class CategoriaApiTests(APITestCase):
    def test_categoria_crud(self):
        list_url = reverse("categoria-list")
        response = self.client.post(
            list_url,
            {"nome": "Lanches", "descricao": "Lanches da casa"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        categoria_id = response.data["id"]

        self.assertEqual(self.client.get(list_url).status_code, status.HTTP_200_OK)
        detail_url = reverse("categoria-detail", kwargs={"pk": categoria_id})
        self.assertEqual(self.client.get(detail_url).status_code, status.HTTP_200_OK)
        self.assertEqual(
            self.client.patch(
                detail_url,
                {"descricao": "Atualizada"},
                format="json",
            ).status_code,
            status.HTTP_200_OK,
        )
        self.assertEqual(
            self.client.put(
                detail_url,
                {"nome": "Burgers", "descricao": "Hambúrgueres"},
                format="json",
            ).status_code,
            status.HTTP_200_OK,
        )
        self.assertEqual(
            self.client.delete(detail_url).status_code,
            status.HTTP_204_NO_CONTENT,
        )
        self.assertEqual(self.client.get(detail_url).status_code, status.HTTP_404_NOT_FOUND)


class ProdutoApiTests(APITestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nome="Lanches")

    def test_produto_crud(self):
        list_url = reverse("produto-list")
        response = self.client.post(
            list_url,
            {
                "nome": "X-Burger",
                "preco": "12.50",
                "disponivel": True,
                "categoria": self.categoria.pk,
            },
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        produto_id = response.data["id"]

        self.assertEqual(self.client.get(list_url).status_code, status.HTTP_200_OK)
        detail_url = reverse("produto-detail", kwargs={"pk": produto_id})
        self.assertEqual(self.client.get(detail_url).status_code, status.HTTP_200_OK)
        self.assertEqual(
            self.client.patch(
                detail_url,
                {"disponivel": False},
                format="json",
            ).status_code,
            status.HTTP_200_OK,
        )
        self.assertEqual(
            self.client.put(
                detail_url,
                {
                    "nome": "X-Burger Duplo",
                    "preco": "17.00",
                    "disponivel": True,
                    "categoria": self.categoria.pk,
                },
                format="json",
            ).status_code,
            status.HTTP_200_OK,
        )
        self.assertEqual(
            self.client.delete(detail_url).status_code,
            status.HTTP_204_NO_CONTENT,
        )
        self.assertEqual(self.client.get(detail_url).status_code, status.HTTP_404_NOT_FOUND)


class AdminRegistrationTests(TestCase):
    def test_cardapio_models_are_registered(self):
        self.assertTrue(admin.site.is_registered(Categoria))
        self.assertTrue(admin.site.is_registered(Produto))
