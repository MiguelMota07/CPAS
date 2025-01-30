def teste_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input())
for i in range (n):
    number = int(input())
    nu = int("".join(reversed(str(number))))
    # nu = int(str(number)[::-1])
    if teste_primo(nu) and teste_primo(number):
        print("SIM")
    else:
        print("NAO")