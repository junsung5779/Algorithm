
# Hoare-Partition 알고리즘
def partition(A[], l,r):
    p  = A[l]
    i,j = l,r
    while i<=j:
        while A[i] <= p:
            i++
        while A[j] >= p:
            j--
        if i < j:
            swap(A[i],A[j])
    swap(A[l],A[j])
    return j