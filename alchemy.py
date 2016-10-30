import json
from watson_developer_cloud import AlchemyLanguageV1

API_KEY = 'd468d0c84418f10b0d5cb84ba7985d90bcf0db71'


def emotion(text_input):
	alchemy_language = AlchemyLanguageV1(api_key=API_KEY)
	return json.dumps(alchemy_language.emotion(text=text_input), indent=2)

def keyword(text_input):
	alchemy_language = AlchemyLanguageV1(api_key=API_KEY)
	return json.dumps(alchemy_language.keywords(text=text_input), indent=2)

def concept(text_input):
	alchemy_language = AlchemyLanguageV1(api_key=API_KEY)
	return (json.dumps(alchemy_language.concepts(text=text_input), indent=2))
	
if __name__ == '__main__':
	
	infile = open('nlp_test.txt').read()
	value = concept(infile)
	print (value)
	outfile =  open('nlp_test_out.txt', 'w')
	outfile.write(value)
	outfile.close()