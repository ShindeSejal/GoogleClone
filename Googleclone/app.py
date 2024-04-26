from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample search results
search_results = [
    {"title": "Python - Wikipedia", "url": "https://en.wikipedia.org/wiki/Python_(programming_language)"},
    {"title": "Welcome to Python.org", "url": "https://www.python.org/"},
    {"title": "Python Tutorial - W3Schools", "url": "https://www.w3schools.com/python/"}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form.get('query')
    # Here you can implement your search logic
    # For simplicity, we're just returning some sample results
    return render_template('search.html', query=query, results=search_results)

if __name__ == '__main__':
    app.run(debug=True)
