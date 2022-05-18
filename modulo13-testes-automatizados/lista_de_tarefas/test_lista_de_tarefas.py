from datetime import datetime, timedelta
import unittest

from tarefa import Tarefa
from lista_de_tarefas import ListaDeTarefas


class TestAdicionarTarefa(unittest.TestCase):
    def test_adiciona_tarefa_a_lista_de_tarefas(self):
        tarefa = Tarefa("Tarefa Teste")
        lista = ListaDeTarefas()

        lista.adicionar_tarefa(tarefa)

        # self.assertEqual(lista.get_tarefas()[0], tarefa)
        self.assertIn(tarefa, lista.get_tarefas())


class TestGetTarefas(unittest.TestCase):
    def test_retorna_lista_de_tarefas_adicionadas(self):
        tarefa_um = Tarefa("Tarefa Teste 1")
        tarefa_dois = Tarefa("Tarefa Teste 2")
        lista = ListaDeTarefas()

        lista.adicionar_tarefa(tarefa_um)
        lista.adicionar_tarefa(tarefa_dois)

        self.assertEqual(lista.get_tarefas(), [
            tarefa_um,
            tarefa_dois,
        ])


class TestGetTarefasAtrasadas(unittest.TestCase):
    def test_retorna_lista_tarefas_atrasadas(self):
        hoje = datetime.now()
        tarefa_um = Tarefa("Tarefa Teste 1", data=hoje - timedelta(minutes=10))
        tarefa_dois = Tarefa("Tarefa Teste 2", data=hoje - timedelta(days=2))
        tarefa_tres = Tarefa("Tarefa Teste 3", data=hoje + timedelta(seconds=1))
        tarefa_quatro = Tarefa("Tarefa Teste 4", data=hoje + timedelta(days=1))
        lista = ListaDeTarefas()
        
        lista.adicionar_tarefa(tarefa_um)
        lista.adicionar_tarefa(tarefa_dois)
        lista.adicionar_tarefa(tarefa_tres)
        lista.adicionar_tarefa(tarefa_quatro)
        
        self.assertListEqual([tarefa_um, tarefa_dois], lista.get_tarefas_atrasadas())


class TestGetTarefasHoje(unittest.TestCase):
    def test_retorna_lista_tarefas_hoje(self):
        hoje = datetime.now()
        tarefa_um = Tarefa("Tarefa Teste 1", data=hoje - timedelta(minutes=10))
        tarefa_dois = Tarefa("Tarefa Teste 2", data=hoje - timedelta(days=2))
        tarefa_tres = Tarefa("Tarefa Teste 3", data=hoje + timedelta(seconds=1))
        tarefa_quatro = Tarefa("Tarefa Teste 4", data=hoje + timedelta(days=1))
        lista = ListaDeTarefas()
        
        lista.adicionar_tarefa(tarefa_um)
        lista.adicionar_tarefa(tarefa_dois)
        lista.adicionar_tarefa(tarefa_tres)
        lista.adicionar_tarefa(tarefa_quatro)
        
        self.assertListEqual([tarefa_um, tarefa_tres], lista.get_tarefas_para_hoje())

unittest.main()