import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# Creating some test data as a list of dictionaries
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring,'
                       'the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'year_published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'To wound the autumnal city.',
     'year_published': '1975'}
]


# A route to the homepage
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
    <p>A prototype API for distant reading of science fiction novels.</p>'''


# A route to return all the available entries in our catalog
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)


@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL
    # If ID is provided, assign it to a variable
    # If no ID is provided, display an error in the browser
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No id field provided. PLease specify an id."

    # Create an empty list for the results
    results = []

    # Loop through the data and match the results that fit the requested ID
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)

    # Use the jsonify function from Flask to convert our list of python dictionaries to the JSON format
    return jsonify(results)


app.run()

""" Links to the books by id
http://127.0.0.1:5000/api/v1/resources/books?id=3
http://127.0.0.1:5000/api/v1/resources/books?id=2
http://127.0.0.1:5000/api/v1/resources/books?id=1
"""
