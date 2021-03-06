from flask import Flask, render_template, request
from YoutubeSearch import youtube_search
from pprint import pprint

app = Flask(__name__)

video_link = []

@app.route('/')
def home():
    # grab my api data
    return render_template('search.html')


@app.route('/results/<user_input>', methods=['POST'])
def results(user_input):

    user_input = request.form['search_on_youtube']

    youtube_results = youtube_search(user_input)
    titles = youtube_results[1]
    video_id = youtube_results[2]
    image_url = youtube_results[0]


    video_link = []

    for item in video_id:
        video_link.append("https://www.youtube.com/embed/{}".format(item))

    pprint(video_link)

    return render_template('results.html',
                           image = image_url,
                           titles = titles,
                           user_input = user_input,
                           video_link = video_link,
                           )

if __name__ == '__main__':
    app.run(debug=True)
