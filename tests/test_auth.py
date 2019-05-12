import json
class TestAuth:
  def test_get_users(self, client, routes):
    '''testing get all users request'''
    rv = client.get(routes.auth('/users'))
    assert json.loads(rv.data) == {'user': 'one'}