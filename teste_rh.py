from rh import calcular_bonus


def test_bonus_aprovado():
    assert calcular_bonus(5000, 5, "DESENVOLVEDOR") == 750


def test_bonus_sem_tempo_empresa():
    assert calcular_bonus(5000, 2, "DESENVOLVEDOR") == 0


def test_bonus_cargo_errado():
    assert calcular_bonus(5000, 5, "GERENTE") == 0


def test_bonus_sem_requisitos():
    assert calcular_bonus(5000, 1, "ESTAGIARIO") == 0