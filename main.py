def is_palindrome(n):
    '''
    verifica daca un nr dat este palindrom
    :param n: nr natural
    :return: true=este palindrom sau false=NU este palindrom
    '''
    ogl = 0
    cop = n
    while cop != 0:
        ogl = ogl * 10 + cop % 10
        cop = cop // 10
    if ogl == n:
        return True
    else:
        return False


def is_superprime(n):
    '''
    Determină dacă un număr este superprim: dacă toate prefixele sale sunt prime.
    :param n: nr natural
    :return: true=este superprim sau false=NU este superprim
    '''
    p = 1
    cop = n
    while cop > 9:
        cop = cop // 10
        p = p * 10

    while p != 0:
        nr = n // p
        for i in range(2, nr // 2 + 1):
            if nr % i == 0:
                return False
        p = p // 10

    return True


def is_Prime(x):
    if x < 2:
        return False

    for i in range(2, x // 2 + 1):
        if x % i == 0:
            return False
    return True


def get_largest_prime_below(n):
    for i in range(n):
        if is_Prime(i):
            ultimul = i

    return ultimul


def test_get_largest_prime_below():
    assert get_largest_prime_below(19) == 17
    assert get_largest_prime_below(25) == 23


def test_is_palindrome():
    assert is_palindrome(1221) is True
    assert is_palindrome(1254) is False


def test_is_superprime():
    assert is_superprime(233) is True
    assert is_superprime(237) is False


def main() -> object:
    test_is_palindrome()
    test_is_superprime()
    while True:
        print("1.verifica daca un nr dat este palindrom")
        print("2.determina daca un nr este superprim")
        print("3.determina ulimul nr prim mai mic decat un nr citit")
        print("4.iesire")
        optiune = input("dati optiune:")

        if optiune == "1":
            numar1 = int(input("dati nr:"))
            print(is_palindrome(numar1))
        elif optiune == "2":
            numar2 = int(input("dati nr:"))
            print(is_superprime(numar2))

        elif optiune == "3":
            numar3 = int(input("dati nr:"))
            print(get_largest_prime_below(numar3))

        elif optiune == "4":
            break

        else:
            print("optiune gresita")


if __name__ == '__main__':
    main()
