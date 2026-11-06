# Version B: each pair typed in one go, like  max_connections=200
pair1 = input("Pair 1 (key=value): ")
pair2 = input("Pair 2 (key=value): ")
pair3 = input("Pair 3 (key=value): ")

print("[config]")
print("\t" + pair1.replace("=", " = "))
print("\t" + pair2.replace("=", " = "))
print("\t" + pair3.replace("=", " = "))
