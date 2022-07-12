import limits_definition as limits
import test_check_limits as test

def battery_is_ok(parameters,Language):
  parameters = parameters + limits.Parameter_name #append name of parameters
  battery_status = Is_batteryparams_lowlimit_ok(parameters,Language) and Is_batteryparams_highlimit_ok(parameters,Language)
  return battery_status

def Is_batteryparams_lowwarninglimit_ok(parameters,Language):
  for item in range(limits.Parameter_count):
    if parameters[item] <= limits.Low_warning_values[item]:
      LowWarning_Message(parameters[item+limits.Parameter_count],item ,Language)
      return False
  return True

def Is_batteryparams_lowlimit_ok(parameters,Language):
  for item in range(limits.Parameter_count):
    if parameters[item] <= limits.Low_Breach_values[item]:
      LowBreach_Message(parameters[item+limits.Parameter_count],item,Language)
      return False
  Is_batteryparams_lowwarninglimit_ok(parameters,Language)
  return True

def Is_batteryparams_highlimit_ok(parameters,Language):
  for item in range(limits.Parameter_count):
    if parameters[item] >= limits.High_Breach_values[item]:
      HighBreach_Message(parameters[item+limits.Parameter_count] ,item,Language)
      return False
  Is_batteryparams_highwarninglimit_ok(parameters,Language)
  return True

def Is_batteryparams_highwarninglimit_ok(parameters,Language):
  for item in range(limits.Parameter_count):
    if parameters[item] >= limits.High_Warning_values[item]:
      HighWarning_Message(parameters[item+limits.Parameter_count],item,Language)
      return False
  return True

def HighWarning_Message(parameter,item,Language):
  if Language == "ENG":
    print("Warning :"+ parameter + " Approaching Max range!")
  if Language == "GERMAN":
    parameter = limits.Parameter_name_inGerman[item]
    print("Warnung :"+ parameter + " Annäherung an die maximale Reichweite!")


def LowWarning_Message(parameter,item,Language):
  if Language == "ENG":
    print("Warning :"+ parameter + " Approaching Min range!")
  if Language == "GERMAN":
    parameter = limits.Parameter_name_inGerman[item]
    print("Warnung :"+ parameter + " Nähert sich der Mindestreichweite!")


def HighBreach_Message(parameter,item,Language):
  if Language == "ENG":
    print("FAIL :"+ parameter + "  greater than Max range!")
  if Language == "GERMAN":
    parameter = limits.Parameter_name_inGerman[item]
    print("SCHEITERN :"+ parameter + " größer als die maximale Reichweite!")

def LowBreach_Message(parameter,item,Language):
  if Language == "ENG":
    print("FAIL :"+ parameter + " less than Min range!")
  if Language == "GERMAN":
    parameter = limits.Parameter_name_inGerman[item]
    print("SCHEITERN :"+ parameter + " weniger als Min-Bereich!")



if __name__ == '__main__':
  test.check_limits_test()
