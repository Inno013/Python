from fuzzywuzzy import fuzz

# ratio : membandingkan kesamaan dari keseluruhan string
rasio = fuzz.ratio('Salatiga','salatiga hati beriman')
print('rasionya :',rasio,'%')

# partial_ratio : membandingkan kemiripan dari string secara parsial/sebagian
parsial_rasio = fuzz.partial_ratio('Salatiga','salatiga hati beriman')
print('parsial rasionya :',parsial_rasio,'%')

# token_set_ratio : membandingkan menggunakan ratio tanpa memperhatikan case sensitive
set_ratio = fuzz.token_set_ratio('Salatiga','salatiga hati beriman')
print('token set rasionya :', set_ratio,'%')

# partial_token_set_ratio : membandingkan menggunakan partial tanpa memperhatikan case sensitive
partial_set_ratio = fuzz.partial_token_set_ratio('Salatiga','salatigahati beriman')
print('partial token set rasionya :',partial_set_ratio,'%')