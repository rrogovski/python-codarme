from django.test import TestCase, Client

# Create your tests here.
class TestPaginaInicial(TestCase):
    def test_lista_eventos(self):
        client = Client()
        response = client.get("/")
        # print(response.content)
        # self.assertContains(response,"""<h2 class="text-3xl font-bold mb-12 pb-4 text-center">Últimos Eventos</h2>""")
        self.assertTemplateUsed(response, "agenda/listar_eventos.html")