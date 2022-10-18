from flask import Flask,request,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/sample'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db = SQLAlchemy(app)

class Emp(db.Model):
    empId = db.Column('emp_id',db.Integer(),primary_key=True)
    empName = db.Column('emp_name',db.String(50))
    empSal = db.Column('emp_sal', db.Float())
    empAge = db.Column('emp_age', db.Integer())
    empadr =  db.Column('emp_adr',db.String(50))
    empdes = db.Column('emp_des', db.String(50))
    active = db.Column('emp_active', db.String(50),default='Y')
#
#db.create_all()

#base -- http://localhost:5000 -- uri
#request uri --
def logic(emp):
    return emp.empName

def sort_employees():
    emps = Emp.query.all()
    emps.sort(key=logic)
    return emps

@app.route("/")
def welcome_page():
    a = "Hello, Good NIght..!"
    return render_template('index.html',emps = sort_employees(),sam = a)

@app.route("/employee/save/",methods= ["POST"])
def save_employee():
    print('user given values inside requests -- ',request.args)
    print(request.args,"URI -- GET")
    print(request.form,"URI -- POST")
    #einfo = request.args #get-- uri
    einfo = request.form  # get-- uri
    emp = Emp(empId=einfo['eid'], empName=einfo['enm'],
        empSal=einfo['esal'], empAge=einfo['eage'], empadr=einfo['eadr'],
        empdes=einfo['epos'])
    db.session.add(emp)
    db.session.commit()
    return render_template('index.html',emps = sort_employees(),
                           msg = "Emp record Saved Successfully...!")




if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')












