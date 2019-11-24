import json
import time
import threading
from urllib.request import urlopen, Request

import redis
import pickle
# conn = redis.Redis('localhost')
redisClient = redis.StrictRedis(host='localhost', port=6379)


class BaseGenericsService(object):

	def success(**kwargs):
		result = dict(success=True)
		result.update(kwargs)
		return result

	def failure(**kwargs):
		result = dict(success=False)
		result.update(kwargs)
		return result



class ThreadingCall(object):
	
	def __init__(self, request_url, headers):

		# 5 Minutes wait
		self.interval = 300
		self.request_url = request_url
		self.headers = headers

		thread = threading.Thread(target=self.execute, args=())
		thread.daemon = True
		thread.start()

	def execute(self):
		
		while True:
			
			req = Request(self.request_url, headers=self.headers)
			response = urlopen(req)
			result = response.read()

			redisClient.set('nifty_gainers', result)

			time.sleep(self.interval)



class NiftyGainersService(BaseGenericsService):

	@classmethod
	def retrieve(cls, **kwargs):

		try:

			headers = {
				'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)' 'AppleWebKit/537.11 (KHTML, like Gecko)' 'Chrome/23.0.1271.64 Safari/537.11',
				'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
				'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
				'Accept-Encoding': 'none',
				'Accept-Language': 'en-US,en;q=0.8',
				'Connection': 'keep-alive'
			}

			request_url = 'https://www.nseindia.com/live_market/dynaContent/live_analysis/gainers/niftyGainers1.json'


			#Create 3 Threads
			for item in range(3):
				ThreadingCall(request_url, headers)

			redis_data = redisClient.get('nifty_gainers')

			if redis_data:
				result = json.loads(redis_data)
				data = result.get('data')
			
			else:
				data = list()
			
			return cls.success(data=data)

		except Exception as e:
			print(e)
			return cls.failure(
				code = 500,
				error='Data could not be fetched'
			)

	@classmethod
	def filter(cls, **kwargs):

		try:

			redis_data = redisClient.get('nifty_gainers')

			if redis_data:
				result = json.loads(redis_data)
				data = result.get('data')
			
			else:
				data = list()
			
			return cls.success(data=data)

		except Exception as e:
			print(e)
			return cls.failure(
				code = 500,
				error='Data could not be fetched'
			)
