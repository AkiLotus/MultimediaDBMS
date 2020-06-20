import backend_tree
import random
import time

number_of_records = 10000
number_of_queries = 10000

abs_limit = 100

max_number_of_dimensions = 20
tolerances = [0.0, 0.01, 0.05, 0.1, 0.2, 0.25, 1.0/3, 0.5, 2.0/3, 0.75, 0.8]

for number_of_dimensions in range(1, max_number_of_dimensions+1):
	print('Number of dimensions = {}'.format(number_of_dimensions))
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

	for tolerance in tolerances:
		print('- Tolerance = {}'.format(tolerance))
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

		print('  Brute force execution time: {:.3f} seconds.'.format(bf_time))
		print('  KD-Tree execution time: {:.3f} seconds.'.format(kd_build + kd_query))
		print('  - KD-Tree build time: {:.3f} seconds.'.format(kd_build))
		print('  - KD-Tree query time: {:.3f} seconds.'.format(kd_query))

		correct = 0
		error = 0.0
		total = len(result_bf)
		for i in range(total):
			if (result_bf[i] == result_kd[i]):
				correct += 1
			else:
				# print('Wrong answer on query {}'.format(i+1))
				# print('Query: {}'.format(test_data[i]))
				# print('Expected = {} | Answer = {}'.format(result_bf[i], result_kd[i]))
				error += (result_kd[i] - result_bf[i]) / max(1, result_bf[i]) / total
		print('  Correctness of KD-Tree: {}/{}'.format(correct, total))
		print('  Average relative error: {:.6f}'.format(error))
		# print('result_bf: {}'.format(result_bf))
		# print('result_kd: {}'.format(result_kd))