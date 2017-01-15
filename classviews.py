from flask import Flask,render_template
from flask.views import View
class GnericView(View):
    def __init__(self,template):
        self.tempalte = template
        super().__init__()

    def dispatch_request(self):
        # 相当于之前地return render_template()
        return render_template(self.tempalte)

app = Flask(__name__)


app.add_url_rule(
    # 第一个是路由规则 第二个是视图函数名 提供给url_for使用的 之后地都是传递给init的参数
    '/',view_func=GnericView.as_view(
        'home',template='home.html'
    )
)


if __name__ == '__main__':
    app.run()
