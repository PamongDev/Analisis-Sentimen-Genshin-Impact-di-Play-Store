from google_play_scraper import app, reviews_all, reviews, Sort
import pandas as pd

scrap_ml = reviews_all(
    'com.miHoYo.GenshinImpact',
    lang='id',
    country='id',
    sort=Sort.MOST_RELEVANT,
    count=1000
)

df_scrap = pd.DataFrame(scrap_ml)

df_reviews_crop = df_scrap.sample(16000)
df_reviews_crop.to_csv('data_scrap_GI_cleaned_cropin16k.csv')