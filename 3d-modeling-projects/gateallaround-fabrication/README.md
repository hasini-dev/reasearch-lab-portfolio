# GAA Fabrication Tutorial

## Overview

An interactive GAA (Gate-All-Around) fabrication tutorial built with HTML, CSS, JavaScript, and Three.js.

The tutorial uses interactive 3D `.glb` models and flipcards to visually explain the major steps involved in GAA fabrication.

## Overall Structure

* **Sidebar:** Lists the key GAA fabrication steps as clickable buttons.
* **3D Viewer:** Displays 3D `.glb` models for each fabrication step.
* **Flashcard:** Shows the step name on the front and a description on the back. Click the card to flip it.

## Key Features

### 1. Responsive Layout

The page uses a full-screen flex layout:

* Sidebar on the left for step navigation
* Content area on the right for the 3D model viewer and flashcard
* Viewer automatically adjusts when the window is resized

### 2. Interactive 3D Visualization

Uses **Three.js**, **GLTFLoader**, and **OrbitControls** to display interactive 3D models.

Included models:

* `stack_nanosheets.glb`
* `etch_gate_trenches.glb`
* `deposit_gate_material.glb`
* `form_gaa_structure.glb`

Users can:

* Rotate models
* Zoom in and out
* Pan around the model

### 3. Flashcard System

Each fabrication step has an interactive flashcard.

* **Front:** Displays the step title
* **Back:** Displays a brief explanation and bullet points
* Clicking the card triggers an animated 3D flip

### 4. Error Handling

If a 3D model fails to load, a red error message is displayed to the user.

### 5. Memory Optimization

Previous 3D models and their materials are properly disposed of before loading a new model to help prevent memory leaks.

### 6. Dynamic Resize

The 3D viewer automatically updates the camera and renderer when the browser window is resized.

## GAA Fabrication Steps

### Step 1: Stack Nanosheets

Stack alternating layers of silicon (Si) and silicon-germanium (SiGe).

* Start with a silicon wafer
* Deposit SiGe and Si in alternating layers
* Use chemical vapor deposition

**Model:** `stack_nanosheets.glb`

### Step 2: Etch Gate Trenches

Pattern and etch the gate trenches using lithography.

* Apply photoresist
* Expose and develop to create the trench pattern
* Etch vertically to form deep trenches

**Model:** `etch_gate_trenches.glb`

### Step 3: Deposit Gate Oxide and Metal

Deposit the gate oxide and metal gate materials.

* Use ALD to deposit a high-k gate dielectric
* Deposit the metal gate
* Use CMP to planarize the surface

**Model:** `deposit_gate_material.glb`

### Step 4: Form GAA Structure

Create the final Gate-All-Around structure.

* Remove the sacrificial SiGe layers
* Leave the Si nanosheets suspended
* Complete spacer and contact formation
* Finalize the device stack

**Model:** `form_gaa_structure.glb`

## Project Structure

```text
GAA-Fabrication-Tutorial/
│
├── gaa_fabrication.html
├── stack_nanosheets.glb
├── etch_gate_trenches.glb
├── deposit_gate_material.glb
└── form_gaa_structure.glb
```

## Technologies Used

* **HTML5**
* **CSS3**
* **JavaScript**
* **Three.js**
* **GLTFLoader**
* **OrbitControls**
* **GLB 3D Models**

## How It Works

The sidebar contains buttons for each GAA fabrication step.

When a step is selected:

1. The flashcard title is updated.
2. The flashcard description is updated.
3. The flashcard is reset to its front side.
4. The corresponding `.glb` model is loaded into the 3D viewer.
5. The previous model is removed and disposed of to reduce memory usage.

Three.js renders the 3D model while `OrbitControls` allows the user to rotate, zoom, and pan around it.

## Requirements

* A modern web browser
* Chrome or Edge recommended
* Internet connection for the Three.js CDN
* All required `.glb` models in the same folder as the HTML file

## How to Run

1. Save the file as:

```text
gaa_fabrication.html
```

2. Place the `.glb` models in the same folder:

```text
gaa_fabrication.html
stack_nanosheets.glb
etch_gate_trenches.glb
deposit_gate_material.glb
form_gaa_structure.glb
```

3. Open `gaa_fabrication.html` in a modern browser.

4. Click a fabrication step in the sidebar to:

   * View its 3D model
   * Read its description
   * Interact with the model using the mouse

5. Click the flashcard to flip it and view additional information.

## 3D Models

| Step                         | Model                       |
| ---------------------------- | --------------------------- |
| Stack Nanosheets             | `stack_nanosheets.glb`      |
| Etch Gate Trenches           | `etch_gate_trenches.glb`    |
| Deposit Gate Oxide and Metal | `deposit_gate_material.glb` |
| Form GAA Structure           | `form_gaa_structure.glb`    |

## Optional Improvements

Future versions could include:

* Progress tracker such as **"Step 1 of 4"**
* Automatic model rotation when idle
* A **Next Step** button on the flashcard
* Animated transitions when loading models
* Fade-in/fade-out effects between models

## Educational Purpose

This project is designed as an interactive educational tool for learning about the major stages of **Gate-All-Around (GAA) semiconductor fabrication**.

The combination of 3D visualization and interactive flashcards provides a visual way to explore the fabrication process step by step.
