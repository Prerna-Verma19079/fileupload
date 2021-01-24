# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask,render_template, request, Response
import os
import time
from tqdm import tqdm, trange

app = Flask(__name__)

APP_ROOT=os.path.dirname(os.path.abspath(__file__))
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/uploads', methods=['GET','POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)
    pbar=tqdm(total=100)
    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target,filename])
        for i in range(10):
            time.sleep(0.3)
            pbar.update(10)
            print(pbar)
        pbar.close()
        print(destination)
        file.save(destination)

    return  render_template("complete.html")

@app.route('/delete', methods=['Delete'])
def delete():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target,filename])
        print(destination)
        file.remove(destination)

    return render_template("complete.html")
# Press the green button in the gutter to run the script.
@app.route('/progress')
def progress():
    def generate():
        x = 0

        while x <= 100:
            yield "data:" + str(x) + "\n\n"
            x = x + 10
            time.sleep(0.5)

    return Response(generate(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
