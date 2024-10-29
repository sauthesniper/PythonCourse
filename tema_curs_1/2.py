finalXOR=0
def generate_subsets(arr, index=0, current_subset=[]):
    global finalXOR #utilizeaza variabila globala
    iterationXOR=0
    for a in current_subset:
        iterationXOR=a^iterationXOR
        # face xor cu toate elementele dintr-o submultime

    finalXOR=finalXOR^iterationXOR
    # face xor cu celelalte submultimi xor-ate.
    
    for i in range(index, len(arr)):
        current_subset.append(arr[i])
        generate_subsets(arr, i + 1, current_subset)
        current_subset.pop()

# Exemplu de utilizare
arr = [2, 7, 18]
generate_subsets(arr)
print(f"XOR FINAL : {finalXOR}");