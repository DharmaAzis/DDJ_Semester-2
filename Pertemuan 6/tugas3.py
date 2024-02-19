data_penjualan = [
    {"buah": "semangka", "jumlah":20},
    {"sayur": "tomat", "jumlah":28},
    {"obat": "paramex", "jumlah":40},
    {"celana": "jeans", "jumlah":70},
]

total_penjualan = 0
for item in data_penjualan:
    total_penjualan += item["jumlah"]

print("total penjualan : ", total_penjualan)