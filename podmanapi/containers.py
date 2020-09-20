"""API functions related to containers."""

import requests_unixsocket
from typing import List

from podmanapi import api_endpoint

session = requests_unixsocket.Session()


def commit(container: str, **kwargs) -> str:
    """Create a new image form a container.

    :param container: the name or ID of a container
    :type container: str

    The following are optional parameters:
    repo: (str) the repository name for the created image
    tag: (str) tag name for the created image
    comment: (str) commit message
    author: (str) author of the image
    pause: (bool) pause the container before committing it.
    changes: (List[str]) instructions to apply while committing in Dockerfile format (i.e. "CMD=/bin/foo")
    format: (str) format of the image manifest and metadata (default "oci")
    """
    data = {key: value for key, value in kwargs.items()}
    data["container"] = container
    # just a bit of debugging
    for key, value in data.items():
        print(f"{key=}, {value=}")
    response = session.post(f"{api_endpoint}/commit", data=data)
    if response.status_code == 200:
        return "No Error"
    else:
        return response
