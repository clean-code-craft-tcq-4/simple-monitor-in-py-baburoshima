Parameter_count = 3 
Parameter_name =  ("Temparature","SOC","Charge Rate")
LOW = 0
HIGH = 1

#Extension 1: Early Warning
# Introducing a 'warning' level with a tolerance of 5% of the upper-limit.
# Temparature : 5% of 45 = 2.25
# SOC  : 5% of 80 = 4
# Charge rate : 5% of 0.8 = 0.04
MIN_TEMP = 0
MAX_TEMP = 45
MIN_SOC = 20
MAX_SOC = 80
MIN_CHARGE_RATE = 0.1 #assumption
MAX_CHARGE_RATE = 0.8
MIN_WARNING_TEMP = 2.25 
MIN_WARNING_SOC = 24 
MIN_WARNING_CHARGE_RATE = 0.14
MAX_WARNING_TEMP = 42.75
MAX_WARNING_SOC = 76
MAX_WARNING_CHARGE_RATE = 0.76
Low_Breach_values = MIN_TEMP, MIN_SOC , MIN_CHARGE_RATE
Low_warning_values = MIN_WARNING_TEMP, MIN_WARNING_SOC , MIN_WARNING_CHARGE_RATE
High_Warning_values = MAX_WARNING_TEMP, MAX_WARNING_SOC, MAX_WARNING_CHARGE_RATE
High_Breach_values = MAX_TEMP, MAX_SOC , MAX_CHARGE_RATE
