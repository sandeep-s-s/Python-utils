import datetime

class TimeAgo:

    def __init__(self,dateTimeAgo):
        self.dateTimeAgo = dateTimeAgo
        self.currentDateTime = datetime.datetime.now()
        self.durationInSec = (self.currentDateTime - self.dateTimeAgo).total_seconds()  
        self.seconds = round(self.durationInSec)
        self.minutes = round(self.durationInSec/ 60) # minute = seconds/60
        self.hours = round(self.durationInSec/ 3600) # hour = seconds/3600 [60 * 60]
        self.days = round(self.durationInSec/ 86400) # days = seconds/86400 [24 * 3600]
        self.weeks = round(self.durationInSec / 604800) # weeks =  [7* 24 * 3600]
        self.months = round(self.durationInSec /  2629440) # months ((365+365+365+365+366)/5/12)*24*60*60
        self.years = round(self.durationInSec/ 31536000) # year (365+365+365+365+366)/5 * 24 * 60 * 60 

    def getYears(self):
        return self.years

    def getDays(self):
        return self.days

    def getHours(self):
        return self.hours   

    def getMinutes(self):
        return self.minutes 

    def getSeconds(self):
        return self.seconds

    def timeAgo(self):
        if (self.seconds <=60):
            return("Just Now")
        elif (self.minutes <= 60):
            if (self.minutes == 1):
                return("One minute ago")
            else:
                return(f'{self.minutes} minutes ago')
        elif (self.hours <= 24):
            if (self.hours == 1):
                return("One hour ago")
            else:
                return(f'{self.hours} hours ago')
        elif (self.days <= 7):
            if (self.days == 1):
                return("Yesterday")
            else:
                return(f'{self.days} days ago')
        elif (self.weeks <= 4.3): #4.3 == 52/12  
            if (self.weeks == 1):
                return("A week ago")
            else:
                return(f'{self.weeks} weeks ago')
        elif (self.months <= 12): #4.3 == 52/12  
            if (self.months == 1):
                return("A month ago")
            else:
                return(f'{self.months} months ago')
        else:  
            if (self.years == 1):
                return("A year ago")
            else:
                return(f'{self.years} years ago')



datetime_object = datetime.datetime.strptime('Jan 01 2020  11:10PM', '%b %d %Y %I:%M%p')
p = TimeAgo(datetime_object)
print(p.timeAgo())
      