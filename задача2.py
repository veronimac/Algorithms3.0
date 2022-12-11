''' Сложность алгоритма O(2n) из-за двух не вложенных циклов. Проходим по значениям односвязанного списка и записываем значения,
после чего переводим в 10ную сис'''


def getDecimalValue(self, head):
    ptr = head
    num = ''
    while ptr != None:
        num = num + str(ptr.val)
        ptr = ptr.next

    count = 0
    for i in range(len(num)):  # Перевод в другую систему исчисления
        count += int(num[len(num) - 1 - i]) * 2 ** i

    return count