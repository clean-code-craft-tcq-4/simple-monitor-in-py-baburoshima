import check_limits
import numpy as np

def check_limits_test():
  #initial test cases provided
   # assert(check_limits.battery_is_ok((25, 70, 0.7),"ENG") is True)
   # print("-------------------------------")
   # assert(check_limits.battery_is_ok((50, 85, 0),"ENG") is False)
   # print("-------------------------------")
#SOC	      Temperature	    Charge Rate	
#0 to 20	  -1 to 0	        0 to 0.1	    LOW_BREACH
#21 to 24	  0.1 to 2.25	    0.11 to 0.14	LOW__WARNING
#24 to 75	  2.26 to 42.75   0.15 to 0.75	NORMAL
#76 to 80	  42.76 to 44.75  0.76 to 0.79	HIGH_WARNING
#81 to 100	45 to 50	      0.8 to 1	    HIGH_BREACH

#temparature limit tests
  for temparature in np.arange(-1,0.1,0.5):
    print(" test for Temparature : {:.2f}".format(temparature))
    assert(check_limits.battery_is_ok((temparature, 70, 0.7),"ENG") is False) # low breach 
    print("-------------------------------")
  for temparature in np.arange (0.1,2.25,1):
    print(" test for Temparature : {:.2f}".format(temparature))
    assert(check_limits.battery_is_ok((temparature, 70, 0.7),"GERMAN") is True) # low warning
    print("-------------------------------")
  for temparature in np.arange (2.26,42.75,10.25):
    print(" test for Temparature : {:.2f}".format(temparature))
    assert(check_limits.battery_is_ok((temparature, 70, 0.7),"ENG") is True) # normal
    print("-------------------------------")
  for temparature in np.arange (42.76,44.75,0.5): 
    print(" test for Temparature : {:.2f}".format(temparature))
    assert(check_limits.battery_is_ok((temparature, 70, 0.7),"GERMAN") is True) # high warning
    print("-------------------------------")
  for temparature in np.arange (45,50,1.5):
    print(" test for Temparature : {:.2f}".format(temparature))
    assert(check_limits.battery_is_ok((temparature, 70, 0.7),"ENG") is False) # high breach
    print("-------------------------------")

#SOC limit tests
  for SOC in np.arange(0,20,5):
    print(" test for SOC : {:.2f}".format(SOC))
    assert(check_limits.battery_is_ok((40, SOC, 0.7),"GERMAN") is False) # low breach 
    print("-------------------------------")
  for SOC in np.arange (21,24.1):
    print(" test for SOC : {:.2f}".format(SOC)) 
    assert(check_limits.battery_is_ok((40, SOC, 0.7),"ENG") is True) # low warning
    print("-------------------------------")
  for SOC in np.arange (25,75,15): 
    print(" test for SOC : {:.2f}".format(SOC))
    assert(check_limits.battery_is_ok((40, SOC, 0.7),"GERMAN") is True) # normal
    print("-------------------------------")
  for SOC in np.arange (76,80,1): 
    print(" test for SOC : {:.2f}".format(SOC))
    assert(check_limits.battery_is_ok((40, SOC, 0.7),"ENG") is True) # high warning
    print("-------------------------------")
  for SOC in np.arange (81,100,5):
    print(" test for SOC : {:.2f}".format(SOC)) 
    assert(check_limits.battery_is_ok((40, SOC, 0.7),"GERMAN") is False) # high breach
    print("-------------------------------")


#charge rate limit tests
  for ChargeRate in np.arange(0,0.1,0.05):
    print(" test for ChargeRate : {:.2f}".format(ChargeRate))
    assert(check_limits.battery_is_ok((25, 70, ChargeRate),"ENG") is False) # low breach 
    print("-------------------------------")
  for ChargeRate in np.arange (0.11,0.14,0.01): 
    print(" test for ChargeRate : {:.2f}".format(ChargeRate))
    assert(check_limits.battery_is_ok((25, 70, ChargeRate),"GERMAN") is True) # low warning
    print("-------------------------------")
  for ChargeRate in np.arange (0.15,0.75,0.25): 
    print(" test for ChargeRate : {:.2f}".format(ChargeRate))
    assert(check_limits.battery_is_ok((25, 70, ChargeRate),"ENG") is True) # normal
    print("-------------------------------")
  for ChargeRate in np.arange (0.76,0.79,0.01): 
    print(" test for ChargeRate : {:.2f}".format(ChargeRate))
    assert(check_limits.battery_is_ok((25, 70, ChargeRate),"GERMAN") is True) # high warning
    print("-------------------------------")
  for ChargeRate in np.arange (0.8,1,0.1): 
    print(" test for ChargeRate : {:.2f}".format(ChargeRate))
    assert(check_limits.battery_is_ok((25, 70, ChargeRate),"ENG") is False) # high breach
    print("-------------------------------")

