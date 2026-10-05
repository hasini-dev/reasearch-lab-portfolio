# FinFET Fabrication Tutorial

## Overview

This project is an interactive **FinFET (Fin Field-Effect Transistor) fabrication tutorial** built using **Three.js, HTML, CSS, and JavaScript**.

It visually explains the major steps of the FinFET fabrication process using interactive **3D models** and **flip cards** containing process descriptions.

Users can explore the fabrication sequence through the sidebar, view 3D models of each step, and read concise educational summaries.

## Features

* Interactive 3D visualization for each FinFET fabrication step
* Flip-card interface for step descriptions
* Sidebar navigation for quick access to each step
* Real-time model rotation, zoom, and pan using OrbitControls
* Responsive resizing of the 3D viewer
* Modular structure with an individual model and description for each step

## Fabrication Steps

1. **Substrate Preparation**

   * Start with a clean, doped silicon wafer
   * Remove contaminants
   * Prepare a uniform and reliable base

2. **Fin Patterning**

   * Define fins using photolithography and etching
   * Use reactive ion etching (RIE) to form high-aspect-ratio fins
   * Create the structures needed for transistor operation

3. **Shallow Trench Isolation (STI)**

   * Create trenches between fins
   * Fill the trenches with dielectric material such as SiO₂
   * Polish the surface using chemical-mechanical planarization (CMP)

4. **Gate Stack Formation**

   * Form the gate around the fin
   * Deposit a high-k dielectric such as HfO₂
   * Add a metal gate to wrap around the fin
   * Improve channel control

5. **Spacer Formation**

   * Deposit silicon nitride
   * Perform anisotropic etching to create sidewall spacers
   * Help define and shape the source/drain regions

6. **Source/Drain Formation**

   * Form source and drain regions through ion implantation or selective epitaxy
   * Use materials such as SiGe or SiC for strain engineering
   * Improve transistor performance

7. **Contact Formation**

   * Etch contact holes
   * Deposit barrier and tungsten metal
   * Create low-resistance electrical connections to the source, drain, and gate

8. **Interconnect Formation**

   * Build the chip's wiring layers
   * Use Cu/Al and low-k dielectrics
   * Create vias and multi-level metal lines
   * Complete the circuit layout

## Project Structure

```text
FinFET-Fabrication-Tutorial/
│
├── index.html
│
├── models/
│   ├── finfet_substrate.glb
│   ├── finfet_patterning.glb
│   ├── finfet_sti.glb
│   ├── finfet_gate.glb
│   ├── finfet_spacers.glb
│   ├── finfet_sd.glb
│   ├── finfet_contacts.glb
│   └── finfet_interconnect.glb
│
└── README.md
```

### Main Files

* `index.html` — Main webpage containing the HTML, CSS, and JavaScript
* `models/` — Contains the GLB/GLTF 3D models for each fabrication step
* `README.md` — Project documentation

## Technologies Used

* **HTML** — Webpage structure
* **CSS** — Layout and styling
* **JavaScript** — Interactivity and application logic
* **Three.js** — 3D rendering
* **GLTFLoader** — Loading GLB/GLTF 3D models
* **OrbitControls** — Model rotation, zoom, and navigation

## How It Works

1. Each step button in the sidebar calls the `showStep()` function.
2. The function updates the flashcard title and description.
3. The corresponding `.glb` 3D model is loaded into the Three.js scene.
4. `GLTFLoader` loads the model.
5. `OrbitControls` allows users to rotate and zoom the model.
6. Clicking the flashcard flips it to reveal additional information about the fabrication step.

## Requirements

* A modern web browser such as Chrome, Firefox, or Edge
* An internet connection for loading Three.js and its dependencies from a CDN
* Local `.glb` model files for each fabrication step

## How to Run

1. Download or clone the repository.
2. Make sure the `models` folder is located in the same directory as `index.html`.
3. Place all `.glb` model files inside the `models` folder.
4. Open `index.html` in your browser.
5. Use the sidebar to select a FinFET fabrication step.
6. Rotate, zoom, and explore the corresponding 3D model.
7. Click the flashcard to view the process description.

## Customization

### Add New Steps

To add another fabrication step:

1. Add a new button to the sidebar.
2. Add a new step object to the `steps` array.
3. Include the step's:

   * Title
   * Description
   * Model filename

### Change Content

Titles and descriptions can be modified directly inside the `steps` array in the `<script>` section.

### Customize Styling

The `<style>` section can be edited to change:

* Colors
* Fonts
* Sidebar dimensions
* Viewer layout
* Flashcard appearance
* Spacing and sizing

## 3D Models

| Fabrication Step         | Model                     |
| ------------------------ | ------------------------- |
| Substrate Preparation    | `finfet_substrate.glb`    |
| Fin Patterning           | `finfet_patterning.glb`   |
| Shallow Trench Isolation | `finfet_sti.glb`          |
| Gate Stack Formation     | `finfet_gate.glb`         |
| Spacer Formation         | `finfet_spacers.glb`      |
| Source/Drain Formation   | `finfet_sd.glb`           |
| Contact Formation        | `finfet_contacts.glb`     |
| Interconnect Formation   | `finfet_interconnect.glb` |

## Credits

* Built with **Three.js** for 3D rendering
* Educational content based on standard FinFET fabrication processes
* Designed as an interactive tool for teaching semiconductor device engineering concepts
