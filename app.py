from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_WPM(text, takenTime):
    pass

@app.route('/')
def index():
    default = "Hello There!"
    return render_template('index.html', default=default)

@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        default = "Hello There!"
        text = request.form.get('text')
        print("H")
        takenTime = request.form.get('timeTaken')
        print(takenTime)
        if default == text:
            calculate_WPM(text, takenTime)
            return render_template('index.html', status = "Win", text=text, default=default)
        else:
            return render_template('index.html', status = "Lose", text=text, default=default)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)