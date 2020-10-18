from pyngrok import ngrok
from flask import Flask
from flask import request
from flask import render_template
import time

app = Flask(__name__)

@app.route("/")
def getIP():
    if request.headers.getlist("X-Forwarded-For"):
        ip = request.headers.getlist("X-Forwarded-For")[0]
        print(f"[*] A User has clicked your link ! [{ip}] \n")
        return render_template("Index.html")
    else:
        ip = request.remote_addr
        print(f"[*] A User has clicked your link ! [{ip}] \n")
        return render_template("Index.html")

if __name__ == '__main__':
    print("NovaOS Technology")
    time.sleep(4)
    public_url = ngrok.connect()
    tunnels = ngrok.get_tunnels()
    public_url = tunnels
    print(f"\nNGROK LINK --> {tunnels[1]}\n")
    app.run(port=80)