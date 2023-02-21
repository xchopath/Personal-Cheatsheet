import gzip

def strdecompress(string):
	decompressed_data = gzip.decompress(string)
	decompressed_string = str(decompressed_data, 'utf-8')
	return decompressed_string

def strcompress(string):
	compressed_data = gzip.compress(bytes(string, 'utf-8'))
	return compressed_data

jsonstr = str(json.dumps({'name': 'test'}))
comdata = strcompress(jsonstr)
decdata = json.loads(strdecompress(comdata))
