def calcular_salario(horaTr, recebeHr):
    salario = horaTr*recebeHr
    return salario

horas_tr = float(input('Digite as horas trabalhadas: '))
recebe_hr = float(input('Digite quanto recebe por hora: '))

resultado = calcular_salario(horas_tr,recebe_hr)
print(resultado)