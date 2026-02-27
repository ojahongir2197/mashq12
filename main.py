

# 1
def salom(ism="Dost"):
    print(f"Salom, {ism}!")

salom("joxa")
salom()


# 2
def daraja(raqam, d=2):
    return raqam ** d

print(daraja(3))
print(daraja(3, 3))


# 3
def matn_takror(matn, son=2):
    return matn * son

print(matn_takror("Salom "))
print(matn_takror("Hi ", 3))


# 4
def yosh_xabar(ism, yosh=18):
    print(f"{ism} {yosh} yoshda.")

yosh_xabar("jahongir")
yosh_xabar("bunyot", 20)


# 5
def qoshish(a, b=10):
    return a + b

print(qoshish(5))
print(qoshish(5, 3))


# 6
def kopaytirish(a, k=2):
    return a * k

print(kopaytirish(4))
print(kopaytirish(4, 5))


# 7
def xabar(matn="Xabar yo'q"):
    print(matn)

xabar()
xabar("Salom dunyo")


# 8
def tekshir(raqam, chegara=0):
    return raqam > chegara

print(tekshir(5))
print(tekshir(-2))


# 9
def matn_qosh(matn, qoshimcha="!"):
    return matn + qoshimcha

print(matn_qosh("Salom"))
print(matn_qosh("Hello", "!!!"))


# 10
def salomlash(ism="Mehmon"):
    return f"Xush kelibsiz, {ism}!"

print(salomlash())
print(salomlash("Jahongir"))
