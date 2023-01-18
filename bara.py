def func1(arg1, arg2):
    var7 = func2(arg1, arg2)
    def func3(arg8, arg9):
        var10 = func6()
        var11 = (262434310 ^ var10 ^ ((((arg1 | (-26 & (arg8 + (((arg1 | (-91927149 ^ (arg2 - (arg9 | (arg8 & var7) ^ 396)) ^ arg8) ^ var10) | 584374266) ^ 394) + arg9))) | var7) | var7) + 193136048)) - var10 & arg8
        var12 = var7 + (((arg2 ^ var10) & arg8) ^ var11)
        var13 = arg1 & var10
        result = arg9 ^ (arg1 - ((var13 | (var13 | arg9) ^ arg8 + (-336 & var7)) + var13 + (var13 - -1908532256))) ^ var13
        return result
    var14 = func3(var7, arg2)
    var40 = func7(var14, var7)
    var41 = func10()
    if arg2 < var41:
        var42 = (var14 & var40) ^ arg2 + arg1
    else:
        var42 = (arg1 | var7) | arg2 & arg1
    var43 = var41 + arg1 ^ (var14 & -1771092543)
    var44 = var43 & 2055441908 - var14 ^ -826597668
    var45 = (var44 ^ var43) + -1894579702
    var46 = 547 + ((875 & 937) ^ arg2)
    var47 = (-262206787 ^ arg2) ^ var14 + var7
    var48 = var44 + 204
    if arg2 < var48:
        var49 = -405 - var7 | var43 & var47
    else:
        var49 = var41 - (var40 & var44)
    var50 = (var44 ^ var45) + arg1
    var51 = var47 - var48
    var52 = var46 | var44
    var53 = (var44 & arg2 + var45) & var40
    var54 = var46 & var41
    var55 = var46 + arg1 | var47 + arg2
    var56 = 356 & (var14 + var55)
    var57 = (1111530560 | (var14 | var41)) ^ var47
    result = (var44 + (var56 | (var46 - var14 - var52 ^ (arg2 | (var44 | arg1) ^ -1876589212) ^ (var44 ^ arg2)))) + var51
    return result
def func10():
    func8()
    result = len(xrange(36))
    func9()
    return result
def func9():
    global len
    del len
def func8():
    global len
    len = lambda x : 6
def func7(arg15, arg16):
    var17 = arg15 ^ (317 ^ arg15) ^ arg15
    var18 = var17 - (15 + var17) | -10
    if var18 < arg16:
        var19 = arg16 & var17 - (-145 | 1082986003)
    else:
        var19 = 1600824088 - var18 ^ (var18 ^ var17)
    var20 = (-905798967 & arg16) ^ 54
    var21 = arg16 ^ arg16
    var22 = var21 ^ var21 - var20 - var17
    var23 = ((var22 + var17) | var17) & var20
    var24 = -23987605 & (-2146217644 & (var23 & var22))
    var25 = -1602599922 | (var20 & 1723290810 - arg15)
    var26 = (arg16 | var18) + arg15 ^ var24
    var27 = var22 | var23 - var17 ^ var17
    var28 = (var21 & 910829617 + 819) + var27
    var29 = (457 ^ var22) ^ (arg16 - var23)
    var30 = var26 | var28 + var17 + var22
    var31 = (var30 | var18) + var23
    var32 = var25 + (arg15 | var21 + var26)
    var33 = (var28 + var29) ^ (var24 ^ var20)
    var34 = var33 + var27
    var35 = var31 + var21 & arg16 & arg16
    var36 = (var26 - (var21 ^ var23)) | arg16
    var37 = (var22 | -233) | -528610895
    var38 = -185 ^ var35 - var17 + var37
    if var18 < var37:
        var39 = var33 + (var25 & var34)
    else:
        var39 = (var36 | -372 + var37) - var29
    result = -70245563 & (var38 - var30 | ((var34 ^ (var37 & var17 ^ var32) & var20 & var30 + var35) - var36)) + var26
    return result
def func6():
    func4()
    result = len(xrange(17))
    func5()
    return result
def func5():
    global len
    del len
def func4():
    global len
    len = lambda x : 1
def func2(arg3, arg4):
    var5 = 0
    for var6 in range(7):
        var5 += (var5 - var6) & arg3
    return var5
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 11'
    print 'arg_number: 58'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
