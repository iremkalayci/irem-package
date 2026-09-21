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


class KeepSideFalse(Config):

    name: Literal["False"] = "False"
    value: Literal[False] = False
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    class Config:
        title = "Disable"


class KeepSideTrue(Config):

    name: Literal["True"] = "True"
    value: Literal[True] = True
    type: Literal["bool"] = "bool"
    field: Literal["option"] = "option"

    class Config:
        title = "Enable"


class KeepSideBBox(Config):

    name: Literal["KeepSide"] = "KeepSide"
    value: Union[KeepSideTrue, KeepSideFalse]
    type: Literal["object"] = "object"
    field: Literal["dropdownlist"] = "dropdownlist"

    class Config:
        title = "Keep Sides"


class Degree(Config):

    name: Literal["Degree"] = "Degree"
    value: int = Field(ge=-359.0, le=359.0, default=0)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"
    placeHolder: Literal["[-359, 359]"] = "[-359, 359]"

    class Config:
        title = "Angle"


class FirstExecutorInputs(Inputs):

    inputImage: InputImage


class FirstExecutorOutputs(Outputs):

    outputImage: OutputImage


class FirstBasicText(Config):
    name: Literal["Text"] = "Text"
    value: str
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"


class FirstBasicNumber(Config):
    name: Literal["Number"] = "Number"
    value: int
    type: Literal["number"] = "number"
    field: Literal["selectBox"] = "selectBox"


class FirstAdvancedLanguage(Config):
    name: Literal["Language"] = "Language"
    value: str
    type: Literal["string"] = "string"
    field: Literal["dropdownlist"] = "dropdownlist"


class FirstAdvancedEnabled(Config):
    name: Literal["Enabled"] = "Enabled"
    value: bool
    type: Literal["bool"] = "bool"
    field: Literal["selectBox"] = "selectBox"


class FirstBasicOption(Config):
    name: Literal["Basic"] = "Basic"
    text: FirstBasicText
    number: FirstBasicNumber
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"


class FirstAdvancedOption(Config):
    name: Literal["Advanced"] = "Advanced"
    language: FirstAdvancedLanguage
    enabled: FirstAdvancedEnabled
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"


class FirstExecutorMode(Config):
    name: Literal["Mode"] = "Mode"
    value: Union[FirstBasicOption, FirstAdvancedOption]
    type: Literal["object"] = "object"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"


class FirstExecutorConfigs(Configs):
    mode: FirstExecutorMode


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
        title = "First Executor"
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


class SecondBasicText(Config):
    name: Literal["Text"] = "Text"
    value: str
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"


class SecondBasicNumber(Config):
    name: Literal["Number"] = "Number"
    value: int
    type: Literal["number"] = "number"
    field: Literal["selectBox"] = "selectBox"


class SecondAdvancedLanguage(Config):
    name: Literal["Language"] = "Language"
    value: str
    type: Literal["string"] = "string"
    field: Literal["dropdownlist"] = "dropdownlist"


class SecondAdvancedEnabled(Config):
    name: Literal["Enabled"] = "Enabled"
    value: bool
    type: Literal["bool"] = "bool"
    field: Literal["selectBox"] = "selectBox"


class SecondBasicOption(Config):
    name: Literal["Basic"] = "Basic"
    text: SecondBasicText
    number: SecondBasicNumber
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"


class SecondAdvancedOption(Config):
    name: Literal["Advanced"] = "Advanced"
    language: SecondAdvancedLanguage
    enabled: SecondAdvancedEnabled
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"


class SecondExecutorMode(Config):
    name: Literal["Mode"] = "Mode"
    value: Union[SecondBasicOption, SecondAdvancedOption]
    type: Literal["object"] = "object"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"


class SecondExecutorConfigs(Configs):
    mode: SecondExecutorMode


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
        title = "Second Executor"
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

    class Config:
        title = "Task"


class PackageConfigs(Configs):

    executor: ConfigExecutor


class PackageModel(Package):

    configs: PackageConfigs
    type: Literal["component"] = "component"
    name: Literal["IremPackage"] = "IremPackage"