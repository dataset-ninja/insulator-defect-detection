Dataset **Insulator-Defect Detection** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/M/s/lt/EGYyNu0WbSwV27OgoWrCwVCSxXt5B7OUpFXVXAYrEii5keFJpJ08yeICyAVjNqmgrfq4SzPsg9Y1RrTEgtqyLNUWjjHdtjrviNzb5UVqEpYK8Nupmg8WeaPKNNN8.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Insulator-Defect Detection', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://figshare.com/ndownloader/files/37587370).