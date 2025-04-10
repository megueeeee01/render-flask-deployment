from flask import Flask, request, render_template

app = Flask(__name__)

# Define routes
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        return render_template('index.html', name=name)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
