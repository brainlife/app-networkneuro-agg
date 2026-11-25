# app-networkneuro-agg

<!-- brainlife-app:begin (generated from the App manifest; edit the manifest, not this block) -->

**Aggregates density and count connectivity matrices from several networkneuro outputs into mean and standard-deviation matrices, shown as heatmaps.**

Reads density.csv and count.csv from each input, computes the element-wise mean and standard deviation with numpy, writes density/count mean and std CSV files, and adds plotly heatmaps to the job's product. It registers no output datatype; the CSVs stay in the job's working directory.

Run it on brainlife.io: [https://doi.org/10.25663/bl.app.89](https://doi.org/10.25663/bl.app.89)

| Input | Datatype | Required | Description |
|---|---|---|---|
| `inputs` | `neuro/networkneuro` | yes | Several networkneuro outputs; each must contain density.csv and count.csv. All matrices must have the same size (same parcellation). |

Runtime: 1 CPUs.

<!-- brainlife-app:end -->

Network Neuro Output Aggregator
