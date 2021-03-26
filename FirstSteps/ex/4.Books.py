pages_in_book = int(input())
pager_per_hour = int(input())
days = int(input())

result = (pages_in_book / pager_per_hour) / days
print(float(result))