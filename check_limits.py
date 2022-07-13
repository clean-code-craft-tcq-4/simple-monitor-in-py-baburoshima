import limits_definition as limits
import test_check_limits as test
import Display_messages as messages

def battery_is_ok(parameters,Language):
  parameters = parameters + limits.Parameter_name #append name of parameters
  battery_status = Is_batteryparams_lowlimit_ok(parameters,Language) and Is_batteryparams_highlimit_ok(parameters,Language)
  return battery_status

def Is_batteryparams_lowwarninglimit_ok(parameters,Language):
  for item in range(limits.Parameter_count):
    if parameters[item] <= limits.Low_warning_values[item]:
      messages.Warning_Message(parameters[item+limits.Parameter_count],Language,limits.LOW)
      return False
  return True

def Is_batteryparams_lowlimit_ok(parameters,Language):
  for item in range(limits.Parameter_count):
    if parameters[item] <= limits.Low_Breach_values[item]:
      messages.Breach_Message(parameters[item+limits.Parameter_count],Language,limits.LOW)
      return False
  Is_batteryparams_lowwarninglimit_ok(parameters,Language)
  return True

def Is_batteryparams_highlimit_ok(parameters,Language):
  for item in range(limits.Parameter_count):
    if parameters[item] >= limits.High_Breach_values[item]:
      messages.Breach_Message(parameters[item+limits.Parameter_count],Language,limits.HIGH)
      return False
  Is_batteryparams_highwarninglimit_ok(parameters,Language)
  return True

def Is_batteryparams_highwarninglimit_ok(parameters,Language):
  for item in range(limits.Parameter_count):
    if parameters[item] >= limits.High_Warning_values[item]:
      messages.Warning_Message(parameters[item+limits.Parameter_count],Language,limits.HIGH)
      return False
  return True

if __name__ == '__main__':
  test.check_limits_test()
