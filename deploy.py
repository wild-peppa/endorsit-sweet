from fabric.api import cd, env, get, lcd, local, run, put, prompt

env.hosts = ['207.148.125.71']
env.user = 'ext'
env.password = 'ext-123'


def test():
    # with cd('~/host/Projects/items/endorsit-sweet'):
    with cd('~/www/endorsit-sweet'):
        container = run('docker container ls')
        if 'eds-swt-run' in str(container):
            run('docker stop eds-swt-run')
        image = run('docker images')
        if 'eds-swt' in str(image):
            run('docker rmi eds-swt')

        folders = run('ls endorsit-sweet/endorsit-sweet/logger')
        if 'error_logs' not in folders:
            run('mkdir -p endorsit-sweet/endorsit-sweet/logger/error_logs')
        if 'debug_logs' not in folders:
            run('mkdir -p endorsit-sweet/endorsit-sweet/logger/debug_logs')

        run('git stash && git pull && git stash pop')
        run('docker build -t eds-swt . && docker run -d --rm -p 18100:8001 --name eds-swt-run eds-swt')
