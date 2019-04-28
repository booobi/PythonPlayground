from urllib import urlopen

webpage = urlopen('https://www.bbc.com/weather/727011')
for l in webpage:
    if 'wr-day__weather-type-description wr-js-day-content-weather-type-description wr-day__content__weather-type-description--opaque' in l:
        lft = l.find('description">')
        rght = l.find('</div><div class="wr-day__weather-type">')
        weather = l[lft+len('description">'):rght]
        print weather
        break


from urllib import urlretrieve
webpage = urlretrieve('https://www.bbc.com/weather/727011')
print webpage