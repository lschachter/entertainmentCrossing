import os

class Config:
	SECRET_KEY = os.environ.get('EC_SECRET_KEY', 'dev')