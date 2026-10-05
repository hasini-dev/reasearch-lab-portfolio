# 3D IC Fabrication Tutorial

## Overview

An interactive web-based tutorial that visualizes the **3D Integrated Circuit (3D IC) fabrication process**.

The tutorial combines educational flashcards with interactive 3D model viewing using **Three.js**, allowing users to explore each stage of the fabrication process.

## Features

* Step-by-step explanation of 3D IC fabrication stages
* Interactive flashcard system for each step
* 3D model viewer with orbit controls
* Smooth model transitions
* Responsive layout

## Technologies Used

* **HTML5**
* **CSS3**
* **JavaScript (ES6)**
* **Three.js** for 3D visualization
* **GLTFLoader** for loading `.glb` 3D models
* **OrbitControls** for interactive camera movement

## Fabrication Steps

### 1. 3D IC Overview

3D ICs stack multiple active layers vertically.

* Enables shorter interconnects and higher density
* Uses TSVs, wafer thinning, and bonding
* Challenges include heat, alignment, and testing

### 2. Wafer Preparation

Start with ultra-flat silicon wafers.

* Clean and planarize with CMP
* Prepare the wafer for thinning and bonding
* Ensure surface quality

### 3. TSV Formation

Create **Through-Silicon Vias (TSVs)**.

* Etch holes using DRIE
* Line vias with an insulator and barrier
* Fill with copper and polish

### 4. Die Fabrication

Build CMOS devices on the wafer.

* Add metal layers for TSV connection
* Account for stress and thermal effects during design

### 5. Wafer Thinning

Reduce wafer thickness to access TSVs.

* Use grinding and chemical etching
* Use a temporary carrier to support the wafer
* Enables wafer stacking

### 6. Wafer Bonding

Stack wafers using precision bonding.

* Cu-Cu bonding
* Oxide-oxide bonding
* Adhesive bonding
* Requires precise alignment

### 7. Interposer Fabrication

Add an intermediate routing layer.

* Uses TSVs and RDLs
* Connects different chiplets
* Can be made from silicon or organic materials

### 8. Stacking

Assemble multiple dies or wafers.

* Die-to-die
* Die-to-wafer
* Wafer-to-wafer
* Challenges include thermal management and alignment

### 9. Packaging

Provide final protection and signal routing.

* Add bumps
* Add heat sinks
* Apply underfill
* Test and seal the device

## Project Structure

```text
3D-IC-Fabrication-Tutorial/
│
├── index.html
├── wafer_preparation.glb
├── tsv_formation.glb
├── die_fabrication.glb
├── wafer_thinning.glb
├── wafer_bonding.glb
├── inter.glb
├── stack.glb
└── packaging.glb
```

The `.glb` files contain the 3D models used for the corresponding fabrication steps.

## How It Works

The sidebar contains buttons for each fabrication step. Selecting a step:

1. Updates the flashcard title.
2. Updates the flashcard description.
3. Displays the corresponding 3D model, if one is provided.
4. Resets the flashcard to its front side.

Users can click the flashcard to flip between the step title and its description.

The 3D viewer uses **Three.js**, `GLTFLoader`, and `OrbitControls` to load and interact with the `.glb` models.

## Requirements

* Modern web browser with WebGL support
* Chrome, Edge, or Firefox recommended
* Optional local or hosted `.glb` files for each fabrication step

## How to Run

1. Open `index.html` in a modern web browser.
2. Use the sidebar to select a fabrication step.
3. Read the step summary on the flashcard.
4. View the corresponding 3D model.
5. Click the flashcard to flip between the title and description.

## Adding or Editing Steps

To customize the tutorial, edit the `steps` array inside the `<script>` section of `index.html`.

Each step contains:

```javascript
{
    title: "Step Title",
    desc: "Step Description",
    model: "model_file.glb"
}
```

If `model` is set to `null`, no 3D model will be displayed for that step.

## 3D Models

| Fabrication Step       | Model                   |
| ---------------------- | ----------------------- |
| Wafer Preparation      | `wafer_preparation.glb` |
| TSV Formation          | `tsv_formation.glb`     |
| Die Fabrication        | `die_fabrication.glb`   |
| Wafer Thinning         | `wafer_thinning.glb`    |
| Wafer Bonding          | `wafer_bonding.glb`     |
| Interposer Fabrication | `inter.glb`             |
| Stacking               | `stack.glb`             |
| Packaging              | `packaging.glb`         |

The 3D IC Overview step does not use a model.

## License

This project is provided for **educational and non-commercial use**.

You may modify and adapt the project for your own learning or teaching purposes.
