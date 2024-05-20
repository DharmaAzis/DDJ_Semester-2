import tkinter as tk
from tkinter import messagebox

class KasirApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Project kasir supermarket")

        self.daftar_item = {
            "Minyak": 18000,
            "Sabun": 3000,
            "Sikat gigi": 4000,
            "Saus": 5000,
            "Parfume": 30000,
            "Sabun cuci piring": 4000,
            "Pewangi ruangan": 20000,
            "Snack": 5000,
            "Es cream": 3500,
            "Sabun cuci muka": 17500,
            "Sereal": 35000,
            "Minuman": 8000
        }

        self.keranjang = {}
        self.total_harga = 0

        self.setup_ui()

    def setup_ui(self):
        # Mengatur geometri jendela agar tampilan berada di tengah
        self.master.geometry("400x500")
        self.master.eval('tk::PlaceWindow . center')

        # Menambahkan label sambutan
        self.label_welcome = tk.Label(self.master, text="Selamat datang di Supermarket", font=("Helvetica", 16))
        self.label_welcome.pack(pady=10)

        # Membuat frame untuk menempatkan elemen-elemen GUI
        self.frame = tk.Frame(self.master)
        self.frame.pack(padx=10, pady=10)

        # Menambahkan elemen-elemen GUI ke dalam frame
        self.label_item = tk.Label(self.frame, text="Pilih Item:")
        self.label_item.grid(row=0, column=0, sticky="w")

        self.item_var = tk.StringVar()
        self.item_var.set("Minyak")  # Item default
        self.item_option = tk.OptionMenu(self.frame, self.item_var, *self.daftar_item.keys())
        self.item_option.grid(row=0, column=1)

        self.label_qty = tk.Label(self.frame, text="Jumlah:")
        self.label_qty.grid(row=1, column=0, sticky="w")

        self.qty_entry = tk.Entry(self.frame)
        self.qty_entry.grid(row=1, column=1)

        self.add_button = tk.Button(self.frame, text="Tambah", command=self.tambah_ke_keranjang)
        self.add_button.grid(row=2, columnspan=2)

        self.label_keranjang = tk.Label(self.frame, text="Keranjang Belanja:")
        self.label_keranjang.grid(row=3, columnspan=2)

        self.keranjang_text = tk.Text(self.frame, height=10, width=40)
        self.keranjang_text.grid(row=4, columnspan=2)

        self.label_total_harga = tk.Label(self.frame, text="Total Harga:")
        self.label_total_harga.grid(row=5, columnspan=2)

        self.total_harga_label = tk.Label(self.frame, text="")
        self.total_harga_label.grid(row=6, columnspan=2)

    def tambah_ke_keranjang(self):
        item = self.item_var.get()
        try:
            qty = int(self.qty_entry.get())
            if qty <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Jumlah harus bilangan bulat positif.")
            return

        if item in self.keranjang:
            self.keranjang[item]["qty"] += qty
        else:
            self.keranjang[item] = {"qty": qty, "harga": self.daftar_item[item]}

        self.update_keranjang_text()

    def update_keranjang_text(self):
        self.keranjang_text.delete(1.0, tk.END)
        for item, data in self.keranjang.items():
            qty = data["qty"]
            harga = data["harga"]
            total_harga = qty * harga
            self.keranjang_text.insert(tk.END, f"{item}: {qty} x Rp{harga} = Rp{total_harga}\n")
        self.update_total_harga()

    def update_total_harga(self):
        self.total_harga = sum(data["qty"] * data["harga"] for data in self.keranjang.values())
        self.total_harga_label.config(text=f"Rp{self.total_harga}")

def main():
    root = tk.Tk()
    app = KasirApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
import tkinter as tk
from tkinter import messagebox

class KasirApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Project kasir supermarket")

        self.daftar_item = {
            "Minyak": 18000,
            "Sabun": 3000,
            "Sikat gigi": 4000,
            "Saus": 5000,
            "Parfume": 30000,
            "Sabun cuci piring": 4000,
            "Pewangi ruangan": 20000,
            "Snack": 5000,
            "Es cream": 3500,
            "Sabun cuci muka": 17500,
            "Sereal": 35000,
            "Minuman": 8000
        }

        self.keranjang = {}
        self.total_harga = 0

        self.setup_ui()

    def setup_ui(self):
        # Mengatur geometri jendela agar tampilan berada di tengah
        self.master.geometry("400x550")
        self.master.eval('tk::PlaceWindow . center')

        # Menambahkan label sambutan
        self.label_welcome = tk.Label(self.master, text="Selamat datang di Supermarket", font=("Helvetica", 16))
        self.label_welcome.pack(pady=10)

        # Membuat frame untuk menempatkan elemen-elemen GUI
        self.frame = tk.Frame(self.master)
        self.frame.pack(padx=10, pady=10)

        # Menambahkan elemen-elemen GUI ke dalam frame
        self.label_item = tk.Label(self.frame, text="Pilih Item:")
        self.label_item.grid(row=0, column=0, sticky="w")

        self.item_var = tk.StringVar()
        self.item_var.set("Minyak")  # Item default
        self.item_option = tk.OptionMenu(self.frame, self.item_var, *self.daftar_item.keys())
        self.item_option.grid(row=0, column=1)

        self.label_qty = tk.Label(self.frame, text="Jumlah:")
        self.label_qty.grid(row=1, column=0, sticky="w")

        self.qty_entry = tk.Entry(self.frame)
        self.qty_entry.grid(row=1, column=1)

        self.add_button = tk.Button(self.frame, text="Tambah", command=self.tambah_ke_keranjang)
        self.add_button.grid(row=2, columnspan=2)

        self.label_keranjang = tk.Label(self.frame, text="Keranjang Belanja:")
        self.label_keranjang.grid(row=3, columnspan=2)

        self.keranjang_text = tk.Text(self.frame, height=10, width=40)
        self.keranjang_text.grid(row=4, columnspan=2)

        self.label_total_harga = tk.Label(self.frame, text="Total Harga:")
        self.label_total_harga.grid(row=5, columnspan=2)

        self.total_harga_label = tk.Label(self.frame, text="")
        self.total_harga_label.grid(row=6, columnspan=2)

        # Menambahkan inputan pembayaran
        self.label_pembayaran = tk.Label(self.frame, text="Pembayaran:")
        self.label_pembayaran.grid(row=7, column=0, sticky="w")

        self.pembayaran_entry = tk.Entry(self.frame)
        self.pembayaran_entry.grid(row=7, column=1)

        self.total_button = tk.Button(self.frame, text="Total Harga", command=self.total_harga)
        self.total_button.grid(row=8, columnspan=2)

    def tambah_ke_keranjang(self):
        item = self.item_var.get()
        try:
            qty = int(self.qty_entry.get())
            if qty <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Jumlah harus bilangan bulat positif.")
            return

        if item in self.keranjang:
            self.keranjang[item]["qty"] += qty
        else:
            self.keranjang[item] = {"qty": qty, "harga": self.daftar_item[item]}

        self.update_keranjang_text()

    def update_keranjang_text(self):
        self.keranjang_text.delete(1.0, tk.END)
        for item, data in self.keranjang.items():
            qty = data["qty"]
            harga = data["harga"]
            total_harga = qty * harga
            self.keranjang_text.insert(tk.END, f"{item}: {qty} x Rp{harga} = Rp{total_harga}\n")
        self.update_total
