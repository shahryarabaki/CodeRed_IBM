import json
import requests
import re

def abstract_extractor(link_dbpedia):
	
	link_dbpedia = link_dbpedia.replace("resource", "data")
	link_dbpedia = link_dbpedia + ".xml"
	print (link_dbpedia)
	
	response = requests.get(link_dbpedia)
	#print (response.headers['content-type'])
	text =((response.content))
	# abs = '<dbo:abstract xml:lang="en">'
	#print (text)
	try:
		result = re.search('<dbo:abstract xml:lang="en">(.*)<\/dbo:abstract>', str(text))
		value = ((result.group(1).split('\\n'))[0])
		return (value)
	except AttributeError:
		return ("No abstract extracted\n")

def concept_parser(input_json):
	"""
	this function parse input concept json string into folowing output hashmap
	INPUT: 
		input_json:
			result from emotion parsing each 5 seconds of dictionary
	OUTPUT:
		concept_map:
			resulting hashmap of key as emotion and value as the score of emotion
	"""
	input_string = json.loads(input_json)
	concept_text_map = {}
	list_dbplink = []
	list_text = []
	list_abstracts = []
	for concepts in input_string['concepts']:
		#print (concepts)
		list_dbplink.append(concepts['dbpedia'])
	for concepts in input_string['concepts']:
		#print (concepts)
		list_text.append(concepts['text'])
	print (list_text)
	for link in list_dbplink:
		val = abstract_extractor(link)
		list_abstracts.append(val)
	
	print (list_abstracts)
	
	
	concept_text_map = dict(zip(list_text, list_abstracts))
	print (concept_text_map)
	



	# abstract = abs.group(0)
	# print (abstract)
	
	
	
	
	
if __name__ == "__main__":
	input_string =open('nlp_test_out.txt').read()
	concept_parser(input_string)
