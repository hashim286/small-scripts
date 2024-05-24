The point of this script is to take some output from ibadmin CLI that shows records available for a certain search string such as "dns search test" which may return the record type and then the record itself followed by the IP address

	  A test.example.com 127.0.0.1

This output should be added into "input.txt" and then the script should be run which will generate a YAML file from the output from ibadmin and use that YAML for the jinja template to output to delete the records as well as a backout in case you need to undo the change