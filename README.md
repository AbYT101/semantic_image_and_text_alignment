# Automated Storyboard Synthesis for Digital Advertising

## Overview

This repository contains the code and resources for the 10 Academy Cohort B Week 12 Challenge: Semantic Image and Text Alignment for Automated Storyboard Synthesis in Digital Advertising. The objective is to leverage machine learning, natural language processing, and computer vision techniques to transform textual descriptions of advertisement concepts and assets into detailed, visually compelling storyboards.

## Business Objective

Adludio, a leader in online mobile advertising, aims to automate the end-to-end process of advertising production. This project will enable the rapid generation of creative concepts based on client briefs, significantly reducing the traditional turnaround time and enhancing the efficiency of ad campaign creation.

## Features

- **Input Processing:** Accepts textual inputs detailing the concept, assets, and size of an advertisement.
- **ML and DL Integration:** Utilizes machine learning and deep learning models for image segmentation, object detection, and text generation.
- **AutoGen Agents:** Employs AutoGen agents for asset analysis and automatic asset editing.
- **Storyboard Composition:** Automatically composes individual ad frames into a cohesive storyboard.

## Directory Structure

```
.
├── data
│   ├── assets
│   ├── concepts
│   └── storyboards
├── notebooks
│   ├── EDA.ipynb
│   ├── Image_Analysis.ipynb
│   ├── Text_Analysis.ipynb
│   └── Storyboard_Composition.ipynb
├── src
│   ├── data_processing.py
│   ├── image_analysis.py
│   ├── text_analysis.py
│   └── storyboard_composition.py
├── models
│   ├── yolo_model.pth
│   ├── unet_model.pth
│   └── text_generation_model.pth
├── requirements.txt
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.8+
- PyTorch
- TensorFlow
- OpenCV
- NLTK
- Transformers (Hugging Face)
- YOLOv5

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/storyboard-synthesis.git
cd storyboard-synthesis
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

### Data Preparation

Place your data files in the `data` directory. The `assets` folder should contain the images used to construct the creatives, and the `concepts` folder should contain JSON files outlining the concepts.

### Running the Notebooks

1. **Exploratory Data Analysis (EDA):**

   ```bash
   jupyter notebook notebooks/EDA.ipynb
   ```

2. **Image Analysis:**

   ```bash
   jupyter notebook notebooks/Image_Analysis.ipynb
   ```

3. **Text Analysis:**

   ```bash
   jupyter notebook notebooks/Text_Analysis.ipynb
   ```

4. **Storyboard Composition:**

   ```bash
   jupyter notebook notebooks/Storyboard_Composition.ipynb
   ```

### Running the Scripts

You can also run the individual scripts for specific tasks:

```bash
python src/data_processing.py
python src/image_analysis.py
python src/text_analysis.py
python src/storyboard_composition.py
```


## Resources

- [Dynamic Creative & Content Optimization](https://www.claravine.com/blog/dynamic-creative-content-optimization-dco-marketing-advertising/)
- [Machine Learning in Digital Advertising](https://www.forbes.com/sites/forbestechcouncil/2020/10/26/how-machine-learning-is-shaping-the-future-of-advertising/)
- [YOLO Object Detection](https://pjreddie.com/darknet/yolo/)
- [UNET++ Image Segmentation](https://arxiv.org/abs/1912.05074)

## License

This project is licensed under the Apache 2.0 License. See the LICENSE file for details.



## Contributors

- [@abyt101](https://github.com/AbYT101) - Abraham Teka
<br>

## Contact

For questions or support, please contact me throug [email](mailto:aberhamyirsaw@gmail.com).


## Challenge by

![10 Academy](https://static.wixstatic.com/media/081e5b_5553803fdeec4cbb817ed4e85e1899b2~mv2.png/v1/fill/w_246,h_106,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/10%20Academy%20FA-02%20-%20transparent%20background%20-%20cropped.png)