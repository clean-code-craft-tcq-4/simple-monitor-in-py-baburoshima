import check_limits

def check_limits_test():
    assert(check_limits.battery_is_ok(25, 70, 0.7) is True)
    print("-------------------------------")
    assert(check_limits.battery_is_ok(50, 85, 0) is False)
    print("-------------------------------")
  #temparature limit tests
    assert(check_limits.battery_is_ok(0, 70, 0.7) is True)
    print("-------------------------------")
    assert(check_limits.battery_is_ok(45, 70, 0.7) is True)
    print("-------------------------------")
    assert(check_limits.battery_is_ok(46, 70, 0.7) is False)
    print("-------------------------------")
    assert(check_limits.battery_is_ok(-1, 70, 0.7) is False)
    print("-------------------------------")
  #soc limit tests
    assert(check_limits.battery_is_ok(40, 20, 0.5) is True)
    print("-------------------------------")
    assert(check_limits.battery_is_ok(40, 80, 0.5) is True)
    print("-------------------------------")
    assert(check_limits.battery_is_ok(40, 19, 0.5) is False)
    print("-------------------------------")
    assert(check_limits.battery_is_ok(40, 81, 0.5) is False)
    print("-------------------------------")
  #charge rate tests
    assert(check_limits.battery_is_ok(40, 25, 0.7) is True)
    print("-------------------------------")
    assert(check_limits.battery_is_ok(40, 25, 0.8) is True)
    print("-------------------------------")
    assert(check_limits.battery_is_ok(40, 25, 0.9) is False)
    print("-------------------------------")