import random

def gerar_sugestao():
    # Sugestão aleatória para demonstração
    acoes = ['compra', 'venda', 'aguardar']
    return {
        'acao': random.choice(acoes),
        'preco_referencia': round(random.uniform(20000, 30000), 2),
        'quantidade': 0.001
    }
