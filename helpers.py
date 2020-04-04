import requests
import random
import os
import pickle

OBJECT_LIST_FILE = 'objects_list.data'


def get_object_ids():
	print('getting objects')
	try:
		req = requests.get('https://collectionapi.metmuseum.org/public/collection/v1/objects')
		return req.json()['objectIDs']
		print('getting objects finished')
	except requests.exceptions.RequestException as e:
		raise SystemExit(e)


def create_object_list(object_IDs):
	print('creating object list')
	with open('objects_list.data', 'wb') as filehandle:
		pickle.dump(object_IDs, filehandle)
	print('objects list created')
	

def load_object_list():
	print('loading object list')
	with open('objects_list.data', 'rb') as filehandle:
		return pickle.load(filehandle) 
	print('objects list laded')

def get_image_data(object_IDs):
	print('gettin image data')
	finished = False
	while not finished:
		object_ID = random.choice(object_IDs)
		print(f'checking object {object_ID}')
		url = 'https://collectionapi.metmuseum.org/public/collection/v1/objects/' + str(object_ID)
		try:
			req = requests.get(url)
			image_url = req.json()['primaryImageSmall']			
			is_public = req.json()['isPublicDomain']
			title = req.json()['title']
			artist = req.json()['artistDisplayName']
			classification = req.json()['classification']
			object_IDs.remove(object_ID)
			print(f'Object: object_id {object_ID}, image_url {image_url}, title {title}, artist {artist}, is_public {is_public}, classification {classification}')
		except requests.exceptions.RequestException as e:
			print(e)
		finally:
			finished = image_url and is_public and title

	print(f'Object found: object_id {object_ID}')
	return object_IDs, object_ID, image_url, title, artist


def create_twitter_text(title, artist):
	print('creating text message')
	if artist:
		twitter_text = f'''
		Title: {title}
		Artist: {artist}
		'''
	else:
		twitter_text = f'''
		Title: {title}
		'''
	print(f'Text message: {twitter_text}')
	return twitter_text


def update_object_list(object_IDs):
	print('updating object list')
	if os.path.exists('objects_list.data'):
		os.remove('objects_list.data')
	create_object_list(object_IDs)
	print(f'object list length {len(object_IDs)}')
	print('object list updated')