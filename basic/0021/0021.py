from hashlib import sha256
import os
from hmac import HMAC

def encrypt_password(password, salt = None):
	if salt is None:
		salt = os.urandom(8)
	assert 8 == len(salt)
	assert isinstance(salt, str)

	if isinstance(password, unicode):
		password = password.encode('utf-8')
	assert isinstance(password, str)

	result = password
	for i in range(10):
		# result = HMAC(result, salt, sha256).hexdigest()
		result = HMAC(result, salt, sha256).digest()

	# print result
	return salt + result
		
def validate_password(hashed, input_password):
	return hashed == encrypt_password(input_password, salt=hashed[:8])

if __name__ == '__main__':
	password = 'you-never-know'
	en_key = encrypt_password(password)
	key = raw_input('please enter your key: ')
	if validate_password(en_key, key):
		print "Authentication passed"
	else:
		print "Wrong key!"
