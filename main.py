from flask import Flask, jsonify ,request, render_template 
app=Flask(__name__)

@app.route("/")
def chat():
    return render_template("chat.html")





@app.route('/api/sum', methods=['POST'])
def sum_number():
    if not request.is_json:
        return jsonify({"error": "expected JSON body with 'a' and 'b'"}), 400
    data = request.get_json()
    try:
        a=data.get('a')
        b=data.get('b')
        #accept numbers or numeric strings
        a=float(a)
        b=float(b)
    except Exception:
        return jsonify({"error": "invalid numbers provided"}), 400
    result = a + b
    return jsonify({"sum": result})
if __name__ == '__main__':
    app.run(debug=True)