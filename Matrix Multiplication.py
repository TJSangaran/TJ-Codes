def read_matrix(n,m,nam):
    matrix=[]
    print("Enter Matrix %s:"%(nam))
    for _ in range(n):
        try:
            row=list(map(int,input().split()))
        except ValueError:
            print('Error')
            return False
        else:
            if len(row)==m:
                matrix.append(row)
            else:
                print('Invalid Matrix')
                return False
    return matrix
def matrix_product(n,m,matX,matY):
    for i in range (n):
        for j in range (n):
            t=0
            for k in range(m):
                t+=matX[i][k]*matY[j][k]
            print(t,end=' ')
        print()
n,m=map(int,input('Enter the dimension: ').split(','))
matA=read_matrix(n,m,'A')
if matA:
    matB=read_matrix(n,m,'B')
if matA and matB:
    matrix_product(n,m,matA,matB)

