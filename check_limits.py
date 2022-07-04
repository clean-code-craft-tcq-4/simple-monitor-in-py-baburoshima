import limits_definition as limits
import test_check_limits as test

def battery_is_ok(temperature, soc, charge_rate):
  return IsTemp_ok(temperature) and IsSoc_ok(soc) and IsCharge_rate_ok(charge_rate)

def IsTemp_ok(temperature):
  if temperature not in range(limits.MIN_TEMP, limits.MAX_TEMP+1): # added 1 at end to include MAX value
    if(temperature < limits.MIN_TEMP):
      print('Temperature less than min range!')
    else:
       print('Temperature greater than Max range!')
    return False
  print('Temperature is in range!')
  return True

def IsSoc_ok(soc):
  if soc not in range(limits.MIN_SOC,limits.MAX_SOC+1): # added 1 at end to include MAX value
    if(soc < limits.MIN_SOC):
      print('State of Charge less than min range!')
    else:
       print('State of Charge greater than Max range!')
    return False
  print('State of Charge is in range!')
  return True

def IsCharge_rate_ok(charge_rate):
  if charge_rate > limits.MAX_CHARGE_RATE:
    print('Charge rate is greater than Max range!')
    return False
  print('Charge rate is in range!')

  return True

if __name__ == '__main__':
  test.check_limits_test()