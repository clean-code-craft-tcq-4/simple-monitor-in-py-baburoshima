MIN_TEMP_LIMIT = 0
MAX_TEMP_LIMIT = 45
MIN_SOC_LIMIT = 20
MAX_SOC_LIMIT = 80
CHARGE_RATE_LIMIT = 0.8

def battery_is_ok(temperature, soc, charge_rate):
  return temp_check(temperature) and soc_check(soc) and charge_rate_check(charge_rate)

def temp_check(temperature):
  if temperature < MIN_TEMP_LIMIT or temperature > MAX_TEMP_LIMIT:
    print('Temperature is out of range!')
    return False
  return True

def soc_check(soc):
  if soc < MIN_SOC_LIMIT or soc > MAX_SOC_LIMIT:
    print('State of Charge is out of range!')
    return False
  return True

def charge_rate_check(charge_rate):
  if charge_rate > CHARGE_RATE_LIMIT:
    print('Charge rate is out of range!')
    return False
  return True

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)

  #temparature limit tests
  assert(battery_is_ok(0, 70, 0.7) is True)
  assert(battery_is_ok(45, 70, 0.7) is True)
  assert(battery_is_ok(46, 70, 0.7) is False)
  assert(battery_is_ok(-1, 70, 0.7) is False)
  #soc limit tests
  assert(battery_is_ok(40, 20, 0.5) is True)
  assert(battery_is_ok(40, 80, 0.5) is True)
  assert(battery_is_ok(40, 19, 0.5) is False)
  assert(battery_is_ok(40, 81, 0.5) is False)
  #charge rate tests
  assert(battery_is_ok(40, 25, 0.7) is True)
  assert(battery_is_ok(40, 25, 0.8) is True)
  assert(battery_is_ok(40, 25, 0.9) is False)