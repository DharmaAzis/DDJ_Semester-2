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

        self.label_qty = tk.Label(self.frame, text="Jumlah item:")
        self.label_qty.grid(row=1, column=0, sticky="w")

        self.label_qty = tk.Label(self.frame, text="KELOMPOK : ARKA DHARMA NAGA")
        self.label_qty.grid(row=17, column=0, sticky="w")

        self.qty_entry = tk.Entry(self.frame)
        self.qty_entry.grid(row=1, column=1)

        self.add_button = tk.Button(self.frame, text="Tambah", command=self.tambah_ke_keranjang)
        self.add_button.grid(row=2, columnspan=2)

        self.total_button = tk.Button(self.frame, text="Total Harga", command=self.total_harga)
        self.total_button.grid(row=6, columnspan=2)

        self.struk_text = tk.Text(self.frame, height=10, width=30)
        self.struk_text.grid(row=4, columnspan=2)

        # Menambahkan daftar uang tunai dan kembalian
        self.label_tunai = tk.Label(self.frame, text="Uang Tunai:")
        self.label_tunai.grid(row=3, column=0, sticky="w")

        self.tunai_entry = tk.Entry(self.frame)
        self.tunai_entry.grid(row=3, column=1)

        self.label_kembalian = tk.Label(self.frame, text="Kembalian:")
        self.label_kembalian.grid(row=8, column=0, sticky="w")

        self.kembalian_label = tk.Label(self.frame, text="", fg="green")
        self.kembalian_label.grid(row=8, column=1, sticky="w")

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

        # Menghitung kembalian
        try:
            tunai = int(self.tunai_entry.get())
            if tunai < total:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Uang tunai tidak valid atau kurang.")
            return

        kembalian = tunai - total
        self.kembalian_label.config(text=f"Rp{kembalian}")


def main():
    root = tk.Tk()
    app = KasirApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()