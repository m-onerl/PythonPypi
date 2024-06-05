import requests

class StreamingApiRequestFactory:
    def __init__(self, api_key):
        self.api_key = api_key

    def search_shows_by_filters(self, country, show_type, series_granularity="show", order_by="original_title", output_language="en", order_direction="asc", genres_relation="and"):
        url = f"https://streaming-availability.p.rapidapi.com/shows/search/filters"
        headers = {
            'X-RapidAPI-Key': self.api_key,
            'X-RapidAPI-Host': "streaming-availability.p.rapidapi.com"
        }
        params = {
            'country': country,
            'show_type': show_type,
            'series_granularity': series_granularity,
            'order_by': order_by,
            'output_language': output_language,
            'order_direction': order_direction,
            'genres_relation': genres_relation
        }
        response = requests.get(url, headers=headers, params=params)
        return response.json()

    def search_shows_by_title(self, country, title, show_type="movie", output_language="en", series_granularity="show"):
        url = "https://streaming-availability.p.rapidapi.com/shows/search/title"
        headers = {
            "X-RapidAPI-Key": self.api_key,
            "X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
        }
        params = {
            "country": country,
            "title": title,
            "output_language": output_language,
            "show_type": show_type,
            "series_granularity": series_granularity
        }
        response = requests.get(url, headers=headers, params=params)
        return response.json()

class StreamingAvailability:
    def __init__(self, api_key):
        self.request_factory = StreamingApiRequestFactory(api_key)

    def search_shows_by_filters(self, country, show_type="movie", series_granularity="show", order_by="original_title", output_language="en", order_direction="asc", genres_relation="and"):
        return self.request_factory.search_shows_by_filters(country, show_type, series_granularity, order_by, output_language, order_direction, genres_relation)

    def search_shows_by_title(self, country, title, show_type="movie", output_language="en", series_granularity="show"):
        return self.request_factory.search_shows_by_title(country, title, show_type, output_language, series_granularity)

class DataProcessor:
    def process_data(self, data):
        processed = {}

        if isinstance(data, list):
            items = data
        elif isinstance(data, dict):
            items = data.get('results', data.get('shows', []))
        else:
            raise ValueError("Unsupported data format")

        for item in items:
            title = item.get('title', 'N/A')
            processed[title] = {
                'overview': item.get('overview', 'N/A'),
                'releaseYear': item.get('releaseYear', 'N/A'),
                'genres': [genre['name'] for genre in item.get('genres', [])],
                'directors': item.get('directors', []),
                'cast': item.get('cast', []),
                'rating': item.get('rating', 'N/A')
            }
        return processed
