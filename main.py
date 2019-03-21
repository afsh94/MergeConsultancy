from flask import Flask, render_template, request
import requests

app = Flask("__name__")

# key = "2af99839c0ee910e8c65be3af00512ed-7caa9475-11dfbcd9" #'YOUR API KEY HERE'
# sandbox ="sandbox7bd313e94e3f46fbbe2c1f82dccca286.mailgun.org" #'YOUR SANDBOX URL HERE'/domain name
# recipient = "f.mahmood@qmul.ac.uk" #'YOUR EMAIL HERE'

def send_simple_message(email, name):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox7bd313e94e3f46fbbe2c1f82dccca286.mailgun.org/messages",
        auth=("api", "2af99839c0ee910e8c65be3af00512ed-7caa9475-11dfbcd9"),
        data={"from": "Merge Consultancy <mailgun@sandbox7bd313e94e3f46fbbe2c1f82dccca286.mailgun.org>",
              "to": [email],
              "subject": "Thanks for signing up, "+name,
              "text": "You've signed up to receive information on upcoming workshops and events!"
              })


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/subs")
def signUp():
    return render_template("signUp.html")

@app.route("/output", methods=["POST"])
def sUp():
    # read the posted values from the UI
    name = request.form['your_name']
    email = request.form['your_email']

    # validate the received values
    if name and email:
        send_simple_message(email,name)
        return render_template("thanks.html")

if   __name__ == "__main__":
    app.run(debug=True)
