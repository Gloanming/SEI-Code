
def flight_calculation():
    input1 = input()
    input2 = input()
    # 第一行数据
    append1 = '(+0)'
    if len(input1) > 17:
        takeofftime1, landofftime1, append1 = input1.split(' ')
    else:
        takeofftime1, landofftime1 = input1.split(' ')
    append1 = append1[2]
    append1 = int(append1)
    takehour1, takeminute1, takesecond1 = takeofftime1.split(':')
    landhour1, landminute1, landsecond1 = landofftime1.split(':')
    takehour1 = int(takehour1)
    takeminute1 = int(takeminute1)
    takesecond1 = int(takesecond1)
    landhour1 = int(landhour1)
    landminute1 = int(landminute1)
    landsecond1 = int(landsecond1)
    landhour1 = landhour1 + append1*24
    resulthour1 = landhour1 - takehour1
    resultminute1 = landminute1 - takeminute1
    resultsecond1 = landsecond1 - takesecond1
    while resultsecond1 < 0:
        resultminute1 -= 1
        resultsecond1 += 60
    while resultminute1 < 0:
        resulthour1 -= 1
        resultminute1 += 60

    # print('{:0>2d}:{:0>2d}:{:0>2d}'.format(resulthour1,resultminute1,resultsecond1))

    # 第二行数据
    append2 = '(+0)'
    if len(input2) > 17:
        takeofftime2, landofftime2, append2 = input2.split(' ')
    else:
        takeofftime2, landofftime2 = input2.split(' ')
    append2 = append2[2]
    append2 = int(append2)
    takehour2, takeminute2, takesecond2 = takeofftime2.split(':')
    landhour2, landminute2, landsecond2 = landofftime2.split(':')
    takehour2 = int(takehour2)
    takeminute2 = int(takeminute2)
    takesecond2 = int(takesecond2)
    landhour2 = int(landhour2)
    landminute2 = int(landminute2)
    landsecond2 = int(landsecond2)
    landhour2 = landhour2 + append2*24
    resulthour2 = landhour2 - takehour2
    resultminute2 = landminute2 - takeminute2
    resultsecond2 = landsecond2 - takesecond2
    while resultsecond2 < 0:
        resultminute2 -= 1
        resultsecond2 += 60
    while resultminute2 < 0:
        resulthour2 -= 1
        resultminute2 += 60
    # print('{:0>2d}:{:0>2d}:{:0>2d}'.format(resulthour2,resultminute2,resultsecond2))
    outhour = ((resulthour1 + resulthour2) / 2)
    outmin = ((resultminute1 + resultminute2) / 2)
    outsecond = ((resultsecond1 + resultsecond2) / 2)
    if outhour > int(outhour):
        if outmin < 30:
            outhour = int(outhour)
            outmin += 30
        else:
            outmin -= 30
            outhour = int(outhour) + 1
    if outmin > int(outmin):
        if outsecond < 30:
            outmin = int(outmin)
            outsecond += 30
        else:
            outmin = int(outmin) + 1
            outsecond -= 30
    outhour = int(outhour)
    outmin = int(outmin)
    outsecond = int(outsecond)
    if(outsecond >= 60):
        outsecond -= 60
        outmin += 1
    if(outmin >= 60):
        outmin -= 60
        outhour += 1
    print('{:0>2d}:{:0>2d}:{:0>2d}'.format(outhour, outmin, outsecond))

    # enter your code here
