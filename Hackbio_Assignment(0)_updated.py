Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Python code that prints Name, Email Slack_username, Biostack and Twitter handle
>>> Name = "Onyijen Ojei"
>>> Email = "ojei.onyijen@gmail.com"
>>> Slack_username = "@Ojei"
>>> Biostack = "Drug Development"
>>> Twitter_handle = "@harryjdon05"
>>>  print("{}, {}, {}, {}, {}".format(Name, Email, Slack_username, Biostack, Twitter_handle))
SyntaxError: unexpected indent
>>> print("{}, {}, {}, {}, {}".format(Name, Email, Slack_username, Biostack, Twitter_handle))
Onyijen Ojei, ojei.onyijen@gmail.com, @Ojei, Drug Development, @harryjdon05
>>> #function to calculate Hamming distance between slack handle and twitter handle
>>> def hammingDist(Slack_username, Twitter_handle):
	i = 0
	count = 0
	while(i < len(Slack_username)):
		if(Slack_username[i] !=Twitter_handle[i]):
			count += 1
		i += 1
	return count

>>> Slack_username = "@Ojei"
>>> Twitter_handle = "@harryjdon05"
>>> print(hammingDist(Slack_username, Twitter_handle))
4
>>> 
