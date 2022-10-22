from flask import Flask, render_template,send_from_directory,request,redirect
import os,csv
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     print(url_for('static',filename='favicon.ico'))
#     return render_template('index.html')

@app.route('/')
def my_world():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message} ')

def write_to_csv(data):
    with open('database.csv' ,newline='',mode='a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2,delimiter=',' ,quotechar='"',quoting=csv.QUOTE_MINIMAL) 
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('./thankYou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong'

# @app.route('/index.html')
# def index():
#     return render_template('index.html')

# @app.route('/components.html')
# def components():
#     return render_template('components.html')

# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/works.html')
# def works():
#     return render_template('works.html')

# @app.route('/work.html')
# def work():
#     return render_template('work.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')



# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    #return render_template('login.html', error=error)

# @app.route('/blog')
# def blog():
#     return 'My thoughts'

# @app.route('/favicon.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'favicon.ico')

# @app.route('/blog/2020/dogs')
# def blog2():
#     return 'My thoughts about dogs'