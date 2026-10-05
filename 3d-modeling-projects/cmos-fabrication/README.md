# CMOS Fabrication Tutorial

## Overview

This project is an interactive web-based tutorial that visually explains the **CMOS (Complementary Metal-Oxide-Semiconductor) fabrication process**.

Users can explore each major step in the process using interactive **3D models**, descriptive **flashcards**, and a sidebar for easy navigation.

The tutorial is built using **HTML, CSS, and JavaScript**, with **Three.js** for 3D rendering.

## Features

* Step-by-step guide for the 8 major CMOS fabrication processes
* Interactive 3D model viewer powered by Three.js
* Clickable sidebar navigation for each process step
* Front-and-back flashcards with process summaries
* Responsive layout with adjustable viewer size
* Error handling for missing or invalid 3D model files

## CMOS Fabrication Steps

1. **Wafer Preparation**

   * Start with a high-purity silicon wafer
   * Clean and polish the wafer
   * Prepare the surface for nanoscale patterning

2. **Oxidation**

   * Grow a silicon dioxide (SiO₂) layer using thermal oxidation
   * Control the oxide thickness for device reliability

3. **Photolithography**

   * Apply photoresist
   * Expose the wafer using DUV/EUV light and a photomask
   * Develop the photoresist to create the desired pattern

4. **Etching**

   * Remove selected material using wet or dry etching
   * Transfer the photolithography pattern into underlying layers

5. **Doping**

   * Introduce impurities into the silicon
   * Use dopants such as boron, phosphorus, or arsenic
   * Anneal the wafer to repair crystal damage and activate dopants

6. **Deposition**

   * Deposit thin films using CVD, PVD, or ALD
   * Add materials such as polysilicon and dielectric layers

7. **Metallization**

   * Create metal interconnects using materials such as copper
   * Connect different parts of the chip through multiple metal layers

8. **Packaging**

   * Test and dice the wafer into individual dies
   * Connect the die to a package
   * Encapsulate the chip for protection

## Project Structure

```text
CMOS-Fabrication-Tutorial/
│
├── index.html
│
├── models/
│   ├── wafer_preparation.gltf
│   ├── oxidation.gltf
│   ├── photolithography.gltf
│   ├── etching.gltf
│   ├── doping.gltf
│   ├── deposition.gltf
│   ├── metallization.gltf
│   └── packaging.gltf
│
└── README.md
```

### Main Files

* `index.html` — Main webpage containing the HTML, CSS, and JavaScript
* `models/` — Contains the GLTF 3D models for each fabrication step
* `README.md` — Project documentation

## Technologies Used

* **HTML** — Webpage structure
* **CSS** — Layout and styling
* **JavaScript** — Interactivity and application logic
* **Three.js** — 3D rendering
* **GLTFLoader** — Loading 3D GLTF models
* **OrbitControls** — Camera rotation, zoom, and panning

## How It Works

1. Each sidebar button calls the `showStep()` function.
2. `showStep()` updates the flashcard title and description.
3. The corresponding GLTF model is loaded into the Three.js scene.
4. `OrbitControls` allows users to rotate, zoom, and pan around the 3D model.
5. Users can click the flashcard to flip it and view additional information.

## Requirements

* A modern web browser such as Chrome, Firefox, or Edge
* An internet connection for the Three.js CDN libraries
* Local `.gltf` model files stored in the project's `models/` directory

## How to Run

1. Download or clone this repository.
2. Make sure all `.gltf` model files are inside the `models/` directory.
3. Open `index.html` in a web browser.
4. Use the sidebar to select a CMOS fabrication step.
5. Explore the corresponding 3D model and flip the flashcard to learn more.

## Interactive 3D Models

Each fabrication step has its own GLTF model:

| Step              | Model                    |
| ----------------- | ------------------------ |
| Wafer Preparation | `wafer_preparation.gltf` |
| Oxidation         | `oxidation.gltf`         |
| Photolithography  | `photolithography.gltf`  |
| Etching           | `etching.gltf`           |
| Doping            | `doping.gltf`            |
| Deposition        | `deposition.gltf`        |
| Metallization     | `metallization.gltf`     |
| Packaging         | `packaging.gltf`         |

## Error Handling

The application includes error handling for cases where a 3D model cannot be loaded. If a model fails to load, an error message is displayed to the user instead of leaving the viewer blank.

## Educational Purpose

This project is designed to make semiconductor manufacturing concepts more accessible through **visualization and interaction**. Instead of relying only on written explanations, users can explore each fabrication stage through 3D models and interactive learning elements.
