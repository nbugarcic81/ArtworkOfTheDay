import random
from twitter import twitter_post
import wget
import os
from helpers import get_object_ids, create_object_list, load_object_list, update_object_list, get_image_data, create_twitter_text, OBJECT_LIST_FILE

TEMP_PHOTO = './photo.jpg'


def main():
	print('Starting main')
	if not os.path.exists(OBJECT_LIST_FILE):
		object_IDs = get_object_ids()
		create_object_list(object_IDs)
	else:
		object_IDs = load_object_list()

	object_IDs, object_ID, image_url, title, artist = get_image_data(object_IDs)
	update_object_list(object_IDs)
	twitter_text = create_twitter_text(title, artist)

	if os.path.exists(TEMP_PHOTO):
			os.remove(TEMP_PHOTO)

	try:
		print('downloading')
		wget.download(image_url, TEMP_PHOTO)
		print('image downloaded')
		print('posting on twitter')
		twitter_post(twitter_text, TEMP_PHOTO)
		print('posted')
	except Exception as e:
		print(str(e))
	finally:
		if os.path.exists(TEMP_PHOTO):
			os.remove(TEMP_PHOTO)
			print('temp file deleted')
			update_object_list(object_IDs)
			print('object_list_updated')


if __name__ == '__main__':
	main()

