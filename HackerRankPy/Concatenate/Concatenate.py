import numpy as np

def main():
    # Solicitar valores de N, M y P
    N, M, P = map(int, input().split())
    
    # Solicitar los valores del array_1
    array_1 = []
    for _ in range(N):
        row = list(map(int, input().split()))
        array_1.append(row)
    array_1 = np.array(array_1)
    
    # Solicitar los valores del array_2
    array_2 = []
    for _ in range(M):
        row = list(map(int, input().split()))
        array_2.append(row)
    array_2 = np.array(array_2)
    
    # Concatenar los arrays a lo largo del eje 0
    result = np.concatenate((array_1, array_2), axis=0)
    print(result)

if __name__ == "__main__":
    main()
