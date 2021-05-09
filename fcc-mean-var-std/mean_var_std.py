import numpy as np

def calculate(list):
  
  # Checking for the length of the list 
  if len(list) == 9:
    list = np.reshape(list, (3,3))
  else:
    raise ValueError("List must contain nine numbers.")

  # Empty Dictionary
  calculations = {}

  # Getting all the elements row-wise and column wise
  vertical = [[list[i][j] for i in range(3)] for j in range(3)]
  horizontal = [[list[j][i] for i in range(3)] for j in range(3)]

  # Uncomment these two lines to see the output
  # print(vertical)
  # print(horizontal)

  # Mean row-wise, column-wise and after flattening
  vertical_mean = [np.mean(i) for i in vertical]
  horizontal_mean = [np.mean(i) for i in horizontal]
  flatten_mean = np.mean(list.flatten())

  # Variance row-wise, column-wise and after flattening
  vertical_variance = [np.var(i) for i in vertical]
  horizontal_variance = [np.var(i) for i in horizontal]
  flatten_variance = np.var(list.flatten())

  # Standard Deviation row-wise, column-wise and after flattening
  vertical_std = [np.std(i) for i in vertical]
  horizontal_std = [np.std(i) for i in horizontal]
  flatten_std = np.std(list.flatten())

  # Maximum Value row-wise, column-wise and after flattening
  vertical_max = [np.max(i) for i in vertical]
  horizontal_max = [np.max(i) for i in horizontal]
  flatten_max = np.max(list.flatten())

  # Minimum Value row-wise, column-wise and after flattening
  vertical_min = [np.min(i) for i in vertical]
  horizontal_min = [np.min(i) for i in horizontal]
  flatten_min = np.min(list.flatten())

  # Sum row-wise, column-wise and after flattening
  vertical_sum = [np.sum(i) for i in vertical]
  horizontal_sum = [np.sum(i) for i in horizontal]
  flatten_sum = np.sum(list.flatten())

  # Adding it all to the dictionary using keys-values pair
  calculations["mean"] = [vertical_mean, horizontal_mean, flatten_mean]
  calculations["variance"] = [vertical_variance, horizontal_variance, flatten_variance]
  calculations["standard deviation"] = [vertical_std, horizontal_std, flatten_std]
  calculations["max"] = [vertical_max, horizontal_max, flatten_max]
  calculations["min"] = [vertical_min, horizontal_min, flatten_min]
  calculations["sum"] = [vertical_sum, horizontal_sum, flatten_sum]

  return calculations