def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))

# Неправильное использование тернарного оператора и "summ" вместо "sum"