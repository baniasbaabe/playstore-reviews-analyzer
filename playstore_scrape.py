from urllib import parse
from google_play_scraper import Sort, reviews

class PlaystoreReview:
    def __init__(self, url, lang="en", country="us", count=100, stars=None) -> None:
        if parse.parse_qs(parse.urlparse(url).query)["id"]:
            self.id = parse.parse_qs(parse.urlparse(url).query)["id"][0]
        else:
            raise ValueError(f"URL has no id field. Check again. Given URL: {url}")
        self.lang = lang
        self.country = country
        self.count = count
        self.stars = stars

    def get_reviews(self):
        result, _ = reviews(
            self.id,
            lang=self.lang, # defaults to 'en'
            country=self.country, # defaults to 'us'
            sort=Sort.NEWEST, # defaults to Sort.NEWEST
            count=self.count, # defaults to 100
            filter_score_with=self.stars # defaults to None(means all score)
        )

        return result