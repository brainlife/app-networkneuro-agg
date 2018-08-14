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
plot = {}
plot["type"] = "plotly"
plot["name"] = "density std"
plot["data"] = [{
    "type": "heatmap",
    "colorscale": "Portland",
    "z": density_std.tolist(),
}]
plot["layout"] = {}
plots.append(plot)

plot = {}
plot["type"] = "plotly"
plot["name"] = "density std"
plot["data"] = [{
    "type": "heatmap",
    "colorscale": "Hot",
    "z": density_mean.tolist(),
}]
plot["layout"] = {}
plots.append(plot)

#save product.json
product = {}
product["brainlife"] = plots
with open("product.json", "w") as fp:
    json.dump(product, fp)
