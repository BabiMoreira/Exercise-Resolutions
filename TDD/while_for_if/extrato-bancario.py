salario_integral= float(input('Digite o valor do seu salário:'))
inss = salario_integral*(9/100)
vale_transporte = salario_integral*(3/100)
plano_saude= 347*(15/100)
salario_liquido = salario_integral - inss - vale_transporte - plano_saude
print('EXTRATO BANCARIO: \nSalario Integral: {} \nInss: {} \nVale Transporte: {} \nPlano de Saúde: {} \nSalário Liquído: {}'.format(salario_integral, inss, vale_transporte, plano_saude, salario_liquido))


