def i_cant_believe_it_can_sort(data: list) -> None:
    '''
    "Is this the simplest (and most surprising) sorting algorithm ever?"
    -- Stanley P. Y. Fung, https://arxiv.org/abs/2110.01111 (Algorithm 1)
    '''

    N = len(data)
    for i in range(N):
        for j in range(N):
            if data[i] < data[j]:
                data[i], data[j] = data[j], data[i]


def exchange_sort(data: list) -> None:
    '''
    Exchange Sort (Algorithm 2 from same paper)
    -- Stanley P. Y. Fung, https://arxiv.org/abs/2110.01111
    '''

    N = len(data)
    for i in range(N):
        for j in range(i + 1, N):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]


def i_cant_believe_it_can_sort_improved(data: list) -> None:
    '''
    Algorithm 3, "improved" version of
    "Is this the simplest (and most surprising) sorting algorithm ever?"
    -- Stanley P. Y. Fung, https://arxiv.org/abs/2110.01111
    '''

    N = len(data)
    for i in range(1, N):
        for j in range(i):
            if data[i] < data[j]:
                data[i], data[j] = data[j], data[i]


if __name__ == '__main__':
    import random
    data = list(range(32))
    random.shuffle(data)
    print(f'Shuffled Input: {data}')

    simplest_sort(data)
    print(f'Sorted Output:  {data}')

