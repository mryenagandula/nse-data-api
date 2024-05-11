import datetime
import os

def getPastWeekDate():
    N_DAYS_AGO = 7
    today = datetime.datetime.now()
    n_days_ago = today - datetime.timedelta(days=N_DAYS_AGO)
    strDate = n_days_ago.strftime("%d-%m-%Y");
    return strDate;
    
def getTodayDate():
    today = datetime.datetime.now()
    strDate = today.strftime("%d-%m-%Y");
    return strDate;

def getAutoGeneratedFileName(strFileType):
    strDate = datetime.datetime.now().strftime("%d%m%Y_%H%M%S");
    datefolder = datetime.datetime.now().strftime("%d%m%Y");
    folderPath = "H://NSEReports//"+datefolder;
    if os.path.exists(folderPath):
        print("folder already exits")
    else:
         path = os.path.join("H://NSEReports//", datefolder)
         os.makedirs(path);
   
    fileName = "H://NSEReports//"+datefolder+"//security_wise_archive_"+strFileType+"_data_"+strDate+".csv";
    return fileName;


def getAutoGeneratedLogFileName(strFileType):
    strDate = datetime.datetime.now().strftime("%d%m%Y_%H%M%S");
    fileName = "logs_security_wise_archive_"+strFileType+"_data_"+strDate+".log";
    return fileName;