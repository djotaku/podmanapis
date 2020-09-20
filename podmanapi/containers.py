"""API functions related to containers."""

import requests_unixsocket
from typing import List

from podmanapi import api_endpoint

session = requests_unixsocket.Session()


def commit(container: str, repo: str = None, tag: str = None, comment: str = None, author: str = None,
           pause: bool = None, changes: List[str] = None, a_format: str = None) -> str:
    """Create a new image form a container.

    :param container: the name or ID of a container
    :type container: str
    :param repo: (optional) the repository name for the created image
    :type repo: str
    :param tag: (optional) tag name for the craeted image
    :type tag: str
    :param comment: (optional) commit message
    :type comment: str
    :param author: (optional) author of the image
    :type author: str
    :param pause: (optional) pause the container before committing it.
    :type pause: bool
    :param changes: (optional) instructions to apply while committing in Dockerfile format (i.e. "CMD=/bin/foo")
    :type changes: List[str]
    :param a_format: (optional) format of the image manifest and metadata (default "oci")
    :type a_format: str
    """

    #response = session.post(f"{api_endpoint}/libpod/commit", )