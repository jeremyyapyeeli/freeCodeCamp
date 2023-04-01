import numpy as np

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
