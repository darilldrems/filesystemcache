#FileSystemCache
A simple python class for caching data in file system.

##Getting Started
FileSystemCache can be installed by manually cloning this repository

```python
	from filesystemcache import FileSystemCache
```

##Using filesystemcache
First, you need to create an instance of the class and supply it with the folder directory you intend to use for storing the data

```python
	cache = FileSystemCache("/home/ridwan/storage/")
```

##Storing data
Filesystemcache allows you to store key value pair with expiration time in number of seconds. The value stored can be any valid python data type. When storing objects you do not need to serialize as filesystem cache handles that for you.

```python
	cache.add(key, value, expiration_in_seconds)
```

##Getting data
Filesystemcache allows you to check if the key has been stored before retrieving it. When the value to be retrieved is expired or not available it returns None

```python
	if cache.has(key)
		result = cache.get(key)

	#or

	result = cache.get(key)
```

###Other functions
Filesystemcache allows you to perform other functions such as increment, update. Hopefully I will get around to add more functions or you can add more functions

```python
	#delta is the value you want to increment by
	cache.inc(key, delta)

	cache.update(key, value)
```

NB: I have not gotten around to write tests for it because I wrote it quickly to deploy with my live application but feel free to write tests and send a pull request.



