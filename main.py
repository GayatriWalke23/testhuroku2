from flask import Flask, render_template, request

app = Flask(__name__)
print(app)

@app.route('/')
def index():
    #exec(open('main.py').read())
    return "hello world"


if __name__ == "__main__":
    #exec(open('main.py').read())
    app.debug = True
    app.run()


'''git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/GayatriWalke23/testhuroku2.git
git push -u origin main'''
