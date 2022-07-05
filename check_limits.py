import limits_definition as limits
import test_check_limits as test

def battery_is_ok(parameters):
  parameters = parameters + limits.Parameter_name #append name of parameters
  return Is_batteryparams_minlimit_ok(parameters) and Is_batteryparams_maxlimit_ok(parameters)

def Is_batteryparams_minlimit_ok(parameters):
  for item in range(limits.Parameter_count):
    if parameters[item] <= limits.min_values[item]:
      print("FAIL :"+ parameters[item+limits.Parameter_count] + " less than min range!" )
      return False
  print("All parameters above min range")
  return True

def Is_batteryparams_maxlimit_ok(parameters):
  for item in range(limits.Parameter_count):
    if parameters[item] >= limits.max_values[item]:
      print("FAIL :"+ parameters[item+limits.Parameter_count] + " Greater than Max range!")
      return False 
  print("All parameters with max range")
  return True

if __name__ == '__main__':
  test.check_limits_test()