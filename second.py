"""Дан массив целых чисел. Нужно удалить из него нули. 
Можно использовать только О(1) дополнительной памяти."""

arr = list(map(int, input().split()))

try:
	while 1:
		arr.remove(0)
except ValueError:
	pass
print(arr)

