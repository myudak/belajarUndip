"""
Problem: Cinema Ticket Booking System

Description: You are tasked with developing a cinema ticket booking system. The system must handle customer requests for movie tickets and calculate the total cost of the tickets based on the number of tickets requested and the type of seats chosen (Standard, Premium, or VIP).

Standard Seat: 50,000 IDR
Premium Seat: 75,000 IDR
VIP Seat: 100,000 IDR

If the number of tickets requested is more than 5, a 10% discount should be applied to the total cost. The system should ensure that no more than 10 tickets can be purchased in a single transaction.

Input:
- An integer T (1 ≤ T ≤ 10), the number of tickets requested.
- A string S, the type of seat selected ("Standard", "Premium", or "VIP").

Output:
- A single integer representing the total cost of the tickets, taking into account any applicable discount.
"""


def cinema_ticket(T, S):
    if T < 1 or T > 10:
        return 0
    if S == "Standard":
        if T > 5:
            return 50000 * T - 50000
        return 50000 * T
    if S == "Premium":
        if T > 5:
            return 50000 * T - 50000
        return 50000 * T
    if S == "VIP":
        if T > 5:
            return 50000 * T - 50000
        return 50000 * T


"""
Problem 1: Guess a Number Game (Game Tebak Angka)
English Version:

Description: You are developing a game where the system randomly picks a number between 1 and 100, and the player has to guess it. After each guess, the system will provide feedback whether the guessed number is too low, too high, or correct.

The system should also keep track of the number of attempts it took the player to guess the correct number.

Input:
- An integer G (1 ≤ G ≤ 100), representing the guessed number.

Output:
- If the guessed number is correct, print the number of attempts taken.
- If the guessed number is too low, print "Too low!"
- If the guessed number is too high, print "Too high!"
"""

import random


def guess_number(G):
    if G < 1 or G > 100:
        return "Invalid number"
    if G == random.randint(1, 100):
        return "Correct"
    if G < random.randint(1, 100):
        return "Too low!"
    return "Too high!"


"""
Description: Create a password generator that generates a random password with a specified length. The password must include a mix of uppercase letters, lowercase letters, numbers, and special characters.

Input:
- An integer L (8 ≤ L ≤ 20), representing the length of the password.

Output:
- A string representing the randomly generated password.
"""


def generate_password(L):
    if L < 8 or L > 20:
        return "Invalid length"
    password = (
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-="
    )
    return "".join(random.choice(password) for i in range(L))


"""
Description: At an airport, passengers are assigned to different queues based on their ticket type (Economy, Business, First Class). Your task is to implement a system that simulates the boarding process, where passengers in higher classes (First Class > Business > Economy) board first. For passengers within the same class, they board in the order of arrival.

Input:
- An integer N (1 ≤ N ≤ 100), the number of passengers.
N lines follow, each containing a string representing the passenger’s name and their ticket type ("Economy", "Business", "First").

Output:
- Print the names of the passengers in the order they should board the plane.
"""


def boarding_passengers(N):
    passengers = []
    for i in range(int(N)):
        passengers.append(input())
    passengers.sort(
        key=lambda x: {"First": 1, "Business": 2, "Economy": 3}.get(x.split(" ")[1], 4)
    )
    for i in passengers:
        print(i.split(" ")[0])


print(generate_password(8))


"""
============================================
"""

# Problem 1: Guess a Number Game
import random


def guess_numbers(user: int, target=random.randint(1, 100)) -> str:
    if user < 1 or user > 100:
        return "INVALID"
    if user > target:
        return "Kegedean"
    if user < target:
        return "Kekecilan"
    return "BETUL"


print(guess_numbers(100))

# Problem 2: Password Generator (Generator Kata Sandi)


def password_generators(L):
    if L < 8 or L > 20:
        raise Exception("error")
    list_passwords = (
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()1234567890"
    )

    uppercase = random.choice(list_passwords[:27])
    lowercase = random.choice(list_passwords[27:54])
    special_numbers = random.choice(list_passwords[54:62])
    numbers = random.choice(list_passwords[62:72])
    sisanya = "".join(random.choice(list_passwords) for _ in range(L - 4))

    password = list(uppercase + lowercase + special_numbers + numbers + sisanya)
    random.shuffle(password)

    return "".join(password)


print(password_generators(8))

# Problem 3: Cinema Ticket Booking System (Sistem Pemesanan Tiket Bioskop)


def cinema_ticket_booking(T: int, s: str) -> int:
    TEMPAT_DUDUK = {
        "Standard": 50000,
        "Premium": 75000,
        "VIP": 100000,
    }

    if T < 1 or T > 10:
        return "ERRROR!"
    if s not in TEMPAT_DUDUK:
        return "ERROR"

    harga = T * TEMPAT_DUDUK[s]
    if T > 5:
        harga = harga * 0.9
    return int(harga)


print(cinema_ticket_booking(6, "Premium"))

# Problem 4: Airport Queue System (Sistem Antrian Bandara)


def airport_queue_system():
    N = input()
    types = []

    for _ in range(int(N)):
        types.append(input())

    urutan = {"First": 1, "Business": 2, "Economy": 3}

    jawaban = sorted(types, key=lambda x: urutan.get(x.split(" ")[1], 4))
    for orang in jawaban:
        print(orang.split(" ")[0])


airport_queue_system()
