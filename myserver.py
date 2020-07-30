from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)



#database code Lecture 268-270 --- Lecture 270 csv files
# def write_to_file(data):
# 	with open('database.txt', mode = 'a') as database:
# 		email = data["email"]
# 		subject = data["subject"]
# 		message = data["message"]
# 		file = database.write(f'\n{email},{subjext},{message}')


#Submit Form Code Lecture Videos 267-269
# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
# 	if request.method == 'POST':
# 		data = request.form.to_dict()
# 		write_to_file(data)
# 		return redirect('add html file here')
# 	else:
#       return 'Sorry, try again!'