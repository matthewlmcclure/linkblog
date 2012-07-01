from flask import Flask, request
from plumbum import local
from plumbum.cmd import ls, mkdir, wc, wget
from shorten import dehydrate
app = Flask(__name__)
app.debug=True

@app.route('/', methods=['POST'])
def links():
    if request.method == 'POST':
        href_dir = hrefdir()
        mkdir['-p', href_dir]()
        with local.cwd(local.cwd / href_dir):
            wget['-E', '-H', '-k', '-K', '-p', href()]()
    return ""

def href():
    return request.form['href']

def hrefdir():
    pipeline = ls['-1'] | wc['-l']
    index = int(pipeline())
    return 'links/%s' % dehydrate(index)

if __name__ == '__main__':
    app.run("0.0.0.0")
