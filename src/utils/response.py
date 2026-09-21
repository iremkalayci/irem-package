from sdks.novavision.src.helper.package import PackageHelper

from components.Package.src.models.PackageModel import (
    PackageModel,
    PackageConfigs,
    ConfigExecutor,
    FirstExecutor,
    FirstExecutorResponse,
    FirstExecutorOutputs,
    SecondExecutor,
    SecondExecutorResponse,
    SecondExecutorOutputs,
    OutputImage,
)


def build_response(context):

    executor_value = context.request.model.configs.executor.value

    if isinstance(executor_value, FirstExecutor):
        output_image = OutputImage(value=context.image)
        outputs = FirstExecutorOutputs(
            outputImage=output_image
        )
        response = FirstExecutorResponse(
            outputs=outputs
        )
        executor = FirstExecutor(
            value=response
        )

    elif isinstance(executor_value, SecondExecutor):
        output_image1 = OutputImage(value=context.image1)
        output_image2 = OutputImage(value=context.image2)

        outputs = SecondExecutorOutputs(
            outputImage=output_image1,
            outputImage2=output_image2
        )

        response = SecondExecutorResponse(
            outputs=outputs
        )
        executor = SecondExecutor(
            value=response
        )

    else:
        raise ValueError("Unknown executor")

    package_configs = PackageConfigs(
        executor=ConfigExecutor(
            value=executor
        )
    )

    package = PackageHelper(
        packageModel=PackageModel,
        packageConfigs=package_configs
    )

    return package.build_model(context)