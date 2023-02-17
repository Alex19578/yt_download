from pytube import YouTube
from flask import Flask, request, render_template, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('/index.html')

@app.route('/download', methods=['POST'])
def download():
    try:
        url = request.form['url']
        video = YouTube(url)
        stream = video.streams.get_highest_resolution()
        stream.download('/User/Downloads/')
        filename = video.title + '.mp4'
        return send_file('/User/Downloads/' + filename, as_attachment=True)
    except:
        return render_template('/index.html')

if __name__ == '__main__':
    app.run(debug=True)
