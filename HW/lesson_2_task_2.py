year = int(input("Год: "))
def is_year_leap(year):
        if (year % 4 == 0):
                print ( "год" , year , ": True" )
                return True
        else:
                print ( "год" , year , ": False")
                return False
        
is_year_leap(year)
