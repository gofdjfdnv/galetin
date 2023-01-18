def func1(arg1, arg2):
    var7 = func2(arg1, arg2)
    def func3(arg8, arg9):
        var10 = (arg1 - arg2) + var7 + var7 ^ arg1 + 199 & arg9
        var11 = var7 ^ arg2
        result = arg2 - var10
        return result
    var12 = func3(arg2, arg1)
    var17 = func4(var12, arg2)
    var22 = func5(arg2, var7)
    var27 = func6(arg1, var7)
    var28 = 105 - var7
    var29 = (var17 - var22 & (arg1 ^ -1797794788)) ^ (((arg2 - var28) + var12 | -702) ^ var12 ^ ((var28 ^ ((var27 | arg2) ^ (-1809934602 & (222483663 | arg1))) - var17) - var28 & (var27 ^ var17 | var22) | 648)) | var22
    var30 = ((var17 & var12) + ((arg1 & -892 + (264 | -1382351746) - (((var7 ^ var29 & var17 & arg1 ^ (var12 | var27) + (var7 & ((var7 ^ arg2) & (arg1 | var7 ^ var29)))) ^ 1910543861) & var27)) | arg2)) | var28
    var31 = var17 - (((-1057796933 | var17) ^ (var28 & var27) - -2017626673) ^ (-446647602 - var12 & var30) + (var7 & (var27 + var27 | 736584399))) | (var7 | var30 ^ 758583961)
    result = (var31 ^ var29) | var7
    return result
def func6(arg23, arg24):
    var25 = 0
    for var26 in range(34):
        var25 += (var25 - arg23) - arg24
    return var25
def func5(arg18, arg19):
    var20 = 0
    for var21 in xrange(45):
        var20 += var20 | 8 | arg18
    return var20
def func4(arg13, arg14):
    var15 = 0
    for var16 in xrange(11):
        if var16 < var16:
            var15 += var15 ^ arg13
        else:
            var15 += -4 ^ arg14 & arg13
    return var15
def func2(arg3, arg4):
    var5 = 0
    for var6 in range(17):
        var5 += var6 + arg3
    return var5
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 7'
    print 'arg_number: 32'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
