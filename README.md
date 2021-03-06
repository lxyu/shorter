# Shorter

[![Build Status](https://travis-ci.org/lxyu/shorter.png?branch=master)](https://travis-ci.org/lxyu/shorter)

Simple flask app to create a short url service.

Creates a robust url shorten service with zero config.


## Usage

Use pip to install shorter:

```bash
$ pip install shorter
```

Run with 'shorter':

```bash
$ shorter
```

Simple test:

```bash
$ curl --form "url=http://google.com" localhost:5000
cpYNkF
$ curl localhost:5000/cpYNkF
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to target URL: <a href="http://google.com">http://google.com</a>.  If not click the link.
```

You may also try visit it using a browser.


## Deploy

Deploy with gunicorn is easy:

```bash
$ gunicorn -w 4 -b 127.0.0.1:5000 shorter:app
```

## Customize

Use a `shorter_config.py` to customize database uri:

```python
# shorter_config.py example
SQLALCHEMY_DATABASE_URI = "sqlite:///shorter.db"
```

