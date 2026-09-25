# Image Rotation Demo

> Rotates one or two input images according to the selected rotation configuration.

**Category:** Classical Computer Vision / Preprocessing

**Status:** Stable

**Last Updated:** 25.09.2026

---

## 1. Overview

Image Rotation Demo is a NovaVision component package that provides two executors for rotating images.

The package supports rotating a single image or two images using the same rotation configuration. The rotation direction can be selected as Clockwise or Counterclockwise, with 90° and 180° angle options.

**Typical use cases:**

- Rotating a single image in a processing pipeline
- Applying the same rotation to two images
- Preprocessing images before further processing

---

## 2. Inputs

### Rotate Image

| Field Name | Kind/Type | Required | Default | Description |
|---|---|---|---|---|
| `inputImage` | Image | Yes | — | Image to be rotated |

![Rotate Image Flow](images/rotate-image-flow.png)

### Rotate Two Images

| Field Name | Kind/Type | Required | Default | Description |
|---|---|---|---|---|
| `inputImage` | Image | Yes | — | First image to be rotated |
| `inputImage2` | Image | Yes | — | Second image to be rotated |

![Rotate Two Images Flow](images/rotate-two-images-flow.png)

---

## 3. Configuration Parameters

| Parameter | Type | Field Type (UI control) | Allowed Values / Range | Default | Description |
|---|---|---|---|---|---|
| `Rotation` | object | `dependentDropdownlist` | Clockwise / Counterclockwise | — | Selects the rotation direction and related parameters |
| `Angle` | object | `dropdownlist` | 90°, 180° | — | Selects the rotation angle |
| `Description` | string | `textInput` | — | — | Description for the selected rotation option |

The `Rotation` configuration contains two options: `Clockwise` and `Counterclockwise`. Each option includes an `Angle` dropdownlist and a `Description` textInput.

> `ConfigExecutor` is not included in this table.

---

## 4. Outputs

### Rotate Image

| Field Name | Kind/Type | Description |
|---|---|---|
| `outputImage` | Image | Rotated output image |

### Rotate Two Images

| Field Name | Kind/Type | Description |
|---|---|---|
| `outputImage` | Image | Rotated first image |
| `outputImage2` | Image | Rotated second image |

![Rotation Example](images/rotation-example.png)

---

## 5. Use Case Examples

**Use case 1: Single Image Rotation**

An image is provided to `Rotate Image`. The selected rotation direction and angle are applied, and the rotated image is returned as `outputImage`.

**Use case 2: Two Image Rotation**

Two images are provided to `Rotate Two Images`. The same rotation configuration is applied to both images, and the rotated images are returned as `outputImage` and `outputImage2`.

---

## 6. Limitations and Notes

- Supported rotation angles are 90° and 180°.
- The same rotation configuration is applied to both images in `Rotate Two Images`.
- The `Description` field is provided as part of the dependent dropdown configuration and does not affect the rotation operation.