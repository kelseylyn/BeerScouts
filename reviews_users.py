# adapted from https://github.com/jadianes/winerama-recommender-tutorial
import sys, os
import pandas as pd
import datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "winerama.settings")

import django
django.setup()

from reviews.models import Review, Beer


def save_review_from_row(review_row):
    review = Review()
    review.id = review_row[0]
    review.user_id = review_row[1]
    review.beer_id = review_row[2]
    review.rating = review_row[3]
    review.abv = review_row[4]
    review.ibu = review_row[5]
    review.something = review_row[6]
    review.beer_name = review_row[7]
    review.beer_style = review_row[8]
    review.brewery_id = review_row[9]
    review.ounces = review_row[10]
    review.save()


if __name__ == "__main__":

    if len(sys.argv) == 2:
        print "Reading from file " + str(sys.argv[1])
        reviews_df = pd.read_csv(sys.argv[1])
        print reviews_df

        reviews_df.apply(
            save_review_from_row,
            axis=1
        )

        print "There are {} reviews in DB".format(Review.objects.count())

    else:
        print "Please, provide Reviews file path"
