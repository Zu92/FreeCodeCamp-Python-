import regex as re

def add_time(start, duration,day=False):
    tiempo=""
    if re.search("AM",start)==None:
        tiempo="PM"
    else:
        tiempo="AM"
    time1=start.split()[0]
    hour1=int(time1.split(":")[0])
    minute1=int(time1.split(":")[1])
    hour2=int(duration.split(":")[0])
    minute2=int(duration.split(":")[1])
    totalminute=minute1+minute2
    days=0
    if hour2>=24:
        days=int(hour2/24)
        print(days)
        hour2=hour2-24*days
    totalhour=hour1+hour2
    print(totalhour)
    if totalminute>=60:
        totalminute=totalminute-60
        totalhour=totalhour+1
    print(totalhour)
    if totalhour>=24:
        days=days+1
        totalhour=totalhour-24
  
    if totalhour>12:
        totalhour=totalhour-12
        if tiempo=="AM":
            tiempo="PM"
        else:
            tiempo="AM"
            days=days+1
    if totalhour==12:
        if tiempo=="PM":
            tiempo="AM"
            days=days+1
        else:
            tiempo="PM"
    dow=["monday","tuesday", "wednesday", "thursday", "friday","saturday","sunday"]
    number=0
    print(days)

    if totalminute<10:
        totalminute="0"+str(totalminute)
    if day!=False:
        day=day.lower()
        print(day)
        number=int(dow.index(day))+1
        index=int(number+days)
        if index> (len(dow)):
            b=int(index/7)
            index=int(index-b*7-1)
        else:
            index=index-1
        dow=["Monday","Tuesday", "Wednesday", "Thursday", "Friday","Saturday","Sunday"]
        dow=dow[index]

        if days==1:
            return(str(totalhour)+":"+str(totalminute)+" "+str(tiempo)+", "+dow+" (next day)")
        if days>1:
            return(str(totalhour)+":"+str(totalminute)+" "+str(tiempo)+", "+dow+" ("+str(days)+" days later)")
        else:
            return(str(totalhour)+":"+str(totalminute)+" "+str(tiempo)+", "+dow)        



    else:
        if days==1:
            return(str(totalhour)+":"+str(totalminute)+" "+str(tiempo)+" (next day)")
        if days>1:
            return(str(totalhour)+":"+str(totalminute)+" "+str(tiempo)+" ("+str(days)+" days later)")
        else:
            return(str(totalhour)+":"+str(totalminute)+" "+str(tiempo))