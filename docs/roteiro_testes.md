# Roteiro de Testes - BiblioTech

## RF01 — Permissão para empréstimo

### Caso de Teste: CT-01
- **Requisito:** RF01
- **Título:** Usuário ativo, sem pendências e sem empréstimos pode realizar empréstimo.
- **Tipo:** Caixa preta
- **Prioridade:** Alta
- **Pré-condição:** Sistema disponível e usuário ativo.
- **Dados de teste:** `usuario_ativo = True`, `possui_pendencia = False`, `emprestimos_ativos = 0`
- **Passos:** 
  1. Executar `pode_emprestar(True, False, 0)`.
- **Resultado esperado:** `True`
- **Resultado obtido:** `True`
- **Status:** [x] Passou / [ ] Falhou

### Caso de Teste: CT-02
- **Requisito:** RF01
- **Título:** Usuário inativo não pode realizar empréstimo.
- **Tipo:** Caixa preta
- **Prioridade:** Alta
- **Pré-condição:** Sistema disponível.
- **Dados de teste:** `usuario_ativo = False`, `possui_pendencia = False`, `emprestimos_ativos = 0`
- **Passos:** 
  1. Executar `pode_emprestar(False, False, 0)`.
- **Resultado esperado:** `False`
- **Resultado obtido:** `False`
- **Status:** [x] Passou / [ ] Falhou

### Caso de Teste: CT-03
- **Requisito:** RF01
- **Título:** Usuário com pendência não pode realizar empréstimo.
- **Tipo:** Caixa preta
- **Prioridade:** Alta
- **Pré-condição:** Sistema disponível.
- **Dados de teste:** `usuario_ativo = True`, `possui_pendencia = True`, `emprestimos_ativos = 0`
- **Passos:** 
  1. Executar `pode_emprestar(True, True, 0)`.
- **Resultado esperado:** `False`
- **Resultado obtido:** `False`
- **Status:** [x] Passou / [ ] Falhou

### Caso de Teste: CT-04
- **Requisito:** RF01
- **Título:** Usuário com exatamente 3 empréstimos ativos não pode realizar outro empréstimo (Fronteira / Revela o defeito).
- **Tipo:** Caixa preta
- **Prioridade:** Alta
- **Pré-condição:** Sistema disponível e usuário ativo.
- **Dados de teste:** `usuario_ativo = True`, `possui_pendencia = False`, `emprestimos_ativos = 3`
- **Passos:** 
  1. Executar `pode_emprestar(True, False, 3)`.
- **Resultado esperado:** `False` (Conforme a regra de "menos de 3 empréstimos")
- **Resultado obtido:** `True` (O sistema permitiu indevidamente devido ao bug proposital)
- **Status:** [ ] Passou / [x] Falhou *(O teste automatizado falhará aqui, o que comprova o sucesso do QA em achar o bug)*
## RF02 — Multa por atraso

### Caso de Teste: CT-05
- **Requisito:** RF02
- **Título:** Atraso de 0 dias não gera multa (Fronteira inferior).
- **Tipo:** Caixa preta
- **Prioridade:** Média
- **Pré-condição:** Sistema disponível.
- **Dados de teste:** `dias_atraso = 0`
- **Passos:** 
  1. Executar `calcular_multa(0)`.
- **Resultado esperado:** `0.0`
- **Resultado obtido:** `0.0`
- **Status:** [x] Passou / [ ] Falhou

### Caso de Teste: CT-06
- **Requisito:** RF02
- **Título:** Atraso de 3 dias gera multa de R$ 6,00 (Faixa de 1 a 7 dias).
- **Tipo:** Caixa preta
- **Prioridade:** Média
- **Pré-condição:** Sistema disponível.
- **Dados de teste:** `dias_atraso = 3`
- **Passos:** 
  1. Executar `calcular_multa(3)`.
- **Resultado esperado:** `6.0`
- **Resultado obtido:** `6.0`
- **Status:** [x] Passou / [ ] Falhou

### Caso de Teste: CT-07
- **Requisito:** RF02
- **Título:** Atraso de 7 dias gera multa de R$ 14,00 (Fronteira superior da 1ª faixa).
- **Tipo:** Caixa preta
- **Prioridade:** Média
- **Pré-condição:** Sistema disponível.
- **Dados de teste:** `dias_atraso = 7`
- **Passos:** 
  1. Executar `calcular_multa(7)`.
- **Resultado esperado:** `14.0`
- **Resultado obtido:** `14.0`
- **Status:** [x] Passou / [ ] Falhou

### Caso de Teste: CT-08
- **Requisito:** RF02
- **Título:** Atraso de 10 dias calcula corretamente a multa com dias excedentes (Acima de 7 dias).
- **Tipo:** Caixa preta
- **Prioridade:** Alta
- **Pré-condição:** Sistema disponível.
- **Dados de teste:** `dias_atraso = 10`
- **Passos:** 
  1. Executar `calcular_multa(10)`.
- **Resultado esperado:** `23.0` (R$ 14,00 + (3 dias excedentes * R$ 3,00))
- **Resultado obtido:** `23.0`
- **Status:** [x] Passou / [ ] Falhou

## RF03 — Classificação de atraso

### Caso de Teste: CT-09
- **Requisito:** RF03
- **Título:** Atraso de 0 dias classifica como "sem atraso".
- **Tipo:** Caixa preta
- **Prioridade:** Baixa
- **Pré-condição:** Sistema disponível.
- **Dados de teste:** `dias_atraso = 0`
- **Passos:** 
  1. Executar `classificar_atraso(0)`.
- **Resultado esperado:** `"sem atraso"`
- **Resultado obtido:** `"sem atraso"`
- **Status:** [x] Passou / [ ] Falhou

### Caso de Teste: CT-10
- **Requisito:** RF03
- **Título:** Atraso de até 7 dias classifica como "atraso leve".
- **Tipo:** Caixa preta (Fronteira)
- **Prioridade:** Baixa
- **Pré-condição:** Sistema disponível.
- **Dados de teste:** `dias_atraso = 7`
- **Passos:** 
  1. Executar `classificar_atraso(7)`.
- **Resultado esperado:** `"atraso leve"`
- **Resultado obtido:** `"atraso leve"`
- **Status:** [x] Passou / [ ] Falhou

### Caso de Teste: CT-11
- **Requisito:** RF03
- **Título:** Atraso de 8 dias classifica como "atraso moderado".
- **Tipo:** Caixa preta (Início da faixa)
- **Prioridade:** Baixa
- **Pré-condição:** Sistema disponível.
- **Dados de teste:** `dias_atraso = 8`
- **Passos:** 
  1. Executar `classificar_atraso(8)`.
- **Resultado esperado:** `"atraso moderado"`
- **Resultado obtido:** `"atraso moderado"`
- **Status:** [x] Passou / [ ] Falhou

### Caso de Teste: CT-12
- **Requisito:** RF03
- **Título:** Atraso acima de 30 dias classifica como "atraso grave".
- **Tipo:** Caixa preta (Fronteira)
- **Prioridade:** Baixa
- **Pré-condição:** Sistema disponível.
- **Dados de teste:** `dias_atraso = 31`
- **Passos:** 
  1. Executar `classificar_atraso(31)`.
- **Resultado esperado:** `"atraso grave"`
- **Resultado obtido:** `"atraso grave"`
- **Status:** [x] Passou / [ ] Falhou