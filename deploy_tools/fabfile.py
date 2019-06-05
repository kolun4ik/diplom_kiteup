from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run
import random

REPO_URL = 'https://github.com/kolun4ik/diplom_kiteup'

def deploy():
    """развернуть"""
    site_folder = f'/home/{env.user}/sites/{env.host}'
    source_folder = site_folder + '/source'
    _create_directory_structure_if_necessery(site_folder)
    _get_latest_source(source_folder)
    _update_settings(source_folder, env.host)
    _updatevirtualenv(source_folder)
    _update_static_file(source_folder)
    _update_database(source_folder)

def _create_directory_structure_if_necessery(site_folder):
    """создаем, если нужно, структуру каталогов"""
    for subfolder in ('database', 'static', 'virtualenv', 'source'):
        run(f'mkdir -p {site_folder}/{subfolder}')


def _get_latest_source(source_folder):
    """получение кода из репозитория"""
    if exists(source_folder + '/.git'):
        run(f'cd {source_folder} && git fetch')
    else:
        run(f'git clone {REPO_URL} {source_folder}')
        current_commit = local("git log -n 1 --format=%H", capture=True)
        run(f'cd {source_folder} && git reset --hard {current_commit}')

def _update_settings(source_folder, site_name):
    """обновляем настройки в settings.py"""
    settings_path = source_folder + '/kiteup/settings.py'
    # выполнение строковой замены
    sed(settings_path, "DEBUG = True", "DEBUG = False")
    sed(settings_path,
        'ALLOWED_HOSTS = .+$',
        f'ALLOWED_HOSTS = ["{site_name}"]'
        )
    secret_key_file = source_folder + '/kiteup/secret_key.py'
    if not exists(secret_key_file):
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        key = ''.join(random.SystemRandom().choice(chars) for _ in range(50))
        append(secret_key_file, f'SECRET_KEY = "{key}"')
    append(settings_path, '\nfrom .secret_key import SECRET_KEY')

def _updatevirtualenv(source_folder):
    """обновление виртуальной среды"""
    virtualenv_folder = source_folder + '/../virtualenv'
    if not exists(virtualenv_folder + '/bin/pip'):
        run(f'python3.7 -m venv {virtualenv_folder}')
    run(f'{virtualenv_folder}/bin/pip install -r {source_folder}/requirement.txt')

def _update_static_file(source_folder):
    """обновление статических файлов"""
    run(f'cd {source_folder} && ../virtualenv/bin/python manage.py collectstatic --noinput')

def _update_database(source_folder):
    """миграция базы данных"""
    # --noinput в помощь, чтобы fabric не запнулся на подверждениях ввода
    run(f'cd {source_folder} && ../virtualenv/bin/python manage.py migrate --noinput')

