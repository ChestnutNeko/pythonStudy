from flask import Flask

app = Flask(__name__)

# 路由解析 通过用户访问的路径，匹配相应的函数
@app.route('/')
def hello_world():
    return 'Hello World! Liz'

@app.route("/user/<name>")
def hello(name):
    return "hello, %s"%name

@app.route("/user/<int:id>")
def hello2(id):
    return "你好，%d号的会员"%id
# debug模式开启

if __name__ == '__main__':
    app.run(debug=True)