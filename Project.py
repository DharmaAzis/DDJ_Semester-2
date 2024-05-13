import tkinter as tk
from tkinter import messagebox

class KasirApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Yomart")

        self.daftar_item = {
            "Minyak": 18000,
            "Sabun": 3000,
            "Sikat gigi": 1000,
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

        self.setup_ui()

    def setup_ui(self):
        # Mengatur geometri jendela agar tampilan berada di tengah
        self.master.geometry("800x600+0+0")  # Ukuran 800x600, di tengah layar

        # Menambahkan label sambutan
        self.label_welcome = tk.Label(self.master, text="Selamat datang di Yomart", font=("Helvetica", 16))
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

        self.total_button = tk.Button(self.frame, text="Total Harga", command=self.total_harga)
        self.total_button.grid(row=3, columnspan=2)

        self.struk_text = tk.Text(self.frame, height=10, width=30)
        self.struk_text.grid(row=4, columnspan=2)

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
            self.keranjang[item] += qty
        else:
            self.keranjang[item] = qty

        messagebox.showinfo("Info", f"{qty} {item} ditambahkan ke keranjang.")

    def total_harga(self):
        total = sum(self.daftar_item[item] * qty for item, qty in self.keranjang.items())

        struk = "==== Struk Pembayaran ====\n"
        for item, qty in self.keranjang.items():
            struk += f"{item}: {qty} x Rp{self.daftar_item[item]}\n"
        struk += f"Total: Rp{total}\n"
        struk += "=========================="
        self.struk_text.delete(1.0, tk.END)
        self.struk_text.insert(tk.END, struk)


def main():
    root = tk.Tk()
    app = KasirApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
