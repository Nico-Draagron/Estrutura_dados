# Soma de Dois (Two Sum): Dado um array de números inteiros e um 
# valor alvo, retorne os índices dos dois números que somados resultam no alvo.
# Dica: Tente resolver com apenas um "passo" pelo array (O(n)).

def two_sum(nums, target):
    num_to_index = {}
    for i, num in enumerate (nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return None

input_array = [2,3, 7, 11, 15]
target_value = 9
result = two_sum(input_array, target_value)
if result:
    print(f'Índices encontrados: {result}')
else:    
    print("Nenhuma combinação encontrada.")