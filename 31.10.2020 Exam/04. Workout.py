from math import ceil

n_days = int(input())
m_km = float(input())
err = m_km
current_km = 0
total = 0

for i in range(1, n_days + 1):
    k_percent = int(input())
    current_km = m_km + (m_km * k_percent / 100)

    m_km = current_km
    total += m_km

diff = abs(total - 1000)

if total < 1000:
    print(f"Sorry Mrs. Ivanova, you need to run {ceil(diff - err)} more kilometers")
else:
    print(f"You've done a great job running {ceil(diff + err)} more kilometers!")