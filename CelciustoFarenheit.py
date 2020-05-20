def conversion(scale=None, temp=None):
    if scale == "F":
        return'C', round((temp - 32.0) * (.55))
    elif scale == "f":
        return 'C', round((temp - 32.0) * (.55))
    elif scale == "C":
        return 'F', round((temp * 1.8) + 32.0)
    elif scale == "c":
        return 'F', round((temp * 1.8) + 32.0)
    else:
        print("Needs to be (F) or (C)!")

scale = str(input("Select (F) or (C)"))
temp = int(input("What Is The Temperature"))
s, m = conversion(scale,temp)
print(temp, "degrees", scale, "is", m, "degrees", s)