import tkinter as tk

root = tk.Tk()
root.title("ĐĂNG NHẬP")

# Kích thước form
window_width = 300
window_height = 200

# Lấy kích thước màn hình
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Lấy vị trí ở giữa
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Đặt kích thước và vị trí
root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.configure(bg="#000000")

# ============================= Giao diện =============================

# Tiêu đề LOGIN
tk.Label(root, text="LOGIN", font=("Arial", 15, "bold"),
         bg="#000000", fg="#00B3FF").place(relx=0.5, rely=0.1, anchor="center")

# Username
tk.Label(root, text="Username", font=("Arial", 12),
         bg="#000000", fg="#FFA200").place(relx=0.025, rely=0.27, anchor="w")

entry_user = tk.Entry(root, font=("Arial", 12), fg="#000000")
entry_user.place(relx=0.35, rely=0.27, anchor="w")

# Password
tk.Label(root, text="Password", font=("Arial", 12),
         bg="#000000", fg="#FFA200").place(relx=0.025, rely=0.47, anchor="w")

entry_pass = tk.Entry(root, font=("Arial", 12), fg="#000000", show="*")
entry_pass.place(relx=0.35, rely=0.47, anchor="w")

# ============================= Chức năng =============================

# --- Nút Đăng nhập ---
btnDangnhap = tk.Button(root, text="Đăng nhập", font=("Arial", 12),
                        bg="#001f4d", fg="white")
btnDangnhap.place(relx=0.025, rely=0.7, width=90, anchor="w")

# --- Nút Xoá ---
btnXoa = tk.Button(root, text="Xoá", font=("Arial", 12),
                   bg="#001f4d", fg="white",
                   command=lambda: (entry_user.delete(0, tk.END), entry_pass.delete(0, tk.END)))
btnXoa.place(relx=0.5, rely=0.7, width=90, anchor="center")

# --- Nút Thoát ---
btnThoat = tk.Button(root, text="Thoát", font=("Arial", 12),
                     bg="#001f4d", fg="white",
                     command=root.quit)
btnThoat.place(relx=0.975, rely=0.7, width=90, anchor="e")

root.mainloop()
