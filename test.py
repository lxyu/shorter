import json
import os
import shorter
import string
import unittest

SHORT_URL_LENGTH = 6


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        shorter.app.testing = True
        shorter.app.config['DEBUG'] = True
        shorter.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        shorter.db.create_all()
        self.app = shorter.app.test_client()

    def tearDown(self):
        os.unlink('test.db')

    def testGreeting(self):
        res = self.app.get('/')
        assert res.status_code == 200
        assert b'Welcome to url shorten service!' == res.data

    def testFormShorten(self):
        res = self.app.post('/url', data=dict(url='http://google.com'))
        assert res.status_code == 200
        short = str(res.data, res.charset)
        assert len(short) == SHORT_URL_LENGTH
        assert all(c in string.ascii_letters for c in short)

    def testJsonShorten(self):
        res = self.app.post('/url', content_type='application/json',
                            data='{"url": "http://google.com"}')
        assert res.status_code == 200
        assert 'application/json' == res.content_type

        _json = json.loads(str(res.data, res.charset))
        assert "short" in _json and len(_json["short"]) == SHORT_URL_LENGTH
        assert all(c in string.ascii_letters for c in _json["short"])

    def testDuplicateShorten(self):
        res1 = self.app.post('/url', data=dict(url='http://google.com'))
        res2 = self.app.post('/url', data=dict(url='http://google.com'))
        assert res1.data == res2.data

    def testExpand(self):
        res = self.app.post('/url', data=dict(url='http://google.com'))
        assert res.status_code == 200
        res = self.app.get(b'/' + res.data)
        assert res.status_code == 302
        assert res.headers.get('Location') == 'http://google.com'

    def testNotExistsExpand(self):
        res = self.app.get('/abc')
        assert res.status_code == 404


if __name__ == '__main__':
    unittest.main()
