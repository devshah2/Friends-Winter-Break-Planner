from flask import Flask, render_template,request
app=Flask(__name__)

# arrivals={"dev":['23']}

def checkInfo():
    return "2023-06-01","2023-09-01"
@app.route('/',methods=(['GET']))
def main():
    # print(request.args)
    # print(request.method)
    # 
    # else: 
    return render_template('index.html')

@app.route('/calendar',methods=(['POST']))
def main2():
    if(request.method=='POST'): 
        name=request.form.get("name")
        email=request.form.get("Email")
        arriving,leaving=checkInfo()
        dates=[[21,6,2023],[22,6,2023]]
        n=10
        values=[2,4]
        people=[["dev","edhita"],["dev","edhita","ritvik","nikunj"]]
        return render_template('calendar.html',arriving=arriving,leaving=leaving,name=name,dates=dates,n=n,values=values,people=people)
    else:
        return "hi"

if(__name__=='__main__'):
    app.run()