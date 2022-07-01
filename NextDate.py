#program to find next date of a gicen date
day,month,year=[int(x) for x in input("Enter the date:(dd/mm/yyyy) ").split('/')]
if month ==12:
    if day ==31:
        day = 1
        month = 1
        year = year + 1
    else:
        day = day+1
    print('Next date {}/{}/{}'.format(day,month,year))
elif month in [1,3,5,7,8,10]:
    if day ==31:
        day =1
        month = month +1
    else:
        day = day + 1
    print('Next date {}/{}/{}'.format(day,month,year))
elif month in[4,6,9,11]:
    if day == 30:
        day =1
        month=month+1
    else:
        day =day +1
    print('Next date {}/{}/{}'.format(day,month,year))
elif month == 2:
    if ((year%4==0)and not (year%100==0)or(year%400==0)):
        if day ==29:
            day = 1
            month =month +1
        else:
            day = day +1
        print('Next date {}/{}/{}'.format(day,month,year))
    else:
        if day ==28:
            day =1
            month = month + 1
        else:
            day = day +1
        print('Next date {}/{}/{}'.format(day,month,year))
else:
    print('Invalid Data')
            
