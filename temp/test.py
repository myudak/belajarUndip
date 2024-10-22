import random


def password_generator(L: int) -> str:
    if int(L) < 6 or int(L) > 20:
        return "Invalid length"

    list_password = (
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*"
    )

    huruf_besar = random.choice(list_password[:26])
    huruf_kecil = random.choice(list_password[26:52])
    angka = random.choice(list_password[52:62])
    simbol = random.choice(list_password[62:70])
    sisa = "".join(random.choice(list_password) for _ in range(int(L) - 2))

    password = list(huruf_besar + huruf_kecil + sisa + angka + simbol)
    random.shuffle(password)

    return "".join(password)


print(
    password_generator(input()),
)
