import flask
from flask import Flask, render_template, request

from processing import process


app = Flask(__name__)


@app.route('/', methods=["get", "post"])
def index():
    message = ''
    if request.method == "POST":
        # загружаем переменные
        # IW
        IW = request.form.get("IW")
        try:
            IW = float(IW)
        except:
            IW = 46
            message += 'Некорректный ввод. Установлено значение по умолчанию. '
        # IF
        IF = request.form.get("IF")
        try:
            IF = float(IF)
        except:
            IF = 141
            message += 'Некорректный ввод. Установлено значение по умолчанию. '
        # VW
        VW = request.form.get("VW")
        try:
            VW = float(VW)
        except:
            VW = 10
            message += 'Некорректный ввод. Установлено значение по умолчанию. '
        # FP
        FP = request.form.get("FP")
        try:
            FP = float(FP)
        except:
            FP = 80
            message += 'Некорректный ввод. Установлено значение по умолчанию. '
        # соберем все в строку DataFrame
        depth, width = process(IW, IF, VW, FP)
        depth = round(depth, 2)
        width = round(width, 2)
        message += f"Глубина шва {depth} мм. Ширина шва {width} мм."
    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run()