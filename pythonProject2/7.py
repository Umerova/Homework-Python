k = {0:'Гагарин Юрий Алексеевич'}

def fio(full_name):
    surname, name, patronymic = full_name.split()
    return ' '.join((surname, f'{name[0]}.', f'{patronymic[0]}.'))

k = {key: fio(val) for key,val in k.items()}
print(k)
