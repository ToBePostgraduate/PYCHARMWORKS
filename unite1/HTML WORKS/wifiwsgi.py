from wsgiref.simple_server import make_server
import sys
import getopt

import os


def _help():
    print('''
            支持的参数有
            -h  输出帮助
            --http-socket   需要绑定的socket
            --wsgi-file 符合wsgi规范的文件，作为服务器应用
            --chdir 进入目录
            --module    wsgi模块，配合chdir使用
            
            2018/10/28 v1.0 wifi
            ''')


opts, args = getopt.getopt(sys.argv[1:], 'h', [
    'http-socket=',
    'plugin=',
    'wsgi-file=',
    'chdir=',
    'module=',
])

data = {}
try:
    for i, j in opts:
        data[i] = j
    if '-h' in data:
        _help()
        os._exit(0)
    if '--chdir' in data:
        os.chdir(data['--chdir'])

    if '--module' in data:
        exec('import ' + data['--module'] + ' as app')

    elif '--wsgi-file' in data:
        exec('import ' + data['--wsgi-file'].split('.')[0] + ' as app')

    else:
        print('没有指定application')

    socket_ip, socket_port = data['--http-socket'].split(':')

    socket_port = int(socket_port)

except KeyError:
    print('参数错误')

else:
    server = make_server('', socket_port, app.application)
    server.serve_forever()
