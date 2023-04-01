# Project Introduction

This project requires you to create a function named `calculate()` that will take in a list of exactly 9 elements, covert it into a 3x3 NumPy array, and return a dictionary of `{'mean', 'variance', 'standard deviation', 'max', 'min', 'sum'}` along both axes and for the flattened matrix. If the list contains any other number of elements apart from 9, it should raise a `ValueError` exception with the message: "List must contain nine numbers". The values in the returned dictionary should be lists and not NumPy arrays.

## Sample Input and Output

### Input:
`calculate([0,1,2,3,4,5,6,7,8])` 

### Output:
```
{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
  'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
  'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]
}
```

## Solution Walkthrough
### 1. Error Handling for lists not having exactly 9 elements
```
if len(list) != 9:
    raise ValueError("List must contain nine numbers.")
```
`len(list)` checks for the number of elements in the list. If this list does not have exactly 9 elements, a `ValueError` exception is raised and the flow will be exited.

### 2. Converting the list into a 3x3 matrix
```
df_list = np.array(list).reshape(3, 3)
```

### 3. Creating a `calculations` dictionary as the function output
```
calculations = {}
```

### 4. Calculating the statistics of the 3x3 matrix along both axes and flattened matrix
```
calculations['mean'] = [
    df_list.mean(axis=0).tolist(),
    df_list.mean(axis=1).tolist(),
    df_list.mean()
  ]
  
  calculations['variance'] = [
    df_list.var(axis=0).tolist(),
    df_list.var(axis=1).tolist(),
    df_list.var()
  ]
  
  calculations['standard deviation'] = [
    df_list.std(axis=0).tolist(),
    df_list.std(axis=1).tolist(),
    df_list.std()
  ]
  
  calculations['max'] = [
    df_list.max(axis=0).tolist(),
    df_list.max(axis=1).tolist(),
    df_list.max()
  ]
  
  calculations['min'] = [
    df_list.min(axis=0).tolist(),
    df_list.min(axis=1).tolist(),
    df_list.min()
  ]
  
  calculations['sum'] = [
    df_list.sum(axis=0).tolist(),
    df_list.sum(axis=1).tolist(),
    df_list.sum()
  ]
```

### 5. Returning the `calculations` dictionary as output
```
return calculations
```

## Full Code
```
def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")

  df_list = np.array(list).reshape(3, 3)

  calculations = {}

  calculations['mean'] = [
    df_list.mean(axis=0).tolist(),
    df_list.mean(axis=1).tolist(),
    df_list.mean()
  ]
  
  calculations['variance'] = [
    df_list.var(axis=0).tolist(),
    df_list.var(axis=1).tolist(),
    df_list.var()
  ]
  
  calculations['standard deviation'] = [
    df_list.std(axis=0).tolist(),
    df_list.std(axis=1).tolist(),
    df_list.std()
  ]
  
  calculations['max'] = [
    df_list.max(axis=0).tolist(),
    df_list.max(axis=1).tolist(),
    df_list.max()
  ]
  
  calculations['min'] = [
    df_list.min(axis=0).tolist(),
    df_list.min(axis=1).tolist(),
    df_list.min()
  ]
  
  calculations['sum'] = [
    df_list.sum(axis=0).tolist(),
    df_list.sum(axis=1).tolist(),
    df_list.sum()
  ]

  return calculations
```

