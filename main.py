from flask import Flask, render_template
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from YoutubeSearch import youtube_search
#from SpotifySearch import SearchSpot
from pprint import pprint

app = Flask(__name__)

video_link = []

@app.route('/')
def home():
    # grab my api data
    return render_template('search.html')


@app.route('/results/<user_input>')
def results(user_input):
    youtube_results = youtube_search(user_input)
    titles = youtube_results[1]
    video_id = youtube_results[2]
    #video_link = "https://www.youtube.com/embed/{}".format(video_id)

    #image_url = ['snippet.thumbnails.(key).url']
    image_url = youtube_results[0]
    #image = '{}'.format(image_url)


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



# @app.route('/spotifyresults/<user_input>')
# def spotifyresults(user_input):
#     spotify_results = SearchSpot(user_input)
#
#     return render_template ('spotifyresults.html',
#                             spotify_results = spotify_results,
#                             )
#
#pprint(youtube_search('beyonce')[1])

if __name__ == '__main__':
    app.run(debug=True)
