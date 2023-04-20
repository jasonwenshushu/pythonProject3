
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/blog/<int:blog_id>')
def blog_detail(blog_id):
    return render_template('blog_detail.html', blog_id=blog_id)


if __name__ == '__main__':
    app.run(debug=True)
