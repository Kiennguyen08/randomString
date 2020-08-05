import random 

def randomize (arr, n): 
    for i in range(n-1,1,-1): 
        j = random.randint(1,i) 
        arr[i],arr[j] = arr[j],arr[i] 
    return arr 


def main(text):
    smallText = text.split(' ')
    res = ''
    for arr in smallText:
        arr1 = list(arr)
        n = len(arr1) 
        if('.' in arr1 or ',' in arr1):
            temp = ''.join(randomize(arr1, n-1))
        else:
            temp = ''.join(randomize(arr1, n))
        res += temp + ' '
    return res
if __name__ == "__main__":
    main(text)
  