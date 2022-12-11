""" Сложность алгоритма O(n) из-за одного цикла. Проходим по связанному списку и записываем значения,
после чего возвращаем сравнение с обратной строкой."""


def isPalindrome(self, head):
    ptr = head
    pal = ''
    while ptr:
        pal = pal + str(ptr.val)
        ptr = ptr.next
    return pal == pal[::-1]