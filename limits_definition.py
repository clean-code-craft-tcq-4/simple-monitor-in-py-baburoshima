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
TOLERANCE = 0.05
Low_Breach_values = MIN_TEMP, MIN_SOC , MIN_CHARGE_RATE
Low_warning_values = MIN_TEMP + TOLERANCE*MAX_TEMP, MIN_SOC  + TOLERANCE*MAX_SOC , MIN_CHARGE_RATE + TOLERANCE*MAX_CHARGE_RATE
High_Warning_values = MAX_TEMP - TOLERANCE*MAX_TEMP, MAX_SOC - TOLERANCE*MAX_SOC , MAX_CHARGE_RATE - TOLERANCE*MAX_CHARGE_RATE
High_Breach_values = MAX_TEMP, MAX_SOC , MAX_CHARGE_RATE
