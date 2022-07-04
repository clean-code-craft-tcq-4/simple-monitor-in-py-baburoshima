import limits_definition as limits
import test_check_limits as test

def battery_is_ok(parameters):
  parameters = parameters + limits.Parameter_list
  batter_params_check_minlimit(parameters)
  batter_params_check_maxlimit(parameters)
  return batter_params_check_maxlimit(parameters) and batter_params_check_minlimit(parameters)

def batter_params_check_minlimit(parameters):
  for item in range(limits.Parameter_count):
    if parameters[item] < limits.min_values[item]:
      print(parameters[item+limits.Parameter_count] + " less than min range!" )
      return False
  return True

def batter_params_check_maxlimit(parameters):
  for item in range(limits.Parameter_count):
    if parameters[item] > limits.max_values[item]:
      print(parameters[item+limits.Parameter_count] + " Greater than Max range!")
      return False 
  return True

if __name__ == '__main__':
  test.check_limits_test()