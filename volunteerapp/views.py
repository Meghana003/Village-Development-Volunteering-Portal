from django.shortcuts import render
import pymysql

def index(request):
    return render(request,'volunteerapp/index.html')
    
def login(request):
    return render(request,'volunteerapp/login.html')
def Register(request):
    return render(request,'volunteerapp/register.html')
def VRegAction(request):
    
    name=request.POST['name']
    email=request.POST['email']
    mobile=request.POST['mobile']
    address=request.POST['address']
    username=request.POST['username']
    password=request.POST['password']
    con=pymysql.connect(host="localhost",user="root",password="root",database="volunteer_portal")
    cur=con.cursor()
    i=cur.execute("insert into volunteer values(null,'"+name+"','"+email+"','"+mobile+"','"+address+"','"+username+"','"+password+"')")
    con.commit()
    if i>0:
        context={'data':'Registration Successful...!!'}
        return render(request,'volunteerapp/register.html',context)
    else:
        context={'data':'Registration Failed...!!'}
        return render(request,'volunteerapp/register.html',context)
def VLogAction(request):
    uname=request.POST.get('username')
    passw=request.POST.get('password')
    con=pymysql.connect(host="localhost",user="root",password="root",database="volunteer_portal")
    cur=con.cursor()
    data=cur.execute("select * from volunteer where username='"+uname+"'and password='"+passw+"'")
    data=cur.fetchone()
    if data is not None:
        request.session['user']=uname
        request.session['email']=data[2]
        request.session['id']=data[0]
        return render(request,'volunteerapp/VolunteerHome.html')
    else:
        context={'data':'Login Failed ....!!'}
        return render(request,'volunteerapp/login.html',context)
   
def ViewPrograms(request):
    con=pymysql.connect(host="localhost",user="root",password="root",database="volunteer_portal")
    cur=con.cursor()
    data=cur.execute("select * from event")
    data=cur.fetchall()
    strdata="<table border='1' style='margin-bottom:10px;margin-top:10px;'><tr><th>Event ID</th><th>Location</th><th>Date of Event</th><th>Program Name</th><th>Description</th><th>Apply</th></tr>"
    for i in data:
        strdata+="<tr><td>"+str(i[0])+"</td><td>"+str(i[1])+"</td><td>"+str(i[2])+"</td><td>"+str(i[3])+"</td><td>"+str(i[4])+"</td><td><a href='/Apply?eid="+str(i[0])+"&location="+str(i[1])+"&date="+str(i[2])+"&event="+str(i[3])+"'>Confirm</a></td></tr>"
    context={'data':strdata}
    return render(request,'volunteerapp/ViewPrograms.html',context)
def Apply(request):
    eid=request.GET['eid']
    location=request.GET['location']
    date=request.GET['date']
    event=request.GET['event']
    request.session['eid']=eid
    request.session['location']=location
    request.session['date']=date
    request.session['event']=event
    return render(request,'volunteerapp/Apply.html')
    
def ApplyAction(request):
    eid=request.POST['eid']
    location=request.POST['location']
    date=request.POST['date']
    event=request.POST['event']
    userid=str(request.session['id'])
    username=str(request.session['user'])
    con=pymysql.connect(host="localhost",user="root",password="root",database="volunteer_portal")
    cur=con.cursor()
    i=cur.execute("insert into apply_event values(null,'"+eid+"','"+location+"','"+date+"','"+event+"','"+userid+"','"+username+"','waiting')")
    con.commit()
    if i>0:
        context={'data':'Application Submitted!'}
        return render(request,'volunteerapp/VolunteerHome.html',context)
    else:
        context={'data':'Apply Failed...!!'}
        return render(request,'volunteerapp/VolunteerHome.html',context)

def applystatus(request):
    userid=str(request.session['id'])
    con=pymysql.connect(host="localhost",user="root",password="root",database="volunteer_portal")
    cur=con.cursor()
    data=cur.execute("select * from apply_event where uid='"+userid+"'")
    data=cur.fetchall()
    strdata="<table border='1' style='margin-bottom:10px;margin-top:10px;'><tr><th>Event ID</th><th>Location</th><th>Date of Event</th><th>Program Name</th><th>Status</th></tr>"
    for i in data:
        strdata+="<tr><td>"+str(i[1])+"</td><td>"+str(i[2])+"</td><td>"+str(i[3])+"</td><td>"+str(i[4])+"</td><td>"+str(i[7])+"</td></tr>"
    context={'data':strdata}
    return render(request,'volunteerapp/ViewApplyStatus.html',context)
    

