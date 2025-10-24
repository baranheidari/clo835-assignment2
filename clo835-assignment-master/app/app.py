import os
import socket
from flask import Flask
import pymysql
app=Flask(__name__)
def db_ok():
    host=os.environ.get("DB_HOST","mysql")
    user=os.environ.get("DB_USER","app")
    password=os.environ.get("DB_PASSWORD","apppass")
    name=os.environ.get("DB_NAME","appdb")
    try:
        conn=pymysql.connect(host=host,user=user,password=password,database=name,connect_timeout=2)
        conn.close()
        return True
    except Exception:
        return False
@app.route("/")
def index():
    color=os.environ.get("APP_COLOR","blue")
    host=socket.gethostname()
    dbstatus="ok" if db_ok() else "down"
    return f"""<html><head><title>CLO835</title></head><body style="margin:0;background:{color};color:#111;font-family:Arial,Helvetica,sans-serif"><div style="display:flex;flex-direction:column;align-items:center;justify-content:center;height:100vh"><h1>CLO835 App</h1><h2>Color: {color}</h2><h3>Container: {host}</h3><h3>DB: {dbstatus}</h3></div></body></html>"""
if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080)
