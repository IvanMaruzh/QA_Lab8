import re
import copy


def parser(output, error):
	KEYS = ('Interval', 'Transfer', 'Bitrate')
	data_output = re.findall(r'\b([0-9\.\-]+)\s+sec\s+([0-9\.]+)\s+[A-Z]?Bytes\s+([0-9\.]+)\s+[A-Z]?bits/sec\b', output.decode("utf-8"))
	error = error.decode("utf-8")

	formatted_data_output = []
	temp = {}
	for data in data_output:
		temp.clear()
		for idx in range(len(KEYS)):
			if idx == 0:
				temp[KEYS[idx]] = data[idx]
			else:
				temp[KEYS[idx]] = float(data[idx])

		formatted_data_output.append(copy.deepcopy(temp))

	return formatted_data_output, error if error else None
