<h1 align="center">Network Neuro Aggregator</h1>

<p align="center">
  Mean and standard-deviation connectivity matrices, with heatmaps, from several networkneuro outputs.
</p>

<p align="center">
  <a href="https://github.com/brainlife/abcd-spec"><img src="https://img.shields.io/badge/ABCD_Spec-v1.1-green.svg" alt="ABCD Spec v1.1"></a>
  <a href="https://doi.org/10.25663/bl.app.89"><img src="https://img.shields.io/badge/Brainlife-bl.app.89-blue.svg" alt="Run on brainlife.io"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-lightgrey.svg" alt="MIT license"></a>
</p>

## 🧠 At a glance

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

> **Aggregates density and count connectivity matrices from several networkneuro outputs into mean and standard-deviation matrices, shown as heatmaps.**

Reads density.csv and count.csv from each input, computes the element-wise mean and standard deviation with numpy, writes density/count mean and std CSV files, and adds plotly heatmaps to the job's product. It registers no output datatype; the CSVs stay in the job's working directory.

| | |
|---|---|
| 📥 **Inputs** | `neuro/networkneuro` |
| ⚙️ **Resources** | 1 CPUs |
| 🔗 **Run it** | [doi.org/10.25663/bl.app.89](https://doi.org/10.25663/bl.app.89) |

#### 📥 Inputs

| Input | Datatype | Required | Description |
|---|---|---|---|
| `inputs` | `neuro/networkneuro` | yes | Several networkneuro outputs; each must contain density.csv and count.csv. All matrices must have the same size (same parcellation). |

<!-- brainlife-app:end -->

## 🚀 Running the App

### ☁️ On brainlife.io

Open the App at [doi.org/10.25663/bl.app.89](https://doi.org/10.25663/bl.app.89), select several `neuro/networkneuro` datasets from your project and press **Execute**. Each input must contain `density.csv` and `count.csv`, and all matrices must have the same size (that is, come from the same parcellation).

The App computes the element-wise mean and standard deviation of the density and count matrices across inputs, and shows four heatmaps (density mean, density std, count mean, count std) on the results page. It does not register an output datatype: the aggregated matrices remain in the job's working directory.

### 💻 Locally

The App runs directly on the host (no container). You need Python with NumPy.

1. Clone this repository.
2. Create `config.json` listing the networkneuro output directories to aggregate (see `config.json.sample`):

   ```json
   {
       "outputs": ["output1", "output2", "output3", "output4"]
   }
   ```

3. Run the App:

   ```bash
   ./main
   ```

## 📦 Outputs

```text
density.mean.csv   element-wise mean of the density matrices
density.std.csv    element-wise standard deviation of the density matrices
count.mean.csv     element-wise mean of the count matrices
count.std.csv      element-wise standard deviation of the count matrices
product.json       plotly heatmaps of the four matrices, shown on brainlife.io
```

The matrices are written with NumPy's default (space) delimiter.

## 🩺 Troubleshooting

- **The App fails while loading an input or computing the mean**: every input directory must contain both `density.csv` and `count.csv`, and all matrices must have the same dimensions.

## 📚 Citing

> [!TIP]
> If you use this App in your work, please cite the App, the software it builds on and brainlife.io (below). GitHub's **Cite this repository** button gives the App citation in APA and BibTeX.

- Network Neuro Aggregator. brainlife.io App. [doi:10.25663/bl.app.89](https://doi.org/10.25663/bl.app.89)
- Hayashi S, Caron BA, Heinsfeld AS, et al. brainlife.io: a decentralized and open-source cloud platform to support neuroscience research. *Nature Methods* 21:809–813 (2024). [doi:10.1038/s41592-024-02237-2](https://doi.org/10.1038/s41592-024-02237-2)
- Avesani P, McPherson B, Hayashi S, et al. The open diffusion data derivatives, brain data upcycling via integrated publishing of derivatives and reproducible open cloud services. *Scientific Data* 6:69 (2019). [doi:10.1038/s41597-019-0073-y](https://doi.org/10.1038/s41597-019-0073-y)

## 👥 Authors

- Soichi Hayashi

## 💰 Funding

[![Wellcome-226486/Z/22/Z](https://img.shields.io/badge/Wellcome-226486%2FZ%2F22%2FZ-purple.svg)](https://wellcome.org/)
[![NIH-NINDS-U24NS140384](https://img.shields.io/badge/NIH_NINDS-U24NS140384-green.svg)](https://reporter.nih.gov/project-details/11261037)
[![NIH-NINDS-UM1NS132207](https://img.shields.io/badge/NIH_NINDS-UM1NS132207-green.svg)](https://reporter.nih.gov/project-details/11411328)
[![NIH-NIBIB-R01EB029272](https://img.shields.io/badge/NIH_NIBIB-R01EB029272-green.svg)](https://reporter.nih.gov/project-details/10262925)
[![NIH-NIBIB-R01EB030896](https://img.shields.io/badge/NIH_NIBIB-R01EB030896-green.svg)](https://reporter.nih.gov/project-details/10428625)
[![NIH-NIMH-R01MH126699](https://img.shields.io/badge/NIH_NIMH-R01MH126699-green.svg)](https://reporter.nih.gov/project-details/10460628)
[![NIH-NIDCD-R01DC020088](https://img.shields.io/badge/NIH_NIDCD-R01DC020088-green.svg)](https://reporter.nih.gov/project-details/11140284)
[![NSF-BCS-1734853](https://img.shields.io/badge/NSF_BCS-1734853-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1734853)
[![NSF-BCS-2203524](https://img.shields.io/badge/NSF_BCS-2203524-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2203524)
[![NSF-IIS-1636893](https://img.shields.io/badge/NSF_IIS-1636893-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1636893)
[![NSF-OAC-2148729](https://img.shields.io/badge/NSF_OAC-2148729-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148729)
[![NSF-IIS-1912270](https://img.shields.io/badge/NSF_IIS-1912270-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1912270)
[![NSF-IIS-2148700](https://img.shields.io/badge/NSF_IIS-2148700-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148700)
[![NSF-OAC-1916518](https://img.shields.io/badge/NSF_OAC-1916518-blue.svg)](https://www.nsf.gov/awardsearch/showAward?AWD_ID=1916518)

<sub>brainlife.io is publicly funded, and acknowledging that support helps keep it running. This App was developed with support from Wellcome, the U.S. National Institutes of Health (including the BRAIN Initiative BRAIN CONNECTS program: The Axonal Projectome EXchange, U24NS140384, and the Center for Mesoscale Connectomics, UM1NS132207) and the U.S. National Science Foundation.</sub>

## ⚖️ License

MIT.
