import pytest
from weconnect import create_app

@pytest.fixture
def client():
  '''creates the testing client instance'''
  test_app = create_app(testing=True)
  client = test_app.test_client()
  yield client

@pytest.fixture
def routes(request):
  '''creates url endpoints'''
  class Routes:
    version = 3
    base_url = 'api/v{}'.format(version)

    @classmethod
    def url(cls, prefix, endpoint):
      return cls.base_url + prefix + endpoint

    def auth(self, endpoint):
      return self.url('/auth', endpoint)

    def business(self, endpoint):
      return self.url('/businesses', endpoint)
    
    def review(self, endpoint):
      return self.business(endpoint) + '/reviews'

  routes = Routes()
  yield routes
