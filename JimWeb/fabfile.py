from fabric.api import env,run
from fabric.operations import sudo 

GIT_REPO = "https://github.com/zgGitHub/JimWeb.git"

env.user = 'root'
env.password = 'Jimsir123'

env.hosts = ['www.lovejim.cn']

env.port = '22'

def deploy():
    source_folder = '/home/jimsir/sites/www.lovejim.cn/DjangoBlog'

    run('cd %s && git pull' % source_folder)
    run("""
        cd {} &&
        ../env/bin/pip install -r requirements.txt && 
        ../env/bin/python3 manage.py collectstatic --noinput && 
        ../env/bin/python3 manage.py migrate
    """.format(source_folder))
    sudo('restart gunicorn-www.lovejim.cn')
    sudo('service nginx reload')
