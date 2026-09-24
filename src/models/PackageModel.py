from pydantic import Field, validator

from typing import List, Optional, Union, Literal

from sdks.novavision.src.base.model import (
    Package,
    Image,
    Inputs,
    Configs,
    Outputs,
    Response,
    Request,
    Output,
    Input,
    Config
)


class InputImage(Input):
    name: Literal["inputImage"] = "inputImage"
    value: Union[List[Image], Image]
    type: str = "object"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get("value")
        if isinstance(value, Image):
            return "object"
        elif isinstance(value, list):
            return "list"

    class Config:
        title = "Image"


class OutputImage(Output):
    name: Literal["outputImage"] = "outputImage"
    value: Union[List[Image], Image]
    type: str = "object"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get("value")
        if isinstance(value, Image):
            return "object"
        elif isinstance(value, list):
            return "list"

    class Config:
        title = "Image"


class FirstExecutorInputs(Inputs):
    inputImage: InputImage


class FirstExecutorOutputs(Outputs):
    outputImage: OutputImage


class FirstClockwiseAngle90(Config):
    name: Literal["90"] = "90"
    value: Literal[90] = 90
    type: Literal["number"] = "number"
    field: Literal["option"] = "option"


class FirstClockwiseAngle180(Config):
    name: Literal["180"] = "180"
    value: Literal[180] = 180
    type: Literal["number"] = "number"
    field: Literal["option"] = "option"


class FirstClockwiseAngle(Config):
    name: Literal["Angle"] = "Angle"
    value: Union[FirstClockwiseAngle90, FirstClockwiseAngle180]
    type: Literal["object"] = "object"
    field: Literal["dropdownlist"] = "dropdownlist"


class FirstClockwiseDescription(Config):
    name: Literal["Description"] = "Description"
    value: str
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"


class FirstClockwise(Config):
    name: Literal["Clockwise"] = "Clockwise"
    angle: FirstClockwiseAngle
    description: FirstClockwiseDescription
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"


class FirstCounterAngle90(Config):
    name: Literal["90"] = "90"
    value: Literal[90] = 90
    type: Literal["number"] = "number"
    field: Literal["option"] = "option"


class FirstCounterAngle180(Config):
    name: Literal["180"] = "180"
    value: Literal[180] = 180
    type: Literal["number"] = "number"
    field: Literal["option"] = "option"


class FirstCounterAngle(Config):
    name: Literal["Angle"] = "Angle"
    value: Union[FirstCounterAngle90, FirstCounterAngle180]
    type: Literal["object"] = "object"
    field: Literal["dropdownlist"] = "dropdownlist"


class FirstCounterDescription(Config):
    name: Literal["Description"] = "Description"
    value: str
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"


class FirstCounter(Config):
    name: Literal["Counterclockwise"] = "Counterclockwise"
    angle: FirstCounterAngle
    description: FirstCounterDescription
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"


class FirstExecutorRotation(Config):
    name: Literal["Rotation"] = "Rotation"
    value: Union[FirstClockwise, FirstCounter]
    type: Literal["object"] = "object"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"


class FirstExecutorConfigs(Configs):
    rotation: FirstExecutorRotation

class FirstExecutorRequest(Request):
    inputs: Optional[FirstExecutorInputs]
    configs: FirstExecutorConfigs

    class Config:
        json_schema_extra = {
            "target": "configs"
        }


class FirstExecutorResponse(Response):
    outputs: FirstExecutorOutputs


class FirstExecutor(Config):
    name: Literal["FirstExecutor"] = "FirstExecutor"
    value: Union[FirstExecutorRequest, FirstExecutorResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "Rotate Image 90°"
        json_schema_extra = {
            "target": {
                "value": 0
            }
        }


class SecondInputImage(Input):
    name: Literal["inputImage2"] = "inputImage2"
    value: Union[List[Image], Image]
    type: str = "object"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get("value")
        if isinstance(value, Image):
            return "object"
        elif isinstance(value, list):
            return "list"


class SecondOutputImage(Output):
    name: Literal["outputImage2"] = "outputImage2"
    value: Union[List[Image], Image]
    type: str = "object"

    @validator("type", pre=True, always=True)
    def set_type_based_on_value(cls, value, values):
        value = values.get("value")
        if isinstance(value, Image):
            return "object"
        elif isinstance(value, list):
            return "list"


class SecondExecutorInputs(Inputs):
    inputImage: InputImage
    inputImage2: SecondInputImage


class SecondExecutorOutputs(Outputs):
    outputImage: OutputImage
    outputImage2: SecondOutputImage

class SecondClockwiseAngle90(Config):
    name: Literal["90"] = "90"
    value: Literal[90] = 90
    type: Literal["number"] = "number"
    field: Literal["option"] = "option"


class SecondClockwiseAngle180(Config):
    name: Literal["180"] = "180"
    value: Literal[180] = 180
    type: Literal["number"] = "number"
    field: Literal["option"] = "option"


class SecondClockwiseAngle(Config):
    name: Literal["Angle"] = "Angle"
    value: Union[SecondClockwiseAngle90, SecondClockwiseAngle180]
    type: Literal["object"] = "object"
    field: Literal["dropdownlist"] = "dropdownlist"


class SecondClockwiseDescription(Config):
    name: Literal["Description"] = "Description"
    value: str
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"


class SecondClockwise(Config):
    name: Literal["Clockwise"] = "Clockwise"
    angle: SecondClockwiseAngle
    description: SecondClockwiseDescription
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"


class SecondCounterAngle90(Config):
    name: Literal["90"] = "90"
    value: Literal[90] = 90
    type: Literal["number"] = "number"
    field: Literal["option"] = "option"


class SecondCounterAngle180(Config):
    name: Literal["180"] = "180"
    value: Literal[180] = 180
    type: Literal["number"] = "number"
    field: Literal["option"] = "option"


class SecondCounterAngle(Config):
    name: Literal["Angle"] = "Angle"
    value: Union[SecondCounterAngle90, SecondCounterAngle180]
    type: Literal["object"] = "object"
    field: Literal["dropdownlist"] = "dropdownlist"


class SecondCounterDescription(Config):
    name: Literal["Description"] = "Description"
    value: str
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"


class SecondCounter(Config):
    name: Literal["Counterclockwise"] = "Counterclockwise"
    angle: SecondCounterAngle
    description: SecondCounterDescription
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"


class SecondExecutorRotation(Config):
    name: Literal["Rotation"] = "Rotation"
    value: Union[SecondClockwise, SecondCounter]
    type: Literal["object"] = "object"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"


class SecondExecutorConfigs(Configs):
    rotation: SecondExecutorRotation

class SecondExecutorRequest(Request):
    inputs: Optional[SecondExecutorInputs]
    configs: SecondExecutorConfigs

    class Config:
        json_schema_extra = {
            "target": "configs"
        }


class SecondExecutorResponse(Response):
    outputs: SecondExecutorOutputs


class SecondExecutor(Config):
    name: Literal["SecondExecutor"] = "SecondExecutor"
    value: Union[SecondExecutorRequest, SecondExecutorResponse]
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"

    class Config:
        title = "Rotate Two Images 90°"
        json_schema_extra = {
            "target": {
                "value": 0
            }
        }


class ConfigExecutor(Config):
    name: Literal["ConfigExecutor"] = "ConfigExecutor"
    value: Union[FirstExecutor, SecondExecutor]
    type: Literal["executor"] = "executor"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"
    restart: Literal[True] = True

    class Config:
        title = "Task"


class PackageConfigs(Configs):
    executor: ConfigExecutor


class PackageModel(Package):
    configs: PackageConfigs
    type: Literal["component"] = "component"
    name: Literal["IremPackage"] = "IremPackage"