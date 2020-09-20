"""API functions related to images"""

import requests_unixsocket

from podmanapi import api_endpoint

session = requests_unixsocket.Session()


def create_image():
    pass


def remove_image():
    pass


def image_exists(container: str) -> str:
    """"Check if image exists in local store

    :param container: the name or ID of the container
    :type container: str

    :returns: JSON with information
    """
    return session.get(f"{api_endpoint}/{container}/exists").json()