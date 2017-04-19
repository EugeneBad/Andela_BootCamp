""" Function obtains descriptions of each season of the T.V show Homeland using the itunes search API. """

import requests


def homeland():
    print('\t\tHOMELAND: Hands down the best T.V show ever!\n')

    for season in range(1, 6):

        # Initiate requests object whose value is the response json object from the itunes API.
        result = requests.get('https://itunes.apple.com/search?',
                              params={'term': 'Homeland, Season {}'.format(season),
                                      'media': 'tvShow',
                                      'limit': 1})

        # Parse JSON object
        result_parsed = result.json()

        # Filter out the 'longDescription' key.
        season_description = result_parsed['results'][0]['longDescription']

        print('SEASON: {}'.format(season) + '\n' + season_description + '\n\n')

    print('Go Get a Copy!')


if __name__ == '__main__':
    homeland()
