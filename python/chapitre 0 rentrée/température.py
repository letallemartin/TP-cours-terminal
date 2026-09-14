x = int(input("température"))
if x >= 30:
    print("boire de l'eau")
elif x > 20 and x < 30:
    print("se baigner")
elif x > 0 and x <= 20:
    print("sortir couvert")
else:
    print("tient toi au chaud")
    