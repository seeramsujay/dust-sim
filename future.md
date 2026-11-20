# DustSim: Architectural Review & 3D Simulation Roadmap (future.md)

---

## 1. Architectural Code Review & Current State Analysis

DustSim is an edge-native, real-time 3D atmospheric particle transport simulator and proactive mitigation engine built on **Vite**, **React Three Fiber (R3F)**, **Three.js**, and **Tailwind CSS**. It models the physical dispersion of airborne particulate matter ($PM_{2.5} / PM_{10}$) across industrial construction zones, simulating Brownian drift under real-time wind and humidity vectors, while running an automated pre-wetting autopilot that commands water-mist sprinklers to intercept dust clouds.

### Architectural Strengths
- **GPU-Accelerated Particle Shaders:** Employs `THREE.Points` and customized vertex/fragment shaders for rendering thousands of dynamic dust and water droplet particles at 60 FPS.
- **Proactive Pre-Wetting Autopilot:** Rather than reactive triggering, evaluates 30-minute forward forecasts and triggers 60% mist output before particulate concentration breaches legal thresholds.
- **Glassmorphic Telemetry Dashboard:** Clean, responsive UI with interactive 3D OrbitControls, node deployment pins, real-time variance charts, and CSV export.

### Identified Bottlenecks & Modernization Needs
1. **CPU Particle Physics Bound:** Particle physics calculations (wind vector offsets, gravity integration, ground collision) are currently computed on the CPU per frame, creating performance bottlenecks above $10^4$ particles.
2. **Simplified Fluid Dynamics:** Employs basic kinematic equations rather than Navier-Stokes fluid dynamics for complex wind eddies around 3D building obstacles.
3. **Synthetic Sensor Feeds:** Relies on simulated sensor inputs rather than live WebSocket streams from physical DustVision edge gateways.

---

## 2. Strategic Engineering Roadmap

```mermaid
flowchart TD
    subgraph Phase 1: WebGPU Compute Shaders
        P1A[WebGPU Compute Shader Kernel] --> P1B[1,000,000 Particles at 60 FPS]
        P1B --> P1C[GPU Memory Shared Buffers]
    end

    subgraph Phase 2: 3D Digital Twin GIS Ingestion
        P2A[Cesium 3D Tiles & CityGML Ingestion] --> P2B[Obstacle-Aware Collision Grids]
        P2B --> P2C[Street Canyon Wind Vortex Shaders]
    end

    subgraph Phase 3: WebXR Virtual & Augmented Reality
        P3A[WebXR Immersive Inspection Mode] --> P3B[First-Person Site Superintendent Walkthrough]
        P3B --> P3C[Interactive Holographic Sprinkler Tuning]
    end

    subgraph Phase 4: Reinforcement Learning FinOps Water Balancer
        P4A[PPO Reinforcement Learning Agent] --> P4B[Minimum Water Usage vs PM Threshold SLA]
        P4B --> P4C[Automated Municipal Water Supply Integration]
    end

    Phase 1 --> Phase 2
    Phase 2 --> Phase 3
    Phase 3 --> Phase 4
```

---

## 3. Detailed Milestone Execution Plan

### Milestone 1: WebGPU Compute Shader Acceleration
- [ ] **WebGPU Particle Pipeline:** Migrate particle state integration from CPU JavaScript to a WebGPU compute shader pipeline, scaling capacity to $>500,000$ concurrent particles with zero CPU load.
- [ ] **Custom Gravitational Scavenging Shaders:** Model the exact collision physics between falling water mist droplets ($20\mu\text{m}$) and suspended PM10 particles.

### Milestone 2: 3D Digital Twin City Model Ingestion
- [ ] **CityGML & glTF Mesh Loading:** Allow site operators to load real architectural 3D building models and scaffolding meshes.
- [ ] **Wind Shadow & Eddy Simulation:** Compute aerodynamic wake zones behind buildings where dust gathers in stagnant air pockets.

### Milestone 3: WebXR Immersive Headset Support
- [ ] **VR Site Walkthrough:** Enable site safety engineers to inspect simulated dust plumes using Meta Quest / Apple Vision Pro via WebXR.
- [ ] **Spatial Holographic Markers:** Pin virtual water cannons and adjust spray cone angles in 3D space with hand gestures.

### Milestone 4: Reinforcement Learning Water-Conservation Autopilot
- [ ] **PPO Water Optimization Agent:** Train a Proximal Policy Optimization (PPO) agent to minimize total water consumption while keeping dust concentrations below $50\mu\text{g/m}^3$.
- [ ] **Live Telemetry WebSocket Bridge:** Connect the 3D visualizer directly to live DustVision IoT hardware gateways in real time.
