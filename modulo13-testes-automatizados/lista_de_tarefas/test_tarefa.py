import unittest
from datetime import datetime, timedelta
from tarefa import Tarefa


class TestConcluir(unittest.TestCase):
    def test_concluir_tarefa_altera_concluido_para_true(self):
        tarefa = Tarefa("Estudar Python")
        tarefa.concluir()
        self.assertEqual(tarefa.concluida, True)

    def test_concluir_tarefa_concluida_mantem_concluida_como_true(self):
        tarefa = Tarefa("Estudar Python")
        tarefa.concluir()
        self.assertEqual(tarefa.concluida, True)
        tarefa.concluir()
        self.assertEqual(tarefa.concluida, True)


class TestAdiarNotificacao(unittest.TestCase):
    def test_adia_notificacao_em_N_minutos(self):
        dt_original = datetime(2022, 2, 10, 9, 10)  # year, month, day, hour, minute, second, millisecond
        tarefa = Tarefa("Estudar Python", data_notificacao=dt_original)
        teste = tarefa.adiar_notificacao(15)
        
        print(f"tarefa.data_notificacao => {tarefa.data_notificacao}")

        dt_esperado = datetime(2022, 2, 10, 9, 25)
        self.assertEqual(tarefa.data_notificacao, dt_esperado)
        
class TestAdicionarDescricao(unittest.TestCase):
    def test_add_descricao(self):
        descricao = 'Descrição da tarefa teste'
        tarefa = Tarefa("Tarefa teste", data_notificacao=datetime.now())
        tarefa.adicionar_descricao(descricao)
        
        self.assertEqual(tarefa.descricao, descricao)
        
class TestVerificarTarefaAtrasada(unittest.TestCase):
    def test_verificar_tarefa_atrasada(self):
        hoje = datetime.now()
        tarefa = Tarefa("Estudar Python", data=hoje - timedelta(days=1))
        
        self.assertEqual(tarefa.atrasada(), True)
        
class TestVerificarTarefaNaoAtrasada(unittest.TestCase):
    def test_verificar_tarefa_atrasada(self):
        hoje = datetime.now()
        tarefa = Tarefa("Estudar Python", data=hoje + timedelta(days=1))
        
        self.assertEqual(tarefa.atrasada(), False)


unittest.main()