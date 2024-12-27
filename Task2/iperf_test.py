import parser

class TestSuite():
	def test_iperf_client_connection(self, client):
		output, error, error_server = client
		p_output, p_error = parser.parser(output, error)

		assert not error_server, f"Server error: {error_server}"
		assert not p_error, f"Client returned an error: {p_error}"
		assert p_output, "Parsed output is empty!"

		for line in p_output:
			assert line["Transfer"] > 1 and line["Bitrate"] > 11.2
