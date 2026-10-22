nama_toko = "Toko Pak Joko"
targetday = 450_000
uang = 0

print(f"\n=== {nama_toko} ===")

for hari in range(1,8):
    uang += targetday
    print(f"Day -{hari} : Rp{uang:,}".replace(",", "."))

print("-----------------------")
print(f"Total in Day 7: Rp{uang:,}".replace(",", "."))