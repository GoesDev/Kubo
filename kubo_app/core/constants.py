from enum import Enum

TIPO_CONTA = ['Corrente', 'Poupança']

class TipoTransacao(Enum):
    """Representa se a transação é Receita ou Despesa."""
    RECEITA = 'Receita'
    DESPESA = 'Despesa'
    TRANSFERENCIA = 'Transferência'

# --- VARIÁVEIS DE CONFIGURAÇÃO GERAL ---

LIMITE_ALERTA_ORCAMENTO = 0.80  # 80% do orçamento consumido dispara um alerta
MOEDA_PADRAO = 'BRL'            # Código da moeda padrão (Real Brasileiro)