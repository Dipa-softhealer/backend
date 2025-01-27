# Day of the Week from Date

from datetime import datetime



def getWeekDay(inp):
    tmp = datetime.strptime(inp,"%Y-%M-%d")
    if(tmp.weekday()==0):
        return "monday"
    elif(tmp.weekday()==1):
        return "tuesday"
    elif(tmp.weekday()==2):
        return "wednesday"
    elif(tmp.weekday()==3):
        return "thusday"
    elif(tmp.weekday()==4):
        return "friday"
    elif(tmp.weekday()==5):
        return "saturday"
    elif(tmp.weekday()==6):
        return "sunday, funday!"
    
inp = '2021-10-11'
res = getWeekDay(inp)
print(res)