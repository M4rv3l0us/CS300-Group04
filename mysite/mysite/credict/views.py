website="example.com.vn"
def charge(request):
    return website+"/charge/"
    
def report(request,id=-1):
    if id==-1:
        return website+"/reports/"
    else:
        return website+"/reports/%d/" %id