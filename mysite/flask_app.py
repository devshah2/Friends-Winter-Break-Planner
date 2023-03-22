from flask import Flask, render_template,request
import datetime
app=Flask(__name__)
pwd="anything21"
import MySQLdb


# arrivals={"dev":['23']}

def checkInfo(name, email):
    db = MySQLdb.connect(
        host = "friendsBreakPlanner.mysql.pythonanywhere-services.com",
        user = "friendsBreakPlan",
        passwd = pwd,
        db = "friendsBreakPlan$default"
        )
    # return str(db)

    cursor = db.cursor()
    cursor.execute("SELECT arrival,departure FROM dates where name='{}' and email='{}';".format(name,email))
    if [x for x in cursor] == []:
        cursor.execute("insert into dates(name, email) values('{}','{}');".format(name,email))
        db.commit()
        return "",""
    else:
        return [x for x in cursor][0]

@app.route('/',methods=(['GET']))
def main():
    return render_template('index.html')

def func(name,email):
    arriving,leaving=checkInfo(name,email)
    db = MySQLdb.connect(
        host = "friendsBreakPlanner.mysql.pythonanywhere-services.com",
        user = "friendsBreakPlan",
        passwd = pwd,
        db = "friendsBreakPlan$default"
        )
    cursor = db.cursor()
    cursor.execute("SELECT name,arrival,departure FROM dates;")
    res=[x for x in cursor if x[1]!=None and x[2]!=None]
    arrivals=[x[1] for x in res]
    departures=[x[2] for x in res]
    cur=min(arrivals)
    last=max(departures)
    delta = datetime.timedelta(days=1)
    cur-=delta

    dates=[]
    values=[]
    people=[]
    i=0

    while(cur<=last):
        dates.append([cur.strftime("%d"),cur.strftime("%m"),cur.strftime("%Y")])

        count=0
        names=[]

        for entry in res:
            if(entry[1]<=cur and entry[2]>=cur):
                count+=1
                names.append(entry[0])
        values.append(count)
        people.append(names)


        i+=1
        cur+=delta

    # return str(min(arrivals))
    # dates=[[21,6,2023],[22,6,2023]]
    # values=[2,4]

    n=len([x for x in cursor])
    # people=[["dev","edhita"],["dev","edhita","ritvik","nikunj"]]
    # return str(people)
    return render_template('calendar.html',arriving=arriving,leaving=leaving,name=name,email=email,dates=dates,n=n,values=values,people=people)

@app.route('/calendar',methods=(['POST']))
def main2():
    if(request.method=='POST'):
        name=request.form.get("name")
        email=request.form.get("Email")
        return func(name,email)

@app.route('/calendar2',methods=(['POST']))
def calendar2():
    name=request.form.get("name")
    email=request.form.get("email")
    arriving=request.form.get("arriving")
    leaving=request.form.get("leaving")
    # return "update dates set arrival='{}', departure='{}' where name='{}' and email='{}';".format(arriving, leaving,name,email)
    db = MySQLdb.connect(
        host = "friendsBreakPlanner.mysql.pythonanywhere-services.com",
        user = "friendsBreakPlan",
        passwd = pwd,
        db = "friendsBreakPlan$default"
        )

    cursor = db.cursor()
    cursor.execute("update dates set arrival='{}', departure='{}' where name='{}' and email='{}';".format(arriving, leaving,name,email))
    db.commit()
    return func(name,email)



if(__name__=='__main__'):
    app.run()