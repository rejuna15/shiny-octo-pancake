from flask import Flask, request
from URL import URL
from DB import DB

app = Flask(__name__)


@app.route('/ShortUrl', methods=['GET'])
def ShortenURL():
    url = request.args.get('url')
    url_obj = URL()
    is_valid = url_obj.parse_url(url)
    short_url = "https://url_short.com/"

    if not is_valid:
        return "URL is invalid"
    else:
        with DB().cursor() as cur:
            cur.execute(f"Select * from urls where `long_url`='{url}'")
            # Check if url has already been shortened
            if cur.rowcount > 0:
                short_url = cur.fetchone()[2]
                return " Already shortened to " + short_url
            else:
                cur.execute(f"Insert into urls(`long_url`) Values ('{url}')")
                url_id = cur.lastrowid
                short_url += url_obj.encode(
                    url_id + 10000000000)  # Adding 10000000000 (10 billion) to generate a six character url
                cur.execute(f"Update urls set short_url='{short_url}' where id='{url_id}'")
        return "Shortened URL is " + short_url


@app.route('/OriginalUrl', methods=['GET'])
def GetOriginalURL():
    short_url = request.args.get('short_url')
    url_obj = URL()
    res=None
    if short_url is not None:
        url_id = url_obj.decode(short_url)
        with DB().cursor() as cur:
            statement = f"Select * from urls where id='{url_id - 10000000000}'"
            cur.execute(statement)
            res = cur.fetchone()
    return "Original URL is "+ res[1] if res is not None else "No URL found"


if __name__ == '__main__':
    app.run()
