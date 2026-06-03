# Event-Camera Simulation Resources

Companion repository for **Event-Camera Simulation: A Review**.

This page collects papers and public resources related to event-camera simulation. The list follows the review's mechanism-based categories: physics- and rule-based simulation, learning-based event generation, and Evaluation and Sim-to-Real Analysis resources.

Last updated: 2026-06-03.

## Project Page

Public site: <https://bonaparte233.github.io/event_camera_simulation/>

## Review Paper

**Event-Camera Simulation: A Review**

The paper link and BibTeX entry for the review will be added after the preprint or published version is public.

## Physics- and Rule-Based Event-Camera Simulation

### Threshold-Based Simulation

- **Pineda Garcia et al.**, *pyDVS: An Extensible Real-Time Dynamic Vision Sensor Emulator*, IEEE SSCI 2016. [[paper](https://doi.org/10.1109/SSCI.2016.7850249)] [[code](https://github.com/chanokin/pyDVS)]
- **Bi and Andreopoulos**, *PIX2NVS: Parameterized Conversion of Pixel-Domain Video Frames to Neuromorphic Vision Streams*, ICIP 2017. [[paper](https://doi.org/10.1109/ICIP.2017.8296630)] [[code](https://github.com/PIX2NVS/PIX2NVS)]
- **Mueggler et al.**, *The Event-Camera Dataset and Simulator: Event-Based Data for Pose Estimation, Visual Odometry, and SLAM*, IJRR 2017. [[paper](https://doi.org/10.1177/0278364917691115)] [[project](https://rpg.ifi.uzh.ch/davis_data.html)] [[code](https://github.com/uzh-rpg/rpg_davis_simulator)]
- **Rebecq, Gehrig, and Scaramuzza**, *ESIM: an Open Event Camera Simulator*, CoRL 2018. [[paper](https://proceedings.mlr.press/v87/rebecq18a.html)] [[project](https://rpg.ifi.uzh.ch/esim.html)] [[code](https://github.com/uzh-rpg/rpg_esim)]
- **Scheerlinck et al.**, *CED: Color Event Camera Dataset*, CVPR Workshops 2019. [[paper](https://doi.org/10.1109/CVPRW.2019.00215)] [[project](https://rpg.ifi.uzh.ch/CED.html)]
- **Gehrig et al.**, *Video to Events: Recycling Video Datasets for Event Cameras*, CVPR 2020. [[paper](https://doi.org/10.1109/CVPR42600.2020.00364)] [[code](https://github.com/uzh-rpg/rpg_vid2e)]
- **Pantho et al.**, *Event Camera Simulator Design for Modeling Attention-based Inference Architectures*, Journal of Real-Time Image Processing 2022. [[paper](https://doi.org/10.1007/s11554-021-01191-y)]
- **Ziegler et al.**, *Real-time Event Simulation with Frame-Based Cameras*, ICRA 2023. [[paper](https://arxiv.org/abs/2209.04634)] [[project](https://cogsys-tuebingen.github.io/realtime_event_simulator/)] [[code](https://github.com/cogsys-tuebingen/event_simulator)]
- **Ma et al.**, *I2E: Real-Time Image-to-Event Conversion for High-Performance Spiking Neural Networks*, AAAI 2026. [[paper](https://doi.org/10.1609/aaai.v40i3.37179)] [[code](https://github.com/Ruichen0424/I2E)]

### Sensor-Level Simulation

- **Stoffregen et al.**, *Reducing the Sim-to-Real Gap for Event Cameras*, ECCV 2020. [[paper](https://doi.org/10.1007/978-3-030-58583-9_32)] [[project](https://timostoff.github.io/20ecnn)] [[code](https://github.com/TimoStoff/event_cnn_minimal)]
- **Joubert et al.**, *Event Camera Simulator Improvements via Characterized Parameters*, Frontiers in Neuroscience 2021. [[paper](https://doi.org/10.3389/fnins.2021.702765)]
- **Hu, Liu, and Delbruck**, *v2e: From Video Frames to Realistic DVS Events*, CVPR Workshops 2021. [[paper](https://doi.org/10.1109/CVPRW53098.2021.00144)] [[code](https://github.com/SensorsINI/v2e)]
- **Radomski et al.**, *Enhanced Frame and Event-Based Simulator and Event-Based Video Interpolation Network*, arXiv 2021. [[paper](https://arxiv.org/abs/2112.09379)]
- **Mou et al.**, *Accurate Event Simulation using High-Speed Videos*, Electronic Imaging 2022. [[paper](https://doi.org/10.2352/EI.2022.34.7.ISS-242)]
- **Lin et al.**, *DVS-Voltmeter: Stochastic Process-Based Event Simulator for Dynamic Vision Sensors*, ECCV 2022. [[paper](https://doi.org/10.1007/978-3-031-20071-7_34)] [[code](https://github.com/Lynn0306/DVS-Voltmeter)]
- **Jiang, Zhou, and Lin**, *ADV2E: Bridging the Gap Between Analogue Circuit and Discrete Frames in the Video-to-Events Simulator*, arXiv 2024. [[paper](https://arxiv.org/abs/2411.12250)]
- **Ning et al.**, *Raw2Event: Converting Raw Frame Camera into Event Camera*, arXiv 2025. [[paper](https://arxiv.org/abs/2509.06767)]
- **Lu et al.**, *Hybrid Event Frame Sensors: Modeling, Calibration, and Simulation*, arXiv 2025. [[paper](https://arxiv.org/abs/2511.18037)] [[project](https://yunfanlu.github.io/HESIM/)]
- **Lou et al.**, *V2V: Scaling Event-Based Vision through Efficient Video-to-Voxel Simulation*, NeurIPS 2025. [[paper](https://arxiv.org/abs/2505.16797)] [[project](https://neurips.cc/virtual/2025/poster/118917)] [[code](https://github.com/HYLZ-2019/V2V)]

### Scene-Level Simulation

- **Kaiser et al.**, *Towards a Framework for End-to-End Control of a Simulated Vehicle with Spiking Neural Networks*, SIMPAR 2016. [[paper](https://doi.org/10.1109/SIMPAR.2016.7862386)]
- **Li et al.**, *InteriorNet: Mega-scale Multi-sensor Photo-realistic Indoor Scenes Dataset*, BMVC 2018. [[project](https://interiornet.org/)] [[paper](https://interiornet.org/items/interiornet_paper.pdf)]
- **Rizzo, Schuman, and Plank**, *Event-Based Camera Simulation Wrapper for Arcade Learning Environment*, ICONS 2022. [[paper](https://doi.org/10.1145/3546790.3546817)]
- **Palinauskas et al.**, *Generating Event-Based Datasets for Robotic Applications using MuJoCo-ESIM*, ICONS 2023. [[paper](https://doi.org/10.1145/3589737.3605984)] [[code](https://github.com/fortissNC/Mujoco-ESIM)]
- **Tsuji et al.**, *Event-Based Camera Simulation Using Monte Carlo Path Tracing with Adaptive Denoising*, ICIP 2023. [[paper](https://doi.org/10.1109/ICIP49359.2023.10222771)] [[code](https://github.com/0V/ESIM-AD)]
- **Li et al.**, *BlinkFlow: A Dataset to Push the Limits of Event-based Optical Flow Estimation*, IROS 2023. [[paper](https://arxiv.org/abs/2303.07716)] [[project](https://zju3dv.github.io/blinkflow/)] [[code](https://github.com/zju3dv/blink_sim)]
- **Han et al.**, *Physical-Based Event Camera Simulator*, ECCV 2024. [[paper](https://doi.org/10.1007/978-3-031-72995-9_2)] [[code](https://github.com/lanpokn/PECS_trail_version)]
- **Manabe et al.**, *Monte Carlo Path Tracing and Statistical Event Detection for Event Camera Simulation*, ICCP 2024. [[paper](https://doi.org/10.1109/ICCP61108.2024.10644728)] [[code](https://github.com/ichi-raven/MC-EBCS)]
- **Reinold, Ghosh, and Gallego**, *Combined Physics and Event Camera Simulator for Slip Detection*, WACV Workshops 2025. [[paper](https://doi.org/10.1109/WACVW65960.2025.00104)] [[code](https://github.com/tub-rip/event_slip)]
- **Rodriguez et al.**, *An Event Camera Simulator for Arbitrary Viewpoints Based on Neural Radiance Fields*, VISAPP 2025. [[paper](https://doi.org/10.5220/0013388400003912)]
- **Li et al.**, *GS2E: Gaussian Splatting is an Effective Data Generator for Event Stream Generation*, arXiv 2025. [[paper](https://arxiv.org/abs/2505.15287)] [[project](https://intothemild.github.io/GS2E.github.io/)] [[code](https://github.com/PKU-YuanGroup/GS2E)]
- **Li et al.**, *EventTracer: Fast Path Tracing-Based Event Stream Rendering*, arXiv 2025. [[paper](https://arxiv.org/abs/2508.18071)]
- **Kyatham et al.**, *EREBUS: End-to-End Robust Event Based Underwater Simulation*, arXiv 2025. [[paper](https://arxiv.org/abs/2511.01381)]
- **Middleton et al.**, *Modelling and Simulation of Neuromorphic Datasets for Anomaly Detection in Computer Vision*, arXiv 2026. [[paper](https://arxiv.org/abs/2602.23514)] [[code](https://github.com/EDGYOrganism/ANTShapes)]
- **CARLA DVS plugin** [[platform paper](https://arxiv.org/abs/1711.03938)] [[project](https://carla.org/)] [[docs](https://carla.readthedocs.io/en/latest/ref_sensors/#dvs-camera)] [[code](https://github.com/carla-simulator/carla)]
- **Microsoft AirSim Event Camera simulation plugin**. [[docs](https://microsoft.github.io/AirSim/event_sim/)] [[code](https://github.com/microsoft/AirSim)]

### Differentiable / Trainable Extensions

- **Nehvi et al.**, *Differentiable Event Stream Simulator for Non-Rigid 3D Tracking*, CVPR Workshops 2021. [[paper](https://arxiv.org/abs/2104.15139)] [[project](http://gvv.mpi-inf.mpg.de/projects/Event-based_Non-rigid_3D_Tracking)]
- **Gu et al.**, *How to Learn a Domain-Adaptive Event Simulator*, ACM MM 2021. [[paper](https://doi.org/10.1145/3474085.3475229)] [[code](https://github.com/iCVTEAM/LETGAN)]
- **Greene et al.**, *SENPI: A PyTorch-Enabled Tool for Synthetic Event Camera Data Generation and Algorithm Development*, SPIE Synthetic Data for AI/ML 2025. [[paper](https://doi.org/10.1117/12.3053238)] [[code](https://github.com/joeg18/senpi_ebi)]

## Learning-Based Event Generation

### Direct Event Generation

- **Zhu et al.**, *EventGAN: Leveraging Large Scale Image Datasets for Event Cameras*, ICCP 2021. [[paper](https://doi.org/10.1109/ICCP51581.2021.9466265)] [[code](https://github.com/alexzzhu/EventGAN)]
- **Masuda et al.**, *Neural Implicit Event Generator for Motion Tracking*, ICRA 2022. [[paper](https://doi.org/10.1109/ICRA46639.2022.9812142)]
- **Zhang et al.**, *V2CE: Video to Continuous Events Simulator*, ICRA 2024. [[paper](https://doi.org/10.1109/ICRA57147.2024.10609864)] [[code](https://github.com/ucsd-hdsi-dvs/V2CE-Toolbox)]
- **Bhattacharya et al.**, *EvDNeRF: Reconstructing Event Data with Dynamic Neural Radiance Fields*, WACV 2024. [[paper](https://doi.org/10.1109/WACV57701.2024.00574)] [[project](https://www.anishbhattacharya.com/research/evdnerf)] [[code](https://github.com/anish-bhattacharya/EvDNeRF)]

### Conditional Event Generation

- **Gu et al.**, *Reliable Event Generation With Invertible Conditional Normalizing Flow*, IEEE TPAMI 2024. [[paper](https://doi.org/10.1109/TPAMI.2023.3326538)]
- **Ott, Wang, and Liu**, *Text-to-Events: Synthetic Event Camera Streams from Conditional Text Input*, NICE 2024. [[paper](https://arxiv.org/abs/2406.03439)]
- **Zhang et al.**, *An Event-Oriented Diffusion-Refinement Method for Sparse Events Completion*, Scientific Reports 2024. [[paper](https://doi.org/10.1038/s41598-024-57333-2)]
- **Hu et al.**, *ControlEvents: Controllable Synthesis of Event Camera Data with Foundational Prior from Image Diffusion Models*, WACV 2026. [[paper](https://arxiv.org/abs/2509.22864)] [[project](https://yuxuan-xue.com/controlevents/)]

## **Evaluation and Sim-to-Real Analysis**

- **Cannici et al.**, *N-ROD: A Neuromorphic Dataset for Synthetic-to-Real Domain Adaptation*, CVPR Workshops 2021. [[paper](https://openaccess.thecvf.com/content/CVPR2021W/EventVision/papers/Cannici_N-ROD_A_Neuromorphic_Dataset_for_Synthetic-to-Real_Domain_Adaptation_CVPRW_2021_paper.pdf)] [[project](https://n-rod-dataset.github.io/home/)]
- **Planamente et al.**, *DA4Event: Towards Bridging the Sim-to-Real Gap for Event Cameras Using Domain Adaptation*, IEEE RA-L 2021. [[paper](https://doi.org/10.1109/LRA.2021.3093870)] [[code](https://github.com/DA4EVENT/home)]
- **Ziegler et al.**, *BiasBench: A Reproducible Benchmark for Tuning the Biases of Event Cameras*, CVPR Workshops 2025. [[paper](https://doi.org/10.1109/CVPRW67362.2025.00493)] [[project](https://cogsys-tuebingen.github.io/biasbench/)] [[code](https://github.com/cogsys-tuebingen/biasbench)]
- **Chanda et al.**, *Event Quality Score (EQS): Assessing the Realism of Simulated Event Camera Streams via Distances in Latent Space*, CVPR Workshops 2025. [[paper](https://ieeexplore.ieee.org/document/11147485)] [[code](https://github.com/eventbasedvision/EQS)]
- **Tan, B N, and Chakravarthi**, *How Real is CARLA's Dynamic Vision Sensor? A Study on the Sim-to-Real Gap in Traffic Object Detection*, CVIP 2025. [[paper](https://arxiv.org/abs/2506.13722)]

## Contributing

Contributions are welcome through issues or pull requests. Please include the authors, paper title, venue/year, paper link, official project or code link when available.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the entry format and category labels.

## Citation

The citation for **Event-Camera Simulation: A Review** will be added when the paper becomes public. If you use this repository before then, please cite the individual papers listed above.
