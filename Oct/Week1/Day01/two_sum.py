# TWO SUM 
# pattern : One pass hashmap(notebook stores the number, position)

def twosum(nums, target) :
    notebook = {}
    for i in range(len(nums)) :
        complement = target - nums[i]  #for each number check if the complement(target - current) is already in the notebook. if yes, return both positions.
        if complement in notebook : 
            return[notebook[complement], i]
        notebook[nums[i]] = i  #if no, write current number in the notebook and move on.
    return[]

print(twosum([1, 5, 7, 2, 15],9))