from src.bibliotech import pode_emprestar, calcular_multa, classificar_atraso

# --- TESTES DE EMPRÉSTIMO (Os que você já tinha feito) ---
def test_usuario_valido_pode_emprestar():
    assert pode_emprestar(True, False, 0) is True

def test_usuario_inativo_nao_pode_emprestar():
    assert pode_emprestar(False, False, 0) is False

def test_usuario_com_pendencia_nao_pode_emprestar():
    assert pode_emprestar(True, True, 0) is False

def test_usuario_no_limite_nao_pode_emprestar():
    assert pode_emprestar(True, False, 3) is False

# --- NOVOS TESTES: CÁLCULO DE MULTA ---
def test_multa_zero_dias():
    assert calcular_multa(0) == 0.0

def test_multa_ate_sete_dias():
    assert calcular_multa(3) == 6.0

def test_multa_acima_de_sete_dias():
    assert calcular_multa(10) == 23.0

# --- NOVOS TESTES: CLASSIFICAÇÃO DE ATRASO ---
def test_classificacao_sem_atraso():
    assert classificar_atraso(0) == "sem atraso"

def test_classificacao_atraso_leve():
    assert classificar_atraso(5) == "atraso leve"

def test_classificacao_atraso_moderado():
    assert classificar_atraso(15) == "atraso moderado"

def test_classificacao_atraso_grave():
    assert classificar_atraso(35) == "atraso grave"
    