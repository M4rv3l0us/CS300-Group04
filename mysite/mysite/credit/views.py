from Global_Value import MAIN_WEBSITE as website
def charge(request):
    return website+"/credit/charge/"
def report(request,id=-1):
    if id==-1:
        return website+"/credit/reports/"
    else:
        return website+"/credit/reports/%d/" %id