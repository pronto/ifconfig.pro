from flask import Flask, render_template, send_from_directory, request
import os, socket, time, re
socket.setdefaulttimeout(3)

app = Flask(__name__)
app.debug=False
def lookup(addr):
    try:
        return socket.gethostbyaddr(addr)
    except socket.herror:
        return "No dns record for host", "No dns record for host", "No dns record for host"


@app.route('/')
def main():
    ip=request.remote_addr
    agent=str(request.user_agent)
    if "curl" in agent:
        return request.remote_addr + "\n"
    elif "PowerShell" in agent:
        return request.remote_addr + "\n"
    else:
        hostname = lookup(ip)[0]
        return render_template('main.html', 
                ip=request.remote_addr, 
                hostname=hostname , 
                agent=agent,
                lang=request.accept_languages ,
                enco=request.accept_encodings,
                xip=request.access_route[0]
                )
    
    
@app.route('/ip.host')
def iphost():
    hostname=lookup(request.remote_addr)[0]
    return request.remote_addr + " - " + hostname + "\n"


@app.route('/host')
def host():
    hostname=lookup(request.remote_addr)[0]
    return hostname + "\n"

@app.route('/help')
def help():
    f=open('/home/pronto/python/templates/main.html', 'r')
    out = f.read()
    start = out.find('Fea')
    end =  out.find('<!--')
    return out[start:end]

@app.route('/freedooooom')
def freedom():
    return render_template('freedom.html')

@app.route('/robots.txt')
def robots():
    return render_template('robots.txt')

@app.route('/ping')
def ping():
    return render_template('ping.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0')

