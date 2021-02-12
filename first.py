first_lst = list(map(int, input().split()))
second_lst = list(map(int, input().split()))

first_set = set(first_lst)
second_set = set(second_lst)

print(first_set - second_set)
input()