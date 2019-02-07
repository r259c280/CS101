def is_leap(year):
    if year % 4 == 0:
            return True
    else:
            return False
        
year_list = []
    for year in range(1950, 2151):
        if is_leap(year):
            year_list.append(year)



#boom
year_list = [year for year in range(1950, 2151) if is_leap(year)]
