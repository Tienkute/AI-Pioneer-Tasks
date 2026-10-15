print("\n===== 9. EXCEPTION =====")
try:
    number = int(input("Nhap mot so: "))
    print("Ban da nhap:", number)
except ValueError:
    print("Loi: ban phai nhap mot so!")
