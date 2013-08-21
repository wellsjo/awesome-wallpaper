# Awesome Wallpaper
# By Wells Johnston

# This script downloads the best city and earth wallpapers to the
# same directory it is kept in.  Run it with a CRON job however
# often you want your wallpaper to change.

'''
You can edit this stuff
'''

# Picture Type (you can change either to 'False')
nature_pictures = True
city_pictures = True

# How many photos do you want kept in your folder (max:50)?
wallpaper_limit = 10


'''
Don't change anything below this
'''


import urllib2, os, sys, glob, json
image_extensions = ['.jpg', '.jpeg', '.png']


# gets the current directory
dirname = os.path.dirname(sys.argv[0])

# Takes a picture type and retrieves the top 50 pictures for that type
def getImages(picture_type):
    url = 'http://www.reddit.com/r/' + picture_type + 'porn/top/.json?limit=50/'
    images_json = json.loads(urllib2.urlopen(url).read())
    results = images_json['data']['children']
    images = []
    for image in results:
        url = image['data']['url']
        extension = url[url.rfind('.'):].lower()
        print(extension)
        if extension in image_extensions:
            images.append({ 'title': image['data']['title'].replace(' ', '_').replace('/', '_') + extension,
                            'url': url,
                            'picture_type': picture_type })
    return images

# Saves an image directly from a url, also takes a name
def saveImage(url, title):
    f = open(dirname + '/' + title, 'wb')
    f.write(urllib2.urlopen(url).read())
    f.close()

# Fetch image location information and organize data for images to be saved
todays_images = []
save_images = []
if nature_pictures and city_pictures:
    todays_images.append(getImages('earth'))
    todays_images.append(getImages('city'))
    count = 0
    while len(todays_images[0]) > 0 and len(todays_images[1]) > 0:
        save_images.append(todays_images[count % 2].pop())
        count += 1
elif nature_pictures and not city_pictures:
    save_images = getImages('earth')
elif city_pictures and not nature_pictures:
    save_images = getImages('city')

# Delete old wallpapers
old_wallpapers = [x for x in glob.glob(dirname + '/*') if x[-3:] != '.py']
while len(old_wallpapers) + len(save_images) > wallpaper_limit and len(old_wallpapers) > 0:
    os.remove(old_wallpapers.pop())

# Save the new wallpapers
saved_image_count = 0
for image in save_images:
    if len(old_wallpapers) + saved_image_count < wallpaper_limit:
        saveImage(image['url'], image['title'])
        saved_image_count += 1
    else:
        break

new_wallpapers = [x for x in glob.glob(dirname + '/*') if x[-3:] != '.py']

