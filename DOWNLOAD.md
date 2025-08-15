Dataset **Insulator-Defect Detection** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogInMzOi8vc3VwZXJ2aXNlbHktZGF0YXNldHMvMTAyN19JbnN1bGF0b3ItRGVmZWN0IERldGVjdGlvbi9pbnN1bGF0b3ItZGVmZWN0LWRldGVjdGlvbi1EYXRhc2V0TmluamEudGFyIiwgInNpZyI6ICIxR28rMy9wc1NNM3NiVzZnUmFrTmFpY3FKTDg4eTBxblVUY0NobFloUHdJPSJ9?response-content-disposition=attachment%3B%20filename%3D%22insulator-defect-detection-DatasetNinja.tar%22)

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