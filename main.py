# setup, owner name, access_token and headers

infile = open("token.txt", 'r')
access_token = infile.read()
headers = {'Authorization': "Token " + access_token}
