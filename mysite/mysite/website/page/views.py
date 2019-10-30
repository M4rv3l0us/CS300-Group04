from Global_Value import MAIN_WEBSITE as website
def history(request,slug='chillzone',id=1):
    return website+"/page_%s-page_%d/history/" %(slug,id)
def edit(request,slug='chillzone',id=1):
    return website+"/page_%s-page_%d/edit/" %(slug,id)
def discuss(request,slug='chillzone',id=1):
    return website+"/page_%s-page_%d/discuss/" %(slug,id)
def permissions(request,slug='chillzone',id=1):
    return website+"/page_%s-page_%d/permissions/" %(slug,id)