from fabric.api import run,env
import sqlite3

env.hosts = ['localhost']
env.user = 'firewall'
env.password = '12345678QAZxswe'


def proxy_reload():

    conn = sqlite3.connect('proxy')
    c = conn.cursor()
    f = open('proxy_list.cfg', 'wr')
    i=1
    f.write('backend proxy_backend\n')
    f.write('\toption http_proxy\n')
    f.write('\tbalance roundrobin\n')
    for row in c.execute('SELECT * FROM proxy_list'):
        f.write("\tserver squid"+str(i)+" "+row[0]+":"+row[1]+" check inter 2000 rise 2 fall 5\n")
        i+=1
    f.close()

    run('. /opt/haproxy_reload/haproxy_reload/haproxy_reload.sh')


    #run('service haproxy restart')
