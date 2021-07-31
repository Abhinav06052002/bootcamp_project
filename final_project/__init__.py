from flask import Flask
from flask import render_template, request
import psycopg2
from datetime import datetime

app = Flask("Todo")

@app.route("/")
def welcome():
    return render_template("welcome.html")



@app.route("/page2", methods = ["POST"])
def hello():
    global usrnm
    global usrid
    usrnm = request.form['username']
    pwd = request.form['password']
    conn=psycopg2.connect("dbname = todo")
    cur=conn.cursor()
    cur.execute("insert into people (username, password) values (%s,%s)",(usrnm,pwd))
    cur.execute(f"select p.id from people p where username = '{usrnm}';")
    usrid = cur.fetchone()[0] 
    conn.commit()
    cur.close()
    conn.close()
    return render_template("todolist.html")
    
@app.route("/page201", methods = ["POST"])
def log_check():
    global usrnm
    global usrid
    logusr = request.form['username']
    logpwd = request.form['password']
    conn=psycopg2.connect("dbname = todo")
    cur=conn.cursor()
    cur.execute(f"select p.password from people p where username = '{logusr}';") 
    actpwd = cur.fetchone()[0]
     
    if logpwd == actpwd :
        usrnm = logusr
        cur.execute(f"select p.id from people p where username = '{usrnm}';")
        usrid = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return render_template("todolist.html")
    else :
        return render_template("welcome.html")      
   
    
@app.route("/page3", methods = ["POST"])
def day_select():
    global day
    day = request.form['day']
    tasks = execution()
    return render_template("table.html",
                            tasks = tasks,
                            day = day)
                            
@app.route("/page4", methods = ["POST"])
def add_task():
    global tsk
    global d_t
    global usrid
    tsk = request.form['task']
    d_t = request.form['time']
    conn=psycopg2.connect("dbname = todo")
    cur=conn.cursor()
    
    cur.execute(f"insert into {day} (task,due_time,status,person) values (%s,%s,%s,%s)", (tsk,d_t,'pending',usrid))
     
    conn.commit()
    cur.close()
    conn.close()
    tasks = execution()
    return render_template("table.html",
                            day = day,
                            tasks = tasks)                              

@app.route("/page5/<tk>", methods = ["POST"])
def remove_task(tk):
    conn=psycopg2.connect("dbname = todo")
    cur=conn.cursor()
    cur.execute(f"delete from {day} where task = '{tk}';")
    conn.commit()
    cur.close()
    conn.close()
    tasks = execution()
    return render_template("table.html",
                            day = day,
                            tasks = tasks)



    
def execution():
    due_check()
    conn=psycopg2.connect("dbname = todo")
    cur=conn.cursor()
    cur.execute(f"select d.task, d.due_time, d.status from {day} d, people p where d.person=p.id;")
    tasks = cur.fetchall()    
    conn.commit()
    cur.close()
    conn.close()
    return tasks

def due_check():
    conn=psycopg2.connect("dbname = todo")
    cur=conn.cursor()
    cur.execute(f"select pyindex from std where dow = '{day}';")
    day_index = cur.fetchone()[0]
    cur.execute(f"select due_time from {day} where person = {usrid}")
    d_t_lst = cur.fetchall()
    for i in range(0, len(d_t_lst)):
        if (datetime.today().weekday() > day_index) or (datetime.today().weekday() == day_index and int(datetime.now().strftime("%H%M")) > d_t_lst[i][0]) :
            cur.execute(f"update {day} set status = 'overdue' where due_time = {d_t_lst[i][0]};")
    
    conn.commit()
    cur.close()
    conn.close()      
    return    
        



  
if __name__ == "__main__":
    app.run()   
    
    
    
    
    
    
    
    
      
