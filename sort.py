import utils

def merge_sort(arr):
  # Vendo se chegamos ao final da recursão
    if len(arr) > 1:
        mid = len(arr)//2

        # Dividindo na metade
        left = arr[:mid]
        right = arr[mid:]

        # Executando o sort nas metades
        merge_sort(left)  
        merge_sort(right)
  
        i = j = k = 0
  
        # Efetuando o sort
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
  
        # Adicionando os elementos que já foram sorteados
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
  
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
def merge_sort_words(arr):
  # Vendo se chegamos ao final da recursão
    if len(arr) > 1:
        mid = len(arr)//2

        # Dividindo na metade
        left = arr[:mid]
        right = arr[mid:]

        # Executando o sort nas metades
        merge_sort(left)  
        merge_sort(right)
  
        i = j = k = 0
  
        # Efetuando o sort (merge)
        while i < len(left) and j < len(right):
            leftChars = utils.chars_to_number(utils.get_chars(left[i]))
            rightChars = utils.chars_to_number(utils.get_chars(right[j]))
            leftChar = leftChars[0]
            rightChar = rightChars[0]

            if leftChars != rightChars:
                x = y = 0

                while leftChar == rightChar:
                    x+=1
                    y+=1
                    leftChar = leftChars[x]
                    rightChar = rightChars[y]


            if leftChar <= rightChar:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
  
        # Adicionando os elementos que já foram sorteados
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
  
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
