import ipfs_api


def move_to_ipfs(image_path):

    file_path = image_path

    res = ipfs_api.http_client.add(file_path)

    print(res)

    cid = (res["Hash"])

    return cid

