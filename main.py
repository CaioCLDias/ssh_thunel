#bibliotecas necessárias
import sshtunnel
from sshtunnel import SSHTunnelForwarder
import logging
import pymysql
import credentials as c

#conexão com ssh
def open_ssh_tunnel(verbose=False):
    if verbose:
        sshtunnel.DEFAULT_LOGLEVEL = logging.DEBUG

    global tunnel
    tunnel = SSHTunnelForwarder(
        (c.ssh_host, c.ssh_port),
        ssh_username=c.ssh_username,
        ssh_password=c.ssh_password,
        remote_bind_address=(c.localhost, c.port)
    )

    tunnel.start()

#conectando com o banco
def mysql_connect():
    global conn
    conn = pymysql.connect(
        host=c.localhost,
        user=c.user,
        passwd=c.password,
        db=c.database,
        port=tunnel.local_bind_port
    )

#desconectando com o banco
def mysql_disconnect():
    eng.dispose()

#fechado o tunel
def close_ssh_tunnel():
    tunnel.close()