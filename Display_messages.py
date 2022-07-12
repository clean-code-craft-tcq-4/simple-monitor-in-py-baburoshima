import Display_message_definitions as definitions

def Warning_Message(parameter,Language,Violationtype):
  Warning_Message = definitions.TestStatus_message[Language][0] + " " + parameter  + " " + definitions.Warning_message[Language][1] if Violationtype else definitions.TestStatus_message[Language][0] + " " + parameter  + " "+ definitions.Warning_message[Language][0]
  print (Warning_Message)

def Breach_Message(parameter,Language,Violationtype):
  Breach_Message = definitions.TestStatus_message[Language][1] + " " +parameter  + " " + definitions.Breach_message[Language][1] if Violationtype else definitions.TestStatus_message[Language][1] + " " + parameter  + " " + definitions.Breach_message[Language][0]
  print(Breach_Message)
