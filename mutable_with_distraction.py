one_to_three = [1, 2, 3]
random_list = [3, 1, 2]


def foo(bar=one_to_three):
    bar.append(5)
    print(bar)



foo(one_to_three)
foo(one_to_three)
foo()
foo([1])
foo()
