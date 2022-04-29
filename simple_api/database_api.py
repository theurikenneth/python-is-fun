import flask
from flask import request, jsonify
import sqlite3

app = flask.Flask(__name__)
app.config["DEBUG"] = True


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


# results are stored in an SQLite database (books.db)
# the function connects to the database and selects all columns of the table books
@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('books.db')                          # connects to the database using sqlite3
    conn.row_factory = dict_factory                             # lets the connection use the dict_factory function
    cur = conn.cursor()                                         # moves through the db to pull our data
    all_books = cur.execute('SELECT * FROM books;').fetchall()  # pulls all available data

    return jsonify(all_books)


# create a function that creates an error page if the user encounters an error or inputs undefined route
# code 200 means "OK" while code 404 means "Not Found"
@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route('/api/v1/resources/books', methods=['GET'])
def api_filter():
    query_parameters = request.args                 # grabs all the query parameters provided in the URL

    # allows for the filtering by three fields: id, published and author
    id = query_parameters.get('id')
    published = query_parameters.get('published')
    author = query_parameters.get('author')

    query = "SELECT * FROM books WHERE"             # there is definition of both the query and the filter list
    to_filter = []

    if id:
        query += ' id=? AND'                        # id is added to both the query and filter list
        to_filter.append(id)
    if published:
        query += ' published=? AND'                 # published is added to both the query and filter list
        to_filter.append(published)
    if author:
        query += ' author=? AND'                    # author is added to both the query and filter list
        to_filter.append(author)
    if not (id or published or author):             # if the user provides none of the parameters,
        return page_not_found(404)                  # there is the "404 Not Found" page

    # perfects the query by removing the trailing:` AND and cap the query with the ;`
    # required at the end of all SQL statements:
    query = query[:-4] + ';'

    # finally there is execution of the query
    conn = sqlite3.connect('books.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()

    results = cur.execute(query, to_filter).fetchall()

    return jsonify(results)


app.run()

# links to the browser
""" http://127.0.0.1:5000/api/v1/resources/books/all
http://127.0.0.1:5000/api/v1/resources/books?author=Connie+Willis
http://127.0.0.1:5000/api/v1/resources/books?author=Connie+Willis&published=1993
http://127.0.0.1:5000/api/v1/resources/books?published=2010
"""
