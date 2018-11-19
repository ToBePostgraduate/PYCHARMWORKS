import time
def application(req, res):
    res('200 ok', [('Content-Type', 'text/html;charset=UTF-8'),
                   ])
    time.sleep(0.1)
    print(req['QUERY_STRING'])
    if 'name=asd&password=123' == req['QUERY_STRING']:
        yield ('登陆成功'.encode('utf-8'))
    else:
        yield ('登陆失败'.encode('utf-8'))
    print(req)
    #python wifiwsgi.py --http-socket :8000 --plugin python3 --wsgi-file database.py