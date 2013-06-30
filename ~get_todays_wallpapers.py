# gets the best 20 wallpapers every day

import urllib2, re, os, sys, glob

# a list of sites you want to extract pictures from
# defaults are Reddit's cityporn and earthporn
image_sources = ['http://www.reddit.com/r/earthporn', 'http://www.reddit.com/r/cityporn']

# the number of pictures you want to be downloaded every time
image_limit = 30

# destructive downloading means that old wallpaper images are overwritten by new ones
# if set to False, all the wallpapers will be saved.
destructive = True

# modify this to extract the right url pattern.  
# Default is set to http://i.imgur.com/{picture_name}.jpg
image_regex = re.compile('http://i.imgur.com/[a-zA-Z1-9]+\.jpg')

results = []
for url in image_sources:
    html = urllib2.urlopen(url).read()
    tmp_results = image_regex.findall(html)[0:image_limit/len(image_sources)]
    results += tmp_results
results = set(results)

dirname = os.path.dirname(sys.argv[0])
old_images = glob.glob(dirname + '/*.jpg')

for url in results:
    image = url[url.rfind('/') + 1:]
    print(image)
    f = open(dirname + '/' + image, 'wb')
    f.write(urllib2.urlopen(url).read())
    f.close()

new_image_count = len(glob.glob(dirname + '/*.jpg'))

if destructive:
    for image in old_images:
        if new_image_count > image_limit:
            os.remove(image)
            new_image_count -= 1
        else:
            break
