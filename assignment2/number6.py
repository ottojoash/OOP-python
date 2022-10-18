def isYearLeap(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
# Return true if year is a multiple
    # of 4 and not multiple of 100.
    # OR year is multiple of 400.
# return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0));

testData = [1900, 2000, 2015, 1987]
testResults = [False, True, True, False]
for i in range(len(testData)):
    yr = testData[i]
    print(yr, "->", end="")
    result = isYearLeap(yr)
    if result == testResults[i]:
        print("OK - Leap Year")
    else:
        print("Failed - Not Leap Year")