import json

import jinja2
import requests
import yaml

CLOUD_INIT_TPL: str = (
    "https://raw.githubusercontent.com/eoda-dev/vmboot/refs/heads/main/cloud-init/base.tpl.yml"
)


def render_cloud_init_tpl() -> None:
    with requests.get(CLOUD_INIT_TPL) as repsponse:
        cloud_init = jinja2.Template(repsponse.text).render(
            user="steve", public_ssh_key="steve's key"
        )

    # print(cloud_init)
    print(json.dumps(yaml.safe_load(cloud_init)))


x = """content: |
    some test
    and even more"""

if __name__ == "__main__":
    render_cloud_init_tpl()
    # print(yaml.safe_dump(yaml.safe_load(x), default_style="|"))
