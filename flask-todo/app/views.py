from app import app
from flask import render_template



@app.route('/')
def index():
    form = TodoForm()
    todos = Todo.objects.order_by('-time')
    return render_template("index.html",todos=todos, form=form)

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'),404

if __name__ == '__main__':
    app.run()


