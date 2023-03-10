from flask import Flask, render_template  # Import Flask to allow us to create our app


app = Flask(__name__)    # Create a new instance of the Flask class called "app"

 #http://127.0.0.1:5000

@app.route('/play/<int:num>/<color>')          # The "@" decorator associates this route with the function immediately following
def index(num,color):
    return render_template("index.html", var_num = num,var_color = color)# Return the string 'Hello World!' as a response



@app.route('/<path:path>') #went to the wrong site.
def wrong_path(path):
    return "this is the wrong site"



if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.