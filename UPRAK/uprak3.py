belanja = [
    {"buah":"apel", "harga":5000*10},
    {"buah":"nanas", "harga":3000*5},
    {"buah":"pepaya", "harga":7000*7},
    {"buah":"pisang", "harga":2000*20},
    {"buah":"semangka", "harga":15000*1},
  ]

total_belanjaan = 0
for item in belanja:
    total_belanjaan += item["harga"]

print("Total Belanja : ", total_belanjaan)    