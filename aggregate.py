#!/usr/bin/env python

import csv
import json
import numpy

plots = []

#load densities and compute std/mean
densities = []
with open('config.json') as config_f:
    config = json.load(config_f)
    for output_dir in config["outputs"]:
        print("loading", output_dir+"/density.csv")
        density  = numpy.genfromtxt(output_dir+"/density.csv", delimiter=',')
        densities.append(density)

    density_std = numpy.std(densities, axis=0)
    numpy.savetxt('density.std.csv', density_std)
    density_mean = numpy.mean(densities, axis=0)
    numpy.savetxt('density.mean.csv', density_mean)

#generate heatmap from density std/mean
data = {
    "type": "heatmap",
    "z": density_std.tolist(),
}
plot = {}
plot["type"] = "plotly"
plot["name"] = "density std"
plot["data"] = [data]
plot["layout"] = {}
plots.append(plot)

#save product.json
product = {}
product["brainlfe"] = plots
with open("product.json", "w") as fp:
    json.dump(product, fp)
