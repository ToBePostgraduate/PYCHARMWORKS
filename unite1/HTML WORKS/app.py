def application(req, res):
    from io import StringIO
    f = StringIO()

    global n
    print('第', n, '次请求\n', file=f)
    n += 1

    for i in req:
        print('<br>', file=f)
        print(i, '=', req[i], file=f)
    res('200 ok', [
        ('Content-Type', 'text/html;charset=UTF-8'),
    ])
    yield bytes(f.getvalue(), 'utf-8')
# python wifiwsgi.py --http-socket :8000 --plugin python3 --wsgi-file database.py
