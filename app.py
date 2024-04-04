from flask import Flask, render_template, request

from utubevideo import download_video

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    output_path = './downloads'
    return download_video(url, output_path)


if __name__ == "__main__":
    app.run(debug=True)

