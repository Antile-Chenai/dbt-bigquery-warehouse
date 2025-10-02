WITH source AS (
    SELECT * FROM `bigquery-public-data.new_york_airbnb.listings`
)
SELECT
    id,
    name,
    host_id,
    neighbourhood_group,
    neighbourhood,
    room_type,
    price,
    minimum_nights,
    number_of_reviews,
    last_review
FROM source
WHERE price < 1000;
