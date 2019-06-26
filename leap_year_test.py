def leap_year_test(year):
    if year % 4 != 0 :
        print('該年為平年')
    elif year % 100 == 0 and year % 400 != 0 :
        print('該年為平年')
    elif year % 4 == 0 and year % 100 != 0 :
        print('該年為閏年')
    elif year % 400 == 0 and year % 3200 != 0 :
        print('該年為閏年')

year = input('請輸入公元年份')
leap_year_test(int(year))
