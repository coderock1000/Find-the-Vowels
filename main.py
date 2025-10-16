from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def count_vowels():
    result = None
    if request.method == 'POST':
        text = request.form['text']
        vowels = 'aeiou'
        counts = {v: text.lower().count(v) for v in vowels}
        total = sum(counts.values())
        result = counts
        result['total'] = total
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
