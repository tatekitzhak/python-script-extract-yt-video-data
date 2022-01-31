import json
from error import add, mult
import re



def convert_tuple_to_json(tup, obj):
    for a, b,c,d in tup:
    	# print ('a:', a)
    	# print ('b:', b)
    	# print ('b:', c)
    	# print ('b:', d)
        obj.setdefault(b, []).append(c)
    return obj

def remove_replc_non_alphanumeric(str):

    # Remove all non-word characters (everything except numbers and letters)
    str = re.sub(r"[^\w\s]", '', str)

    # Remove all end of string non alphanumeric characters (i.e: question mark or space)
    str = re.sub(r"[\s|\?]+$", '', str)

    # Replace all runs of whitespace with a single dash
    str = re.sub(r"\s+", '-', str)

    return str

tups = [(1, 'topic_a', '41 8!', 1), (1, 'topic_a', '2 0 2 8 ?', 1), (1, 'topic_a', '$30.3 2 3 9 ', 1),  (2, 'topic_b', 'What’s your ?', 2), (2, 'topic_b', 'Have ad !', 2), (2, 'topic_b', 'What’s this', 2), (3, 'topic_c', 'About you', 3), (3, 'topic_c', 'Creating', 3), (3, 'topic_c', 'Building 1 2 3 45', 3), (3, 'topic_c', 'Query abc', 3), (3, 'topic_c', 'Starter ther', 3)]

json_dictionary = {}

data_obj = convert_tuple_to_json(tups, json_dictionary)

for topic in data_obj:
	print(topic, ":")
	for subtopic in json_dictionary[topic]:
		try:
			s = remove_replc_non_alphanumeric(subtopic)
			print(s)
		except Exception as e:
			raise
		else:
			pass
		finally:
			pass
  		



