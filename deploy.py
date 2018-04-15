from fabric.api import cd, env, get, lcd, local, run, put, prompt

env.hosts = ['192.168.0.167']
env.user = 'joit'
env.password = 'wzws670xs'


def test():
    with cd('~/host/Projects/items/endorsit-sweet'):
        container = run('docker container ls')
        if 'eds-swt-run' in str(container):
            run('docker stop eds-swt-run')
        image = run('docker images')
        if 'eds-swt' in str(image):
            run('docker rmi eds-swt')

        run('git stash && git pull && git stash pop')
        run('docker build -t eds-swt . && docker run -d --rm -p 5000:5000 --name eds-swt-run eds-swt')
