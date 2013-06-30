# gets the best 20 wallpapers every day

import urllib2, re, os, sys, glob

image_regex = re.compile('http://i.imgur.com/[a-zA-Z1-9]+\.jpg')

earth_response = urllib2.urlopen('http://www.reddit.com/r/earthporn').read()
city_response = urllib2.urlopen('http://www.reddit.com/r/cityporn').read()

results1 = image_regex.findall(earth_response)[0:20]
results2 = image_regex.findall(city_response)[0:20]
results = set(results1 + results2)

dirname = os.path.dirname(sys.argv[0])
old_images = glob.glob(dirname + '/*.jpg')

for url in results:
    image = url[url.rfind('/') + 1:]
    print(image)
    f = open(dirname + '/' + image, 'wb')
    f.write(urllib2.urlopen(url).read())
    f.close()

new_image_count = len(glob.glob(dirname + '/*.jpg'))

for image in old_images:
    if new_image_count > 20:
        os.remove(image)
        new_image_count -= 1
    else:
        break
