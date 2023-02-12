# perfectgrain

Add noise grain to images.

Limitations: The images should not be bigger than the filter.

<p align="center">
  <img src="in/SMPTE_Color_Bars_16x9.png" alt="logo" width="500px"/>
  <br>
  <i>Input example</i>
</p>

<p align="center">
  <img src="out/SMPTE_Color_Bars_16x9.png" alt="logo" width="500px"/>
  <br>
  <i>Output example with opacity at 170</i>
</p>

# Install dependencies

## Using conda (recommended)

Install [miniconda](https://docs.conda.io/en/latest/miniconda.html), then run:

`conda env create -f environment.yaml`

## Using Python

Install Python 3.8.5 and run:

`pip install -r requirements.txt`

# How to use

- Place the images in the `in` folder
- Use either of the run methods and check the `out` folder afterwards:

## Powershell script

- Execute the script `run.ps1`

## Python command

- Activate the environment if using conda: `conda activate perfectgrain`
- Execute the script: `python ./add_filter.py in out 'filters/Ilford HP5.jpg' 170`

# Configuration

Change the python command to use different folders, filters or opacities.

`python add_filter.py in out filter opacity`

- in: input folder path
- out: output folder path
- filter: filter image path
- opacity: int between 0 and 255, where 0 is transparent

# Credits

Film grain by [filmcomposite](https://www.filmcomposite.com/free-stuff/free-35mm-film-grain-stills).
