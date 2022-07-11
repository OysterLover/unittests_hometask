import requests


def create_folder(path):
    ya_token = 'AQAAAAA1RjtIAADLW3Cq_QCE_047lq5Xt2jj9xc'
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'OAuth {ya_token}'}
    requests.put(f'{url}?path={path}', headers=headers)

if __name__ == '__main__':
    create_folder('test')

