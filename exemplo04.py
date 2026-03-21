# Remover Duplicatas: Dado um array ordenado, remova os elementos duplicados "in-place" 
# (sem criar um novo array), de modo que cada elemento apareça apenas uma vez.

def remove_duplicates(nums):
    if not nums:
        return 0
    
    unique_index = 0
    for i in range(1, len(nums)):
        if nums[i] != nums [unique_index]:
            unique_index +=1
            nums[unique_index] = nums[i]
    return unique_index + 1

input_array = [1, 1, 2, 3, 3, 4, 5, 5]
new_length = remove_duplicates(input_array)
print(f'Novo comprimento do array sem duplicatas: {new_length}')
print(f'Array modificado: {input_array[:new_length]}')
