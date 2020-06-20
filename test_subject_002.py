import backend_tree
import random
import time

number_of_records = 1000
number_of_queries = 1000

abs_limit = 10

number_of_dimensions = 20
tolerances = [random.random() for _ in range(10000)]
tolerances.sort()

training_data = []
test_data = []
for _ in range(number_of_records):
	record = [random.randint(0, abs_limit) for _ in range(number_of_dimensions)]
	training_data.append(record)

for _ in range(number_of_queries):
	record = [random.randint(0, abs_limit) for _ in range(number_of_dimensions)]
	test_data.append(record)

# print('train: {}'.format(training_data))
# print('test: {}'.format(test_data))

result_bf = []

# calculate by bf
start_time = time.time()
for query in test_data:
	result = None
	for data in training_data:
		if result is None: result = backend_tree.raw_distance(query, data)
		else: result = min(result, backend_tree.raw_distance(query, data))
	result_bf.append(result)
end_time = time.time()

bf_time = end_time - start_time

print('Brute force execution time: {:.3f} seconds.'.format(bf_time))

for tolerance in tolerances:
	result_kd = []

	# calculate by kd
	start_time_1 = time.time()
	tree = backend_tree.KDTree(training_data)
	end_time_1 = time.time()

	start_time_2 = time.time()
	for query in test_data:
		_, result = tree.search(data=backend_tree.Data(query), tolerance=tolerance)
		result_kd.append(result)
	end_time_2 = time.time()

	kd_build = end_time_1 - start_time_1
	kd_query = end_time_2 - start_time_2

	correct = 0
	error = 0.0
	total = len(result_bf)
	for i in range(total):
		if (result_bf[i] == result_kd[i]):
			correct += 1
		else:
			error += (result_kd[i] - result_bf[i]) / max(1, result_bf[i]) / total
			
	print('{:.9f},{:.9f},{:.9f},{:.9f}'.format(tolerance, kd_build + kd_query, correct/total, error))