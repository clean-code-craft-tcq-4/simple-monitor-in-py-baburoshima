import limits_definition as limits
import test_check_limits as test

def battery_is_ok(temperature, soc, charge_rate):
  return temp_check(temperature) and soc_check(soc) and charge_rate_check(charge_rate)

def temp_check(temperature):
  if temperature not in range(limits.MIN_TEMP, limits.MAX_TEMP):
    print('Temperature is out of range!')
    return False
  return True

def soc_check(soc):
  if soc not in range(limits.MIN_SOC,limits.MAX_SOC):
    print('State of Charge is out of range!')
    return False
  return True

def charge_rate_check(charge_rate):
  if charge_rate > limits.CHARGE_RATE:
    print('Charge rate is out of range!')
    return False
  return True

if __name__ == '__main__':
  test.check_limits_test()