counts = input().split()

n_set = set()
m_set = set()
n, m = counts
for _ in range(int(n)):
    num = int(input())
    n_set.add(num)

for _ in range(int(m)):
    num = int(input())
    m_set.add(num)

print(*(n_set & m_set), sep='\n')
