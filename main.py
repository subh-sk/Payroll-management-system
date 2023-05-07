# importing Flask and other modules
from flask import Flask, request, render_template
import mysql.connector as mysql
import random
import smtplib
from datetime import datetime as dt
import datetime
import calendar
from dateutil.relativedelta import relativedelta  #pip install python-dateutil
from email.mime.text import MIMEText


def otp_send(email):
    global otp
    otp=random.randint(1000,9999)
    smp = smtplib.SMTP('smtp.gmail.com', 587)
    smp.starttls()
    smp.login('payrollrecoverymail@gmail.com', 'qogaudzbcaoghlto')
    msg_body = f"Hello {email}, Your OTP for account recovery = {otp}"
    msg = MIMEText(msg_body)
    msg['Subject'] = 'Account Recovery OTP'
    msg['From'] = 'payrollrecoverymail@gmail.com'
    msg['To'] = email
    smp.sendmail("payrollrecoverymail@gmail.com", email, msg.as_string())
    smp.quit()

 
wrong_credention_h6="<h6 style='color:red;position: relative;top:-185px;left:670px;width:11%; family-weight:bold; font-size:large;'>{}</h6>"
wrong_credentioal_h6_1="<h6 style='color:red;position: relative;top:-75px;left:675px;width:11%; family-weight:bold; font-size:large;'>{}</h6>"


# Flask constructor
app = Flask(__name__,static_url_path='/static')  
 
# starting webpage
@app.route('/', methods=['POST', 'GET'])
def main_index():
    return render_template("index.html")

# home page of website
@app.route("/home",methods=["POST","GET"])
def index():
    # creating coonection with database
    conn=mysql.connect(host="localhost",user="root",passwd="",db="payroll")
    c=conn.cursor()
    c.execute("SET GLOBAL event_scheduler=ON;") #turning on event scheduler
    c.execute("select Name,Email,Salary from emp_detail")
    emp_details=c.fetchall()
    
    x=datetime.date.today()
    x=x-relativedelta(months=1)
    salary_mnth=x.strftime("%B")
    salary_year=x.strftime("%Y")

    
    for i in (emp_details):
        f_date_x=str(x)

        l_date = x.replace(day = calendar.monthrange(x.year, x.month)[1])
        f_date= datetime.date(int(f_date_x[:4]),int(f_date_x[5:7]),int(f_date_x[8:])).replace(day=1)

        c.execute(f"select Leave_Day from emp_report where Email='{i[1]}' and Approve='approved' and Date between '{f_date}' and '{l_date}'")
        leave_days=c.fetchall()
        # print(x)
        leave_days=sum([j for i in leave_days for j in i ])*500
        # print(x)
        total_salary=i[2]
        deduction=total_salary-leave_days
        allowance=total_salary-deduction
        y=datetime.date.today()
        print("yyyy = ",y,type(y))
        schedule = y.replace(day = calendar.monthrange(y.year, y.month)[1])
        print("schedule = ",schedule,type(schedule))
        # creating event for salary
        if y==schedule:            
            c.execute(f'''CREATE EVENT IF NOT EXISTS `emp_salary_{i[1]}`
            ON SCHEDULE AT '{schedule}'
            ON COMPLETION NOT PRESERVE
            DO INSERT into salary (`Name`, `Email`, `Allowance`, `Deduction`, `Total_Salary`, `Month`,`Year`, `Status`) VALUES ('{i[0]}','{i[1]}','{allowance}','{deduction}','{total_salary}','{salary_mnth}','{salary_year}','Paid');''')
            conn.commit()
    return render_template("index.html")

# login page
@app.route("/login",methods=["POST","GET"])
def check():
    conn=mysql.connect(host="localhost",user="root",passwd="",db="payroll")
    c=conn.cursor()
    output=request.form.to_dict()
    global m_email , m_login_type
    m_email=output["email"]
    password=output["password"]
    m_login_type=output["login_type"]
    if m_login_type=="Admin":
     c.execute("SELECT * FROM admin_detail where Email='{0}'".format(m_email))  
     check_id=(c.fetchall())
     try:
        if password==check_id[0][3] and m_email==check_id[0][2]:
            c.execute("select * from emp_detail ")
            total_emp=len(c.fetchall())
            conn.commit()
            c.execute("select * from emp_detail where Status='active' ")
            total_active=len(c.fetchall())
            conn.commit()
            c.execute("select * from emp_detail where Status='deactive' ")
            total_deative=len(c.fetchall())
            conn.commit()
            c.execute("select * from emp_report ")
            total_leave=len(c.fetchall())
            conn.commit()
            c.execute("select * from emp_report where Approve='Reject' ")
            total_emp_deative=len(c.fetchall())
            conn.commit()
            c.execute("select * from emp_report where Approve='approved' ")
            total_emp_ative=len(c.fetchall())
            conn.commit()
            return render_template("home.html",total_emp=total_emp,total_active=total_active,total_deative=total_deative,total_leave=total_leave,total_emp_deative=total_emp_deative,total_emp_ative=total_emp_ative)
        else:
            return render_template("index.html",show_wrong=True)
     except:
            return render_template("index.html",show_wrong=True)

    else:
        c.execute("SELECT * FROM emp_detail where Email='{0}'".format(m_email))  
        check_id=(c.fetchall())
        try:
            if password==check_id[0][10] and m_email==check_id[0][9]:
                # c.execute("select * from emp_report where Email='{}'".format(m_email))
                # leave=len(c.fetchall())
                c.execute("select * from emp_report where Email='{}'".format(m_email))
                total_emp_leave=len(c.fetchall())
                conn.commit()
                c.execute("select * from emp_report where Approve='Reject' and Email='{}'".format(m_email))
                total_emp_deative=len(c.fetchall())
                conn.commit()
                c.execute("select * from emp_report where Approve='approved' and Email='{}'".format(m_email))
                total_emp_ative=len(c.fetchall())
                conn.commit()
                try:
                    x=datetime.date.today()
                    # print("x = ",x)

                    y=x+relativedelta(months=1)
                    # print("y = ",y)
                    f_date_y=str(y)
                    # print("f_date_x = ",f_date_y)
                    y=datetime.date(int(f_date_y[:4]),int(f_date_y[5:7]),int(f_date_y[8:])).replace(day=1)
                    z=x+relativedelta(months=-1)
                    salary_mnth=z.strftime("%B")
                    salary_year=z.strftime("%Y")
                    c.execute(f"SELECT `Allowance`, `Deduction`, `Total_Salary` FROM `salary` WHERE Email='{m_email}' and Month='{salary_mnth}' and Year='{salary_year}'")
                    emp_salary=c.fetchall()
                    last_salary=emp_salary[0][2]
                    emp_allowance=emp_salary[0][0]
                    emp_dedution=emp_salary[0][1]
                    return render_template("emp_home.html",to_send=total_emp_leave,total_emp_deative=total_emp_deative,total_emp_ative=total_emp_ative,last_salary=last_salary,emp_allowance=emp_allowance,emp_dedution=emp_dedution)
                except:
                    return render_template("emp_home.html",to_send=total_emp_leave,total_emp_deative=total_emp_deative,total_emp_ative=total_emp_ative,last_salary=0,emp_allowance=0,emp_dedution=0)
            else:
                return render_template("index.html",show_wrong=True)
        except:
            return render_template("index.html",show_wrong=True)

# returing forget_account.html page
@app.route("/forgot_account.html",methods=["POST","GET"])
def forgot():
    return render_template("forgot_account.html")

# forget_account page 
@app.route("/forgot_account",methods=["POST","GET"])
def forgot_pass():
    conn=mysql.connect(host="localhost",user="root",passwd="",db="payroll")
    c=conn.cursor()
    global email_check,login_type
    output=request.form.to_dict()
    email=email_check=output["email"]
    mobile=int(output["mob_number"])
    login_type=output["login_type"]
    print(mobile,email,login_type)
    if login_type=="Admin":
        c.execute("SELECT * FROM admin_detail where Email='{}' and Mobile={}".format(email,mobile))  
        check_id=(c.fetchall())
        try:
            if email==check_id[0][2] and mobile==check_id[0][1]:
                otp_send(email)
                return render_template("forgot_pass.html")
            else:
                return render_template("forgot_account.html",show_alert=True)
        except:
            return render_template("forgot_account.html",show_alert=True)
    else:
        c.execute("SELECT * FROM emp_detail where Email='{}' and Mobile={}".format(email,mobile))  
        check_id=(c.fetchall())
        try:
            if email==check_id[0][9] and mobile==check_id[0][4]:
                otp_send(mobile)
                return render_template("forgot_pass.html")
            else:
                return render_template("forgot_account.html",show_alert=True)
        except:
            return render_template("forgot_account.html",show_alert=True)

# login page after using forgot password
@app.route("/login_again",methods=["POST","GET"])
def pass_changed():
    conn=mysql.connect(host="localhost",user="root",passwd="",db="payroll")
    c=conn.cursor()
    output=request.form.to_dict()
    OTP=int(output["OTP"])
    password=output["pass"]
    if OTP==otp:
        if login_type=="Admin": 
            c.execute("update admin_detail set `Password`='{}'  where Email='{}'".format(password,email_check))
            conn.commit()
            return render_template("index.html",show_alert=True)
        else:
            c.execute("update emp_detail set `Password`='{}' where Email='{}'".format(password,email_check))
            conn.commit()
            return render_template("index.html",show_alert=True)
    else:
        return render_template("forgot_pass.html",show_otp=True)
        # return render_template("forgot_pass.html")+'<h6>wr</h6><script>function alert_msg() {alert("Wrong OTP")};</script>'

# signup page
@app.route("/sign_up.html",methods=["POST","GET"])
def l_signup():
    return render_template("sign_up.html")

@app.route("/sign_up",methods=["POST","GET"])
def result():
    conn=mysql.connect(host="localhost",user="root",passwd="",db="payroll")
    c=conn.cursor()
    output=request.form.to_dict()
    fname=output["fname"].lower()
    lname=output["lname"].lower()
    email=output["email"]
    password=output["pass"]
    mobile=output["mob_number"]
    c.execute("INSERT INTO admin_detail values('{} {}','{}','{}','{}')".format(fname,lname,mobile,email,password))
    conn.commit()
    conn.close()
    return render_template("index.html")
#add employee page 
@app.route("/add_employee",methods=["POST","GET"])
def add_emp():
    conn=mysql.connect(host="localhost",user="root",passwd="",db="payroll")
    c=conn.cursor()
    output=request.form.to_dict()
    name=output["name"].lower()
    # name=name.lower()
    city=output["city"]
    address=output["address"]
    salary=output["salary"]
    pincode=output["pincode"]
    bank_account=output["bank_account"]
    mobile=output["mobile"]
    email=output["email"]
    degree=output["degree"]
    designation=output["designation"]
    branch=output["branch"]
    password=output["pass"]
    c.execute("INSERT INTO emp_detail (`Name`, `Address`, `City`, `Pincode`, `Mobile`, `Degree`, `Designation`, `Salary`, `Bank_no`, `Email`, `Password`,`Branch`) VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name,address,city,pincode,mobile,degree,designation,salary,bank_account, email,password,branch))
    conn.commit()
    conn.close()
    return render_template("add_employee.html",show_alert=True)

# returning add_empolyee.html page
@app.route("/add_employee.html",methods=["POST","GET"])
def emp_add():
    return render_template("add_employee.html")

# admin dashbord page
@app.route("/home.html",methods=["POST","GET"])
def emp_add_home():
    conn=mysql.connect(host="localhost",user="root",passwd="",db="payroll")
    c=conn.cursor()
    c.execute("select * from emp_detail ")
    total_emp=len(c.fetchall())
    conn.commit()
    c.execute("select * from emp_detail where Status='active' ")
    total_active=len(c.fetchall())
    conn.commit()
    c.execute("select * from emp_detail where Status='deactive' ")
    total_deative=len(c.fetchall())
    conn.commit()
    c.execute("select * from emp_report ")
    total_leave=len(c.fetchall())
    conn.commit()
    c.execute("select * from emp_report where Approve='Reject' ")
    total_emp_deative=len(c.fetchall())
    conn.commit()
    c.execute("select * from emp_report where Approve='approved' ")
    total_emp_ative=len(c.fetchall())
    conn.commit()
    
    return render_template("home.html",total_emp=total_emp,total_active=total_active,total_deative=total_deative,total_leave=total_leave,total_emp_deative=total_emp_deative,total_emp_ative=total_emp_ative)

# emplyee dashboard page
@app.route("/emp_home.html",methods=["POST","GET"])
def emp_home():
 try:
    conn=mysql.connect(host="localhost",user="root",passwd="",db="payroll")
    c=conn.cursor()
    c.execute("select * from emp_report where Email='{}'".format(m_email))
    total_emp_leave=len(c.fetchall())
    conn.commit()
    c.execute("select * from emp_report where Approve='Reject' and Email='{}'".format(m_email))
    total_emp_deative=len(c.fetchall())
    conn.commit()
    c.execute("select * from emp_report where Approve='approved' and Email='{}'".format(m_email))
    total_emp_ative=len(c.fetchall())
    conn.commit()
    year_date=int(date[:4])
    month_date=int(date[5:7])
    day_date=int(date[8:])
    d = datetime.date(year_date,month_date,day_date)
    l_date = d.replace(day = calendar.monthrange(d.year, d.month)[1])
    f_date= datetime.date(year_date,month_date,day_date).replace(day=1)

    c.execute("select Leave_Day from emp_report where Email='{}' and Approve='approved' and Date BETWEEN '{}' AND '{}';".format(m_email,f_date,l_date))
    emp_leave_count=c.fetchall()
    emp_leave_count=sum([j for i in emp_leave_count for j in i])
    try:
        x=datetime.date.today()
        # print("x = ",x)
        y=x+relativedelta(months=1)
        # print("y = ",y)
        f_date_y=str(y)
        # print("f_date_x = ",f_date_y)
        y=datetime.date(int(f_date_y[:4]),int(f_date_y[5:7]),int(f_date_y[8:])).replace(day=1)
       
        z=x+relativedelta(months=-1)
        salary_mnth=z.strftime("%B")
        salary_year=z.strftime("%Y")
        c.execute(f"SELECT `Allowance`, `Deduction`, `Total_Salary` FROM `salary` WHERE Email='{m_email}' and Month='{salary_mnth}' and Year='{salary_year}'")
        emp_salary=c.fetchall()
        last_salary=emp_salary[0][2]
        emp_allowance=emp_salary[0][0]
        emp_dedution=emp_salary[0][1]
        return render_template("emp_home.html",to_send=total_emp_leave,total_emp_deative=total_emp_deative,total_emp_ative=total_emp_ative,last_salary=last_salary,emp_allowance=emp_allowance,emp_dedution=emp_dedution)
    except:
        return render_template("emp_home.html",to_send=total_emp_leave,total_emp_deative=total_emp_deative,total_emp_ative=total_emp_ative,last_salary=0,emp_allowance=0,emp_dedution=0)
 except:
     return render_template("emp_home.html",to_send=total_emp_leave,total_emp_deative=total_emp_deative,total_emp_ative=total_emp_ative,last_salary=0,emp_allowance=0,emp_dedution=0)

# returning emp_leave.html page
@app.route("/emp_leave.html",methods=["POST","GET"])
def emp_leave():
    return render_template("emp_leave.html")

# returning emp_pass_change.html page
@app.route("/emp_pass_change.html",methods=["POST","GET"])
def emp_pass_change():
    return render_template("emp_pass_change.html")

# returning admin_pass_change.html page
@app.route("/admin_pass_change.html",methods=["POST","GET"])
def admin_pass_change():
    return render_template("admin_pass_change.html")

# returning admin_emp_report.html page
@app.route("/admin_emp_report.html",methods=["POST","GET"])
def admin_emp_report():
    return render_template("admin_emp_report.html")

# returning admin_salary_report.html page
@app.route("/admin_salary_report.html",methods=["POST","GET"])
def admin_salary_report():
    output_salary_report=0
    return render_template("admin_salary_report.html",output_salary_report=output_salary_report)
    

# returning index.html page
@app.route("/index.html",methods=["POST","GET"])
def home_index():
    return render_template("index.html")

# returning emp_salary_report.html page
@app.route("/emp_salary_report.html",methods=["POST","GET"])
def emp_salary_report():
    return render_template("emp_salary_report.html")

# returning admin_leave_report.html page
@app.route("/admin_leave_report.html",methods=["POST","GET"])
def admin_leave_report():
    
    return render_template("admin_leave_report.html")

# admin leave page
@app.route("/admin_leave_report",methods=["POST","GET"])
def admin_leave_report1():
    conn=mysql.connect(host="localhost",user="root",passwd="",db="payroll")
    c=conn.cursor()
    output=request.form.to_dict()
    month=output['month']
    year=output['year']
    name=output['name'].lower()
    c.execute(f"select * from emp_report where  Name='{name}' and Year='{year}' and Month='{month}' ")
    emp_salary=c.fetchall()
    if len(emp_salary)==0:
        return render_template("admin_leave_report.html",show_alert=True)
    table_name=["Name","Email","Leave Day","Date","Reason","Status","Approve"]
    emp_salary=[j for i in emp_salary for j in i]
    # x=dict(table_name,emp_salary)
    table = {table_name[i]: emp_salary[i] for i in range(len(table_name))}
    return render_template("leave_report.html",result=table)

# admin emplyee report page
@app.route("/admin_emp_report",methods=["POST","GET"])
def admin_emp_report1():
    conn=mysql.connect(host="localhost",user="root",passwd="",db="payroll")
    c=conn.cursor()
    output=request.form.to_dict()
    email=output['email']
    name=output['name'].lower()
    c.execute(f"select * from emp_detail where Email='{email}' and Name='{name}' ")
    emp_salary=c.fetchall()
    if len(emp_salary)==0:
        return render_template("admin_emp_report.html",show_alert=True)
    table_name=["Name","Address","City","Pincode","Mobile","Degree","Designation","Salary","Bank no","Email","Password","Status","Branch","Empid"]
    emp_salary=[j for i in emp_salary for j in i]
    # x=dict(table_name,emp_salary)
    table = {table_name[i]: emp_salary[i] for i in range(len(table_name))}
    del table["Password"]
    return render_template("emp_info.html",result=table)

# employee salary dashbord
@app.route("/emp_salary_report",methods=["POST","GET"])
def emp_salary_report1():
    conn=mysql.connect(host="localhost",user="root",passwd="",db="payroll")
    c=conn.cursor()
    output=request.form.to_dict()
    month=output['month']
    year=output['year']
    c.execute(f"select * from salary where Email='{m_email}' and Month='{month}' and Year='{year}'")
    emp_salary=c.fetchall()
    if len(emp_salary)==0:
        return render_template("emp_salary_report.html",show_alert=True)
    table_name=["Name","Email","Allowance","Deduction","Total Salary","Month","Year","Status"]
    emp_salary=[j for i in emp_salary for j in i]
    # x=dict(table_name,emp_salary)
    table = {table_name[i]: emp_salary[i] for i in range(len(table_name))}
    return render_template("emp_salary.html",result=table)
    
# admin salary monitor and search
@app.route("/admin_salary_report",methods=["POST","GET"])
def admin_salary_report1():
    conn=mysql.connect(host="localhost",user="root",passwd="",db="payroll")
    c=conn.cursor()
    output=request.form.to_dict()
    month=output['month']
    year=output['year']
    name=output['name'].lower()
    c.execute(f"select * from salary where Name='{name}' and Month='{month}' and Year='{year}'")
    emp_salary=c.fetchall()
    if len(emp_salary)==0:
        return render_template("admin_salary_report.html",show_alert=True)
    table_name=["Name","Email","Allowance","Deduction","Total Salary","Month","Year","Status"]
    emp_salary=[j for i in emp_salary for j in i]
    # x=dict(table_name,emp_salary)
    table = {table_name[i]: emp_salary[i] for i in range(len(table_name))}
    return render_template("admin_salary.html",result=table)

# employee password change
@app.route("/emp_pass_cng",methods=["POST","GET"])
def emp_pass_cng():
    conn=mysql.connect(host="localhost",user="root",passwd="",db="payroll")
    c=conn.cursor()
    output=request.form.to_dict()
    old_pass=output["old_pass"]
    new_pass=output["pass"]
    email=output["email"]
    c.execute("select * from emp_detail where Email='{}' AND Password='{}'".format(email,old_pass))
    check=(c.fetchall())
    if len(check)==1:
        c.execute("UPDATE emp_detail SET Password='{}' WHERE Email='{}'".format(new_pass,email))
        conn.commit()
        return render_template("emp_pass_change.html",show_alert=True)
    else:
        return render_template("emp_pass_change.html",show_wrong=True)

# admin password change 
@app.route("/admin_pass_cng",methods=["POST","GET"])
def admin_pass_cng():
    conn=mysql.connect(host="localhost",user="root",passwd="",db="payroll")
    c=conn.cursor()
    output=request.form.to_dict()
    old_pass=output["old_pass"]
    new_pass=output["pass"]
    email=output["email"]
    c.execute("select * from admin_detail where Email='{}' AND Password='{}'".format(email,old_pass))
    check=(c.fetchall())
    if len(check)==1:
        c.execute("UPDATE emp_detail SET Password='{}' WHERE Email='{}'".format(new_pass,email))
        conn.commit()
        return render_template("admin_pass_change.html",show_alert=True)
    else:
        return render_template("admin_pass_change.html",show_wrong=True)

# employee leave application
@app.route("/leave_application",methods=["POST","GET"])
def leave():
    global day,date
    conn=mysql.connect(host="localhost",user="root",passwd="",db="payroll")
    c=conn.cursor()
    output=request.form.to_dict()#{'reason:"sedfsgdf","date":"20012-12-15","days":"10"'}
    reson=output["reason"]
    day=output["days"]
    date=output["date"]
    c.execute("SET GLOBAL event_scheduler=ON;")
    # print("date = ",date,type(date))
    year_date=int(date[:4])
    month_date=int(date[5:7])
    day_date=int(date[8:])

    c.execute("select Name from emp_detail where Email='{}' ".format(m_email))
    name=c.fetchall()
    # conn.commit()
    name=name[0][0]
    conn.commit()
    c.execute("select * from emp_report where Email='{}'".format(m_email))
    
    total_emp_leave=len(c.fetchall())
    d = datetime.date(year_date,month_date,day_date)
    l_date = d.replace(day = calendar.monthrange(d.year, d.month)[1])
    f_date= datetime.date(year_date,month_date,day_date).replace(day=1)

    c.execute("select Date from emp_report where Email='{}' and Approve='approved' and Date BETWEEN '{}' AND '{}';".format(m_email,f_date,l_date))
    emp_leave_count=len(c.fetchall())
    
    c.execute("select Date from emp_report where Email='{}' and Status='on'".format(m_email))
    emp_app=c.fetchall()
    
    # inserting leave application into the databse
    if emp_leave_count<2:        
        if len(emp_app)==0:
            c.execute('''INSERT INTO `emp_report`(`Name`, `Email`, `Leave_Day`, `Date`, `Reason`,`Status`,`Approve`,`Month`,`Year`) VALUES ('{}','{}','{}','{}','{}','on','approved',MONTHNAME('{}'),YEAR('{}'))'''.format(name,m_email,day,date,reson,date,date))
            conn.commit()
            c.execute("update emp_detail set `Status`='deactive'  where Email='{}'".format(m_email))
            conn.commit()
            c.execute('''CREATE EVENT IF NOT EXISTS `emp_detail_{}`
            ON SCHEDULE AT '{}' + INTERVAL {} DAY 
            ON COMPLETION NOT PRESERVE
            DO UPDATE `emp_detail` SET `Status`='active' WHERE Email='{}';'''.format(m_email,date,day,m_email))
            conn.commit()
            c.execute('''CREATE EVENT IF NOT EXISTS `emp_report_{}`
            ON SCHEDULE AT '{}' + INTERVAL {} DAY 
            ON COMPLETION NOT PRESERVE
            DO UPDATE `emp_report` SET `Status`='off' WHERE Email='{}';'''.format(m_email,date,day,m_email))
            conn.commit()
            return render_template("emp_leave.html")+'<script> alert("LEAVE APRROVED");</script>'
            
            
        else:
            c.execute('''INSERT INTO `emp_report`(`Name`, `Email`, `Leave_Day`, `Date`, `Reason`,`Status`,`Approve`,`Month`,`Year`) VALUES ('{}','{}','{}','{}','{}','Reject','Reject',MONTHNAME('{}'),YEAR('{}'))'''.format(name,m_email,day,date,reson,date,date))
            conn.commit()
            return render_template("emp_leave.html")+'<script> alert("LEAVE REJECTED (Already Applied)");</script>'
    else:
        c.execute('''INSERT INTO `emp_report`(`Name`, `Email`, `Leave_Day`, `Date`, `Reason`,`Status`,`Approve`,`Month`,`Year`) VALUES ('{}','{}','{}','{}','{}','Reject','Reject',MONTHNAME('{}'),YEAR('{}'))'''.format(name,m_email,day,date,reson,date,date))
        conn.commit() 
        return render_template("emp_leave.html")+'<script> alert("LEAVE REJECTED(Already take 2 leaves this month)");</script>'


if __name__=='__main__':
   app.run(debug=True,port=5000)