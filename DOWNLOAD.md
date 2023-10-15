Dataset **Insulator-Defect Detection** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/c/b/Tz/z2GR0WuMPTsz50KZrTbRGGnWV8Ir3P77nug0nNV3YTS0pAJK8Oth4W1XMImKmHsMcB53boXQjo1DGJfpd6PvTJeG6QAyXSP7jv3UJpATtE6ZAK7brlQ0D0LaZbLI.tar)

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