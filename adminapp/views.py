from django.shortcuts import render
import pymysql

def adminlogin(request):
    return render(request,'adminapp/login.html')
def ALogAction(request):
    name=request.POST.get('username')
    pas=request.POST.get('password')
    if name=='Admin' and pas=='Admin':
        return render(request,'adminapp/adminhome.html')
    else:
        context={'data':'Login Failed...!!'}
        return render(request,'adminapp/login.html',context)
    
def adminhome(request):
    return render(request,'adminapp/adminhome.html')
def postrequirement(request):
    return render(request,'adminapp/PostRequirement.html')
def PostAction(request):
    location=request.POST['location']
    date=request.POST['date']
    event=request.POST['event']
    description=request.POST['description']
    con=pymysql.connect(host="localhost",user="root",password="root",database="volunteer_portal")
    cur=con.cursor()
    i=cur.execute("insert into event values(null,'"+location+"','"+date+"','"+event+"','"+description+"')")
    con.commit()
    if i>0:
        context={'data':'Program Posted Successful...!!'}
        return render(request,'adminapp/PostRequirement.html',context)
    else:
        context={'data','Posting Failed...!!'}
        return render(request,'adminapp/PostRequirement.html',context)
def ViewApplication(request):
    con=pymysql.connect(host="localhost",user="root",password="root",database="volunteer_portal")
    cur=con.cursor()
    data=cur.execute("select * from apply_event")
    data=cur.fetchall()
    strdata="<table border='1' style='margin-bottom:10px;margin-top:10px;'><tr><th>Event ID</th><th>Location</th><th>Date of Event</th><th>Program Name</th><th>User ID</th><th>UserName</th><th>Status</th><th>Accept</th></tr>"
    for i in data:
        strdata+="<tr><td>"+str(i[1])+"</td><td>"+str(i[2])+"</td><td>"+str(i[3])+"</td><td>"+str(i[4])+"</td><td>"+str(i[5])+"</td><td>"+str(i[6])+"</td><td>"+str(i[7])+"</td><td><a href='/adminapp/ConfirmApply?aid="+str(i[0])+"'>Confirm</a></td></tr>"
    context={'data':strdata}
    return render(request,'adminapp/ViewApplication.html',context)
def ConfirmApply(request):
    aid=request.GET['aid']
    con=pymysql.connect(host="localhost",user="root",password="root",database="volunteer_portal")
    cur=con.cursor()
    i=cur.execute("update apply_event set status='Confirmed' where id='"+aid+"'")
    con.commit()
    if i>0:
        context={'data':'Confirmed Successfully...!!'}
        return render(request,'adminapp/adminhome.html',context)
    else:
        context={'data':'Confirmation Failed...!!'}
        return render(request,'adminapp/adminhome.html',context)
