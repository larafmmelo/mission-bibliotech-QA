# Caso de Teste
ID: CT-01
Requisito: RF01
Título: Usuário com três empréstimos não pode realizar outro empréstimo.
Tipo: Caixa preta
Prioridade: Alta
Pré-condição: Sistema disponível e usuário ativo.
Dados de teste: usuario_ativo = True, possui_pendencia = False, emprestimos_ativos = 3
Passos: 
1. Executar pode_emprestar(True, False, 3).
Resultado esperado: False
Resultado obtido: True
Status: [x] Falhou