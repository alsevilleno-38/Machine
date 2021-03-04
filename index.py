import numpy as np

def test():
    try:
        data = np.genfromtxt("data/data.txt", delimiter=",")
        data = data.astype("int64")    
        
        # print(data[data > 0])    
        # print(data.size)    
        # print(np.any(data > 50))
        print((data > 50) & (data < 100))
    except OSError as os_error:
        print("File does not exist")


def test1():
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    s = np.full(a.shape, True)
    s[0, 0] = False
    print(a[a > 1])


def test2():
    a = np.array(range(1, 31))
    a = a.reshape(6, 5)
    # print(a[[0, 4, 5]])
    print(a)
    print()
    # print(a[[0, 4, 5], [0, 2, 3]])
    # print()
    # print(a[[0, 4, 5], 0:2])
    print(a[[0, 1, 2, 3], [1, 2, 3, 4]])
# test2()

def test3():
    j=np.arange(20,dtype=np.int)
    site=np.ones((20,200),dtype=np.int)
    sumkma=np.ones((100,20))
    # print(site[j])
    print(j)
    # print(j.shape)
    # print(np.newaxis)
    # print(j[:,1].shape)

    # [sumkma[site[x],x] for x in range(20)]

    # sumkma[site[j],j]

def test4():
    # x = np.array([[ 0,  1,  2],
    #           [ 3,  4,  5],
    #           [ 6,  7,  8],
    #           [ 9, 10, 11]])
    a = np.array(range(1, 31))
    a = a.reshape(6, 5)

    print(a)
    print()

    rows = np.array([[0, 1],
                 [0, 1]], dtype=np.intp)

    columns = np.array([[2, 4],
                    [2, 4]], dtype=np.intp)                    
    print(a[])  

    # print(rows)
# test2()
test4()