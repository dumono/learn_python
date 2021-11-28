def get_summ(one,two,delimiter='&'):
    return str(str(one) + delimiter + str(two))

result= get_summ("Learn", "python")
print (result)
print(result.upper())