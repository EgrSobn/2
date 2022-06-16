# рекурсия
def gen_bin_tree_rec(height: int, root: int) -> dict:
    if height == 0:
        return {root: []}

    return {
        str(root): [
            gen_bin_tree(height - 1, root * 2),
            gen_bin_tree(height - 1, root + 2)
        ]
    }

# не рекурсия
def gen_bin_tree(height: int, root: int) -> dict:
    tree = {str(root): []}
    if height == 0:
        return tree

    roots = [[root]]

    for l in range(1, height + 1):
        if len(roots) == 1:
            _r = roots[-1]
        else:
            _r = [item for sublist in roots[-1] for item in sublist]

        leaves = list(map(lambda r: [r * 2, r + 2], _r))
        roots.append(leaves)

    str_roots = [
        str(item) for sublist2 in roots[1:] for sublist in sublist2
        for item in sublist
    ]
    str_roots.insert(0, str(roots[0][0]))
    dict_roots = list(map(lambda r: {r: []}, str_roots))

    start = pow(2, height) - 1
    for i in reversed(range(start)):
        dict_roots[i][str_roots[i]].append(dict_roots[i * 2 + 1])
        dict_roots[i][str_roots[i]].append(dict_roots[i * 2 + 2])

    tree = dict_roots[0]
    return tree

# тесты с другими значениями
def other(n: int) -> list:
    from random import randint
    min_height = 0
    max_height = 10
    min_root = -1000
    max_root = 1000
    data = [None] * n
    for i in range(n):
        data[i] = [
            randint(min_height, max_height),
            randint(min_root, max_root)
        ]

    return data

#модуль расчета времени
def calculate_time(data, func) -> float:
    import timeit
    delta = 0
    for n in data:
        start_time = timeit.default_timer()
        func(n[0], n[1])
        delta += timeit.default_timer() - start_time

    return delta

# запуск кода + график через matplot
import matplotlib.pyplot as plt
result1 = []
result2 = []
data_list = []
my_range = range(10, 500, 10)
for n in my_range:
    data_list.append(other(n))
for d in data_list:
    result1.append([calculate_time(d, gen_bin_tree)])
for d in data_list:
    result2.append([calculate_time(d, gen_bin_tree_rec)])

fig, ax = plt.subplots()
ax.plot(my_range, result2, label='Рекурсивный')
ax.plot(my_range, result1, label='Нерекурсивный')

ax.legend()
plt.show()

h = int(5) 
r = int(1)

print(gen_bin_tree_rec(h, r), "\n")
print(gen_bin_tree(h, r))