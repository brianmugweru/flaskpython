from flask import Flask

app = Flask("the-box")

@app.route('api/category/books', methods=['GET', 'POST'])
def book_api():
    return 'some resource'

if __name=__ == '__main__':
    app.run()
