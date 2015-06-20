__author__ = 'Siuxoes'

def count_inversion(sequence):
    return sum([1
                for i in range(len(sequence) - 1, -1, -1)
                for j in range(i - 1, -1, -1)
                if sequence[i] < sequence[j]])

print(count_inversion((1,2,5,3,4,7,6)))