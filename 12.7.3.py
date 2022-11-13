money = int(input('Введите сумму вклада '))

TKB = int(money * 5.6 / 100)
SKB = int(money * 5.9 / 100)
VTB = int(money * 4.28 / 100)
SBER = int(money * 4.0 / 100)
print ('Депозит ТКБ =',TKB, '\nДепозит СКБ =', SKB, '\nДепозит ВТБ =', VTB, '\nДепозит СБЕР =', SBER)
deposit = [TKB, SKB, VTB, SBER]
deposit_max = max(deposit)
print ('Лучший для депозита', deposit_max)

deposit_bank = {'ТКБ' : TKB, 'СКБ' : SKB, 'ВТБ' : VTB, 'СБЕР' : SBER}
max_value = max(deposit_bank.values())
max_value_key = max(deposit_bank, key=deposit_bank.get)
print ('Лучший по вкладу', max_value_key, '=', max_value, 'годовых')
