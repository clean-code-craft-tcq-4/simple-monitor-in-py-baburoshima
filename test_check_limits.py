import check_limits

def check_limits_test():
  #initial test cases provided
   assert(check_limits.battery_is_ok((25, 70, 0.7),"ENG") is True)
   print("-------------------------------")
   assert(check_limits.battery_is_ok((50, 85, 0),"ENG") is False)
   print("-------------------------------")
#SOC	      Temperature	    Charge Rate	
#0 to 20	  -1 to 0	        0 to 0.1	    LOW_BREACH
#21 to 24	  0.1 to 2.25	    0.11 to 0.14	LOW__WARNING
#24 to 75	  2.26 to 42.75   0.15 to 0.75	NORMAL
#76 to 80	  42.76 to 44.75  0.76 to 0.79	HIGH_WARNING
#81 to 100	45 to 50	      0.8 to 1	    HIGH_BREACH

#temparature limit tests
assert(check_limits.battery_is_ok((-1, 70, 0.7),"ENG") is False) # low breach 
print("-------------------------------")
assert(check_limits.battery_is_ok((0, 70, 0.7),"GERMAN") is False) # low breach 
print("-------------------------------")
assert(check_limits.battery_is_ok((0.1, 70, 0.7),"ENG") is True) # low warning
print("-------------------------------")
assert(check_limits.battery_is_ok((2.25, 70, 0.7),"GERMAN") is True) # low warning
print("-------------------------------")
assert(check_limits.battery_is_ok((2.26, 70, 0.7),"ENG") is True) # normal
print("-------------------------------")
assert(check_limits.battery_is_ok((42.75, 70, 0.7),"GERMAN") is True) # normal
print("-------------------------------")
assert(check_limits.battery_is_ok((42.76, 70, 0.7),"ENG") is True) # high warning
print("-------------------------------")
assert(check_limits.battery_is_ok((44.75, 70, 0.7),"GERMAN") is True) # high warning
print("-------------------------------")
assert(check_limits.battery_is_ok((45, 70, 0.7),"ENG") is False) #  high breach
print("-------------------------------")
assert(check_limits.battery_is_ok((50, 70, 0.7),"GERMAN") is False) #  high breach
print("-------------------------------")


#SOC limit tests
assert(check_limits.battery_is_ok((40, 0, 0.7),"ENG") is False) # low breach 
print("-------------------------------")
assert(check_limits.battery_is_ok((40, 20, 0.7),"GERMAN") is False) # low breach 
print("-------------------------------")
assert(check_limits.battery_is_ok((40, 21, 0.7),"ENG") is True) # low warning
print("-------------------------------")
assert(check_limits.battery_is_ok((40, 24, 0.7),"GERMAN") is True) # low warning
print("-------------------------------")
assert(check_limits.battery_is_ok((40, 25, 0.7),"ENG") is True) # normal
print("-------------------------------")
assert(check_limits.battery_is_ok((40, 75, 0.7),"GERMAN") is True) # normal
print("-------------------------------")
assert(check_limits.battery_is_ok((40, 76, 0.7),"ENG") is True) # high warning
print("-------------------------------")
assert(check_limits.battery_is_ok((40, 79, 0.7),"GERMAN") is True) # high warning
print("-------------------------------")
assert(check_limits.battery_is_ok((40, 80, 0.7),"ENG") is False) #  high breach
print("-------------------------------")
assert(check_limits.battery_is_ok((40, 81, 0.7),"GERMAN") is False) #  high breach
print("-------------------------------")
 


#charge rate limit tests
assert(check_limits.battery_is_ok((40, 70, 0),"ENG") is False) # low breach 
print("-------------------------------")
assert(check_limits.battery_is_ok((40, 70, 0.1),"GERMAN") is False) # low breach 
print("-------------------------------")
assert(check_limits.battery_is_ok((40, 70, 0.11),"ENG") is True) # low warning
print("-------------------------------")
assert(check_limits.battery_is_ok((40, 70, 0.14),"GERMAN") is True) # low warning
print("-------------------------------")
assert(check_limits.battery_is_ok((40, 70, 0.15),"ENG") is True) # normal
print("-------------------------------")
assert(check_limits.battery_is_ok((40, 70, 0.75),"GERMAN") is True) # normal
print("-------------------------------")
assert(check_limits.battery_is_ok((40, 70, 0.76),"ENG") is True) # high warning
print("-------------------------------")
assert(check_limits.battery_is_ok((40, 70, 0.79),"GERMAN") is True) # high warning
print("-------------------------------")
assert(check_limits.battery_is_ok((40, 70, 0.8),"ENG") is False) #  high breach
print("-------------------------------")
assert(check_limits.battery_is_ok((40, 70, 1),"GERMAN") is False) #  high breach
print("-------------------------------")

