#!/usr/bin/env python

import csv
import json
import numpy

plots = []

#load densities and compute std/mean
with open('config.json') as config_f:
    config = json.load(config_f)

    densities = []
    counts = []
    for output_dir in config["outputs"]:
        print("loading", output_dir+"/density.csv")
        density = numpy.genfromtxt(output_dir+"/density.csv", delimiter=',')
        densities.append(density)

        print("loading", output_dir+"/counts.csv")
        count = numpy.genfromtxt(output_dir+"/count.csv", delimiter=',')
        counts.append(count)

    density_std = numpy.std(densities, axis=0)
    numpy.savetxt('density.std.csv', density_std)
    density_mean = numpy.mean(densities, axis=0)
    numpy.savetxt('density.mean.csv', density_mean)

    count_std = numpy.std(counts, axis=0)
    numpy.savetxt('count.std.csv', count_std)
    count_mean = numpy.mean(counts, axis=0)
    numpy.savetxt('count.mean.csv', count_mean)

#generate heatmap from density std/mean
plot = {}
plot["type"] = "plotly"
plot["name"] = "density std"
plot["data"] = [{
    "type": "heatmap",
    "colorscale": "Portland",
    "z": density_std.tolist(),
}]
plot["layout"] = {
    "yaxis": {
        "autorange": "reversed"
    }
}
plots.append(plot)

plot = {}
plot["type"] = "plotly"
plot["name"] = "density mean"
plot["data"] = [{
    "type": "heatmap",
    "colorscale": "Hot",
    "z": density_mean.tolist(),
}]
#plot["layout"] = {}
plots.append(plot)

plot = {}
plot["type"] = "plotly"
plot["name"] = "count std"
plot["data"] = [{
    "type": "heatmap",
    "colorscale": "Portland",
    "z": count_std.tolist(),
}]
#plot["layout"] = {}
plots.append(plot)

plot = {}
plot["type"] = "plotly"
plot["name"] = "count mean"
plot["data"] = [{
    "type": "heatmap",
    "colorscale": "Hot",
    "z": count_mean.tolist(),
}]
#plot["layout"] = {}
plots.append(plot)

#save product.json
product = {}
product["brainlife"] = plots
with open("product.json", "w") as fp:
    json.dump(product, fp)
