"""
Каждая семья, живущая в доме N, выписывает газету, или журнал, или и то, и другое.
75 семей выписывают газету, 27 - журнал, 13 - и журнал, и газету.
Даны списки семей в квартирах.
Используя операции со множествами вычислите колько семей живёт в доме N.
"""
newspaper = range(1, 76)
magazine = range(77, 104)
both = range(21, 34)
n1 = len(set(newspaper)) - len(set(both))
n2 = len(set(magazine)) - len(set(both))
n3 = len(set(both))

total_families = n1 + n2 + n3

print("Количество семей, живущих в доме N:", total_families)