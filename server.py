from flask import Flask,render_template,request,redirect
import csv
app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/<string:pagename>")
def htmlpage(pagename):
    return render_template(pagename)




@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data=request.form.to_dict()
            write_to_csv(data)
            return redirect("/index2.html")
        except:
            print("data not stored in database")
    else:
        return "Something went wrong.Try again"


def write_to_csv(data):
    with open("database.csv","a") as database:
        name=data["name"]
        email=data["email"]
        message=data["contact_message"]
        csv_writer=csv.writer(database,delimiter=",",quotechar=";",quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name,email,message])

