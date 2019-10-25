website="example.com.vn"
def page(request,num=1):
    return  website+"/blog/page%d/" %num
def year_archive(request,year=2003):
    return website+"/articles/%d/" %year
def month_archive(request,year=2003,month=3):
    return website+"/articles/%d/%d/" %(year,month) 
def article_detail(request,year=2003,month=3,slug="building-a-django-site"):
    return website+"/articles/%d/%d/%s/" %(year,month,slug)
def comments(request,num=1):
    return website+"comments/page-%d/" %num