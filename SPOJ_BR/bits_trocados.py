def count(n):
    i, j, k , l = 0, 0, 0, 0
    if n >= 50:
        i = n // 50
        n = n % 50
    if n >= 10:
        j = n // 10
        n = n % 10
    if n >= 5:
        k = n // 5
        n = n % 5
    if n >= 1:
        l = n // 1
    print(i, j, k, l)
        
def main():
    amounts = []
    n = int(input())
    while n > 0:
        amounts.append(n)
        n = int(input())
    for z in amounts:
        print("Teste "+str(amounts.index(z)+1))
        count(z)

    return 0

if __name__ == '__main__': 
    main()
