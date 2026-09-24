import os
import sys
import numpy as np

sys.path.append(os.path.join(os.path.dirname(__file__), '../../../../'))

from sdks.novavision.src.media.image import Image
from sdks.novavision.src.base.component import Component
from sdks.novavision.src.helper.executor import Executor
from components.Package.src.utils.response import build_response
from components.Package.src.models.PackageModel import PackageModel


class SecondExecutor(Component):

    def __init__(self, request, bootstrap):
        super().__init__(request, bootstrap)
        self.request.model = PackageModel(**(self.request.data))
        self.image1 = self.request.get_param("inputImage")
        self.image2 = self.request.get_param("inputImage2")

    @staticmethod
    def bootstrap(config: dict) -> dict:
        return {}

    def run(self):
        img1 = Image.get_frame(
            img=self.image1,
            redis_db=self.redis_db
        )

        img2 = Image.get_frame(
            img=self.image2,
            redis_db=self.redis_db
        )

        img1 = np.rot90(img1, k=-1)
        img2 = np.rot90(img2, k=-1)

        self.image1 = Image.set_frame(
            img=img1,
            package_uID=self.uID,
            redis_db=self.redis_db
        )

        self.image2 = Image.set_frame(
            img=img2,
            package_uID=self.uID,
            redis_db=self.redis_db
        )

        packageModel = build_response(context=self)
        return packageModel


if "__main__" == __name__:
    Executor(sys.argv[1]).run()