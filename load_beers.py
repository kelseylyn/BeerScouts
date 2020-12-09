# adapted from https://github.com/jadianes/winerama-recommender-tutorial
import sys, os
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "beerscouts.settings")

import django
django.setup()

from reviews.models import Beer


def save_beer_from_row(beer_row):
    beer = Beer()
    beer.id = beer_row[0]
    beer.abv = beer_row[1]
    beer.ibu = beer_row[2]
    beer.name = beer_row[3]
    beer.style = beer_row[4]
    beer.ounces = beer_row[5]
    beer.save()


if __name__ == "__main__":

    if len(sys.argv) == 2:
        print("Reading from file " + str(sys.argv[1]))
        beers_df = pd.read_csv(sys.argv[1])
        print(beers_df)

        beers_df.apply(
            save_beer_from_row,
            axis=1
        )

        print("There are {} beers".format(Beer.objects.count()))

    else:
        print("Please, provide Beer file path")
