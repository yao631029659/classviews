from flask import Flask,render_template
from flask.views import MethodView


app = Flask(__name__)


class Userview(MethodView):
    def get(self):
        method='get'
        return render_template(
            'home.html',
            method=method,
        )
    def post(self):
        method='post'
        return render_template(
            'home.html',
            method=method,
        )



app.add_url_rule(
    # 第一个是路由规则 第二个是视图函数名
    '/',view_func=Userview.as_view('home')
)


if __name__ == '__main__':
    app.run()
