

def plusMinus(arr):
    print(arr)
    len_arr=len(arr)
    print("length::",len_arr)
    tot_pos=0
    tot_neg=0
    tot_zeros=0
    print(sum((tot_pos+1,tot_neg+1) for i in range(len(arr)) if arr[i]>0  for j in range(len(arr)) if arr[j]<0 ))


if __name__=="__main__":
    arr=[-4,3,-9,0,4,1]
    plusMinus(arr)