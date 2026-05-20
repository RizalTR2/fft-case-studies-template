# Computational Physics: Applied Fast Fourier Transform (FFT)

Welcome to the comprehensive case study assignment on the Discrete Fourier Transform. In this assignment, you will apply the FFT algorithm to three distinct physical datasets to extract meaningful frequency-domain information.

## Objective
Your task is to complete the mathematical and computational analysis within the provided Jupyter Notebooks and publish your findings as a public web portfolio using GitHub Pages.

## Step-by-Step Instructions

### Step 1: Fork and Clone the Repository
1. Click the **Fork** button at the top right of this repository to create a copy under your own GitHub account.
2. Clone your forked repository to your local computational environment:
   `git clone https://github.com/YOUR-USERNAME/fft-case-studies-template.git`
3. Navigate into the directory:
   `cd fft-case-studies-template`

### Step 2: Set Up the Environment
Ensure you have the required Python libraries installed. It is highly recommended to use a virtual environment.
`pip install -r requirements.txt`

### Step 3: Conduct the Analysis
Navigate to the `notebooks/` directory. You will find three case studies. For each notebook, you must:
* Import the provided raw data from the `data/` folder.
* Compute the FFT using `numpy.fft` or `scipy.fft`.
* Plot the time-domain signal and the frequency-domain power spectrum.
* Provide written physical interpretations of your mathematical results using Markdown cells.

### Step 4: Compile to HTML
Once your analysis is complete and your notebooks are fully executed (ensure all plots are visible), you must compile them into static HTML files for web deployment. Run the following commands in your terminal:

`jupyter nbconvert --to html notebooks/Case_1_Astrophysics.ipynb --output-dir docs/`
`jupyter nbconvert --to html notebooks/Case_2_Climatology.ipynb --output-dir docs/`
`jupyter nbconvert --to html notebooks/Case_3_Acoustics.ipynb --output-dir docs/`

*Note: The `docs/index.html` file acts as your homepage and already contains links to these generated files.*

### Step 5: Deploy via GitHub Pages
1. Commit and push your changes back to your GitHub repository:
   `git add .`
   `git commit -m "Completed FFT analysis and compiled HTML"`
   `git push origin main`
2. On your GitHub repository page, navigate to **Settings** > **Pages**.
3. Under **Build and deployment**, set the Source to **Deploy from a branch**.
4. Select the **main** branch, and change the folder from `/(root)` to `/docs`.
5. Click **Save**. Within a few minutes, your computational portfolio will be live!

## Evaluation Criteria
Your submission will be evaluated on the following:
1. **Mathematical Accuracy:** Correct implementation of the FFT, proper normalization, and accurate formulation of the frequency bins (Nyquist limits).
2. **Computational Efficiency:** Clean, well-commented Python code without redundant loops.
3. **Scientific Communication:** The clarity of your data visualizations (labeled axes, correct units) and the depth of your written physical interpretations.

## Data Sources
*https://github.com/datasets/co2-ppm-daily/blob/main/data/co2-ppm-daily.csv*
*https://github.com/ThinamXx/TimeSeries_Sunspots/blob/master/sunspots.csv*
## Penggunaan Ai
Pada pengerjaan *case-based* ini, kami menggunakan:
1. **Gemini 3.1 Pro** untuk *generate* kode Python;
2. **Claude Sonnet 4.6** untuk mengidentifikasi referensi;

## Penggunaan Aplikasi Lain
1. **Jupyter Software** untuk ...
2. **Miniconda** untuk ....
