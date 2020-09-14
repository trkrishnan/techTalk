from flask import Flask
# Flask class constructor takes the name of  
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function tells the application which URL should call this function
@app.route('/sampleAPI', methods = ['POST'])
def sampleResponse():
    return " Server received request. Thank you \n"

#main  function
if __name__ == '__main__':
# run() method of Flask class runs the application  
    app.run(port= 8888)
