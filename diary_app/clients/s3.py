from boto import connect_s3
from boto.s3.connection import S3Connection
from boto.s3.key import Key

def get_connection():
	"""
	For EC2 hosts this is managed by roles
	IAM users must add the correct AWS tokens to their .bash_profile
	"""
	try:
		return connect_s3()
	except Exception as e:
		raise Exception("Unable to connect to S3:", e)
		# return S3Connection(AWS_ACCESS_KEY, AWS_SECRET_KEY)

def get_bucket(connection, bucket_name):
	return connection.get_bucket(bucket_name, validate=False)

def get_bucket_name_from_filename(filename, bucket_names):
	connection = get_connection()
	for name in bucket_names:
		bucket = get_bucket(connection, name)
		files = bucket.list()
		for f in files:
			if f.name == filename:
				return bucket.name
	return None

def download_file(file_key, file_path, bucket_name):
	# items_log.info("Downloading file: %s" % file_key)
	k = Key(get_bucket(get_connection(), bucket_name))
	k.key = file_key
	k.get_contents_to_filename(file_path)
	# items_log.info("Downloading complete!")

def upload_file(file_key, file_path, bucket_name):
	# items_log.info("Uploading file: %s" % file_key)
	k = Key(get_bucket(get_connection(), bucket_name))
	k.key = file_key
	k.set_contents_from_filename(file_path)
	# items_log.info("Upload complete!")

def get_all_files(bucket_name):
	bucket = get_bucket(get_connection(), bucket_name)
	files = bucket.list()
	filenames = []
	for f in files:
		filenames.append(f.name)
	return filenames

def get_download_url(bucket, path, expiry):
	return get_connection().generate_url(
	    expires_in=int(expiry), #seconds w max of 7 days
	    method='GET',
	    bucket=bucket,
	    key=path,
	    query_auth=True,
	    force_http=False
	)