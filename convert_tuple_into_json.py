import json

def convert_tuple_to_json(tup, obj):
    for a, b,c,d in tup:
    	# print ('a:', a)
    	# print ('b:', b)
    	# print ('b:', c)
    	# print ('b:', d)
        obj.setdefault(b, []).append(c)
    return obj

tups = [(1, 'topic_a', '418', 1), (1, 'topic_a', '2028', 1), (1, 'topic_a', '30.3239', 1),  (2, 'topic_b', 'What’s your', 2), (2, 'topic_b', 'Have ', 2), (2, 'topic_b', 'What’s', 2), (3, 'topic_c', 'About ', 3), (3, 'topic_c', 'Creating', 3), (3, 'topic_c', 'Building ', 3), (3, 'topic_c', 'Query ', 3), (3, 'topic_c', 'Starter ', 3)]

json_dictionary = {}

data_obj = convert_tuple_to_json(tups, json_dictionary)

for topic in data_obj:
	print(topic, ":")
	for subtopic in json_dictionary[topic]:
  		print(subtopic)

