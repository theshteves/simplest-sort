def simplest_sort():
    '''
    "Is this the simplest (and most surprising) sorting algorithm ever?"
    -- Stanley P. Y. Fung, https://arxiv.org/abs/2110.01111
    '''

    N = len(data)
    for i in range(N):
        for j in range(i + 1, N):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]


if __name__ == '__main__':
    import random
    data = list(range(32))
    random.shuffle(data)
    print(f'Shuffled Input: {data}')

    simplest_sort(data)
    print(f'Sorted Output:  {data}')

