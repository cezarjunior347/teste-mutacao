def calcular_bonus(salario, anos_empresa, cargo):

    # REGRA SABOTADA
    if anos_empresa >= 0:
        return salario * 0.15

    return 0