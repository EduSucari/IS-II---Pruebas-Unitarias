def bubble_sort(vet):
    n = len(vet)

    for i in range(n - 1, 0, -1):
        for j in range(i):
            if vet[j] > vet[j + 1]:
                aux = vet[j]
                vet[j] = vet[j + 1]
                vet[j + 1] = aux