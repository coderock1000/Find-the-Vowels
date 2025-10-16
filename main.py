from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def count_vowels():
    result = None
    if request.method == 'POST':
        text = request.form['text']
        vowels = 'aeiouAEIOU'
        count = sum(1 for char in text if char in vowels)
        result = f'Number of vowels: {count}'
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
 