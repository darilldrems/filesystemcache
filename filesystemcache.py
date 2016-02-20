import json
import pickle
import os
import datetime

class FileSystemCache():
	def __init__(self, folder_path):
		self.file_name = folder_path + "cache.txt"
		#create file if not exist and initialize it with empty dict
		f = open(self.file_name, 'w')
		initial = {}
		pickle.dump(initial, f)


	def get(self, key):
		dict_obj = self.__get_file_content()

		row = dict_obj.get(key)

		if self.__is_expired_row(row):
			self.delete(key)
			return None

		return row['value']

	def has(self, key):
		dict_obj = self.__get_file_content()

		if key in dict_obj:
			#check expiration before returning true
			row = dict_obj.get(key)

			if self.__is_expired_row(row):
				self.delete(key)
				return False
			return True

		return False

	def delete(self, key):
		dict_obj = self.__get_file_content()

		dict_obj.pop(key)

		self.__put_file_content(dict_obj)
		pass

	def update(self, key, value, lifespan=3600):
		dict_obj = self.__get_file_content()

		dict_obj['key'] = {
			'value': value,
			'_created_at': datetime.datetime.now(),
			'_lifetime': lifespan
		}
		
		self.__put_file_content(dict_obj)

	def add(self, key, value, lifespan=3600):
		dict_obj = self.__get_file_content()

		if dict_obj.get(key) is None:
			dict_obj[key] = {
				'value': value,
				'_created_at': datetime.datetime.now(),
				'_lifetime': lifespan
			}
		
		self.__put_file_content(dict_obj)

	def inc(self, key, delta=1):
		dict_obj = self.__get_file_content()

		if dict_obj.get(key) is None:
			row = dict_obj.get(key)

			if type(row['value']) == int:
				dict_obj[key]['value'] += delta
				self.__put_file_content(dict_obj)

	def reset(self):
		dict_obj = {}
		self.__put_file_content(dict_obj)

	#private methods
	def __get_file_content(self):
		try:
			f = open(self.file_name, 'r')

			return pickle.load(f)
		except IOError:
			print("unable to open file")
			return None

	def __put_file_content(self, new_content):
		try:
			f = open(self.file_name, 'w')
			
			pickle.dump(new_content, f)

		except IOError:
			print("unable to write to file")
			return None

	def __is_expired_row(self, row):
		#check expiration date and if passed 
		_created_at = row['_created_at']
		#total amount of seconds for the existence of the store value
		_lifetime = row['_lifetime']

		diff = datetime.datetime.now() - _created_at

		in_seconds = diff.total_seconds()

		if in_seconds > _lifetime:
			return True

		return False

if __name__ == "__main__":
	cache = FileSystemCache("/home/ridwan/projects/")

	cache.add("name", "ridwan olalere")

	print cache.get("name")



