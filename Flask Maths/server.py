from flask import Flask, render_template, request, jsonify
from Maths.mathematics import summation, subtraction, multiplication

app = Flask("Mathematics Problem Solver")

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

@app.route("/sum")
def sum_route():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    
    if not (is_number(num1) and is_number(num2)):
        return jsonify(error="Please provide numerical inputs for 'num1' and 'num2'."), 400
    
    result = summation(float(num1), float(num2))
    return str(result)

@app.route("/sub")
def sub_route():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    
    if not (is_number(num1) and is_number(num2)):
        return jsonify(error="Please provide numerical inputs for 'num1' and 'num2'."), 400
    
    result = subtraction(float(num1), float(num2))
    return str(result)

@app.route("/mul")
def mul_route():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')
    
    if not (is_number(num1) and is_number(num2)):
        return jsonify(error="Please provide numerical inputs for 'num1' and 'num2'."), 400
    
    result = multiplication(float(num1), float(num2))
    return str(result)

@app.route("/")
def render_index_page():
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
