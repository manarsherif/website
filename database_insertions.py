import os
from photos.models import Photo, ImageClass
from django.core.files import File
import datetime


images_directory = '/home/menna/photos/media/photos'
features_directory = '/home/menna/photos/media/features'

for root, dirs, files in os.walk(images_directory):
    for direcory in dirs:
        image_class = ImageClass()
        image_class.name=direcory.lower()
	image_class.slug=direcory.lower()
        images_dir= images_directory+'/'+direcory
        if os.listdir(images_dir):
            image_class.save()
            print 'class ' + direcory + ' is added to database'
            for filee in os.listdir(images_dir):
                if filee.endswith('.jpg'):
                    ph = Photo()
		    ph.category=image_class.name
                    ph.name = filee
		    ph.slug=filee
                    ph.image.save(filee, File(open(images_dir+'/' + filee, 'r')))
		    ph.description = " "
		    ph.price = 100
		    ph.stock = 100
		    ph.available = True
		    ph.created = datetime.date.today()
		    ph.updated = datetime.date.today()
                    feature_file_dir= features_directory+'/'+direcory+'/'+filee+'.txt'
                    ph.features.save(filee, File(open(feature_file_dir, 'r')))
                    ph.save()

