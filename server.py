from flask import Flask, render_template, request, redirect
app = Flask(__name__)   # our index route will handle rendering our form

@app.route('/')
def index():
  return render_template("index.html")  # this route will handle our form submission
# notice how we defined which HTTP methods are allowed by this route

@app.route('/success', methods=['POST'])
def success():
   
   name = request.form['name']
   location = request.form['location']
   language = request.form['language']
   comment = request.form['comment']
   # redirects back to the '/' route
   return render_template('success.html',name=name, location=location, language=language, comment=comment)

app.run(debug=True) # run our server	# run the app in debug mode
	
