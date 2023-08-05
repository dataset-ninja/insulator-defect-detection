Dataset **Insulator-Defect Detection** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/u/y/1j/dFVgX8asWh3QL4vVEBkbPKkJnqEPcqvlk2vH6ss6fneJj3snw9hzM1paZnBX8il1AVgWriXeMKEmnwTlipqvUAJjHQPLJijUarHCcSn9GzOEkbWO7Ln6jLXL6W0T.tar)

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

The data in original format can be [downloaded here](https://figshare.com/ndownloader/files/37587370)