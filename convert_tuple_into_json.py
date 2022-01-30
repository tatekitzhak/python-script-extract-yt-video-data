import json

data = [(1, 'topic_a', '418', 1), (1, 'topic_a', '2028', 1), (1, 'topic_a', '30.3239', 1),  (2, 'topic_b', 'What’s your', 2), (2, 'topic_b', 'Have ', 2), (2, 'topic_b', 'What’s', 2), (3, 'topic_c', 'About ', 3), (3, 'topic_c', 'Creating', 3), (3, 'topic_c', 'Building ', 3), (3, 'topic_c', 'Query ', 3), (3, 'topic_c', 'Starter ', 3)]

def convert_tuple_to_json(tup, obj):
    for a, b,c,d in tup:
    	# print ('a:', a)
    	# print ('b:', b)
    	# print ('b:', c)
    	# print ('b:', d)
        obj.setdefault(b, []).append(c)
    return obj
      
# Driver Code    
tups = [(1, 'topic_a', '4, 6, 8, 9, 10, 12, 14, 15, 16, 18', 1), (1, 'topic_a', '20, 21, 22, 24, 25, 26, 27, 28', 1), (1, 'topic_a', '30.32, 33, 34, 35, 36, 38, 39', 1), (1, 'topic_a', '40, 42, 44, 45, 46, 48, 49', 1), (1, 'topic_a', '50, 51, 52, 54, 55, 56, 57, 58', 1), (1, 'topic_a', '60, 62, 63, 64, 65, 66, 68, 69', 1), (1, 'topic_a', '70, 72, 74, 75, 76, 77, 78, 80, 81, 82, 84, 85, 86, 87, 88', 1), (1, 'topic_a', '90, 91, 92, 93, 94, 95, 96, 98, 99', 1), (1, 'topic_a', '100, 102, 104, 105, 106, 108, 110', 1), (2, 'topic_b', 'What kind of music are you into', 2), (2, 'topic_b', 'What music did you like when you were younger', 2), (2, 'topic_b', 'What’s your favorite band / singer', 2), (2, 'topic_b', 'Have you been to any concerts recently', 2), (2, 'topic_b', 'What’s your favorite album', 2), (3, 'topic_c', 'About _-Creating Text Topics', 3), (3, 'topic_c', 'Creating Topics from Searches', 3), (3, 'topic_c', 'Building Queries', 3), (3, 'topic_c', 'Query Builder', 3), (3, 'topic_c', 'Recommended Topics', 3), (3, 'topic_c', 'Managing Topics', 3), (3, 'topic_c', 'Hierarchical Topics', 3), (3, 'topic_c', 'Exporting Topics', 3), (3, 'topic_c', 'Importing Topics', 3), (3, 'topic_c', 'Starter Pack Topics', 3), (3, 'topic_c', '123.567.2345', 3), (3, 'topic_c', '344-567-1234', 3), (3, 'topic_c', '256)098-9856', 3), (3, 'topic_c', 'FAQs', 3), (3, 'topic_c', 'test.com', 3)]
json_dictionary = {}

data_obj = convert_tuple_to_json(data, json_dictionary)
# print(data_obj)

for topic in data_obj:
	print(topic, ":", json_dictionary[topic][0])

