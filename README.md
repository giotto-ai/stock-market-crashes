# Detecting Stock Market Crashes with Topological Data Analysis

## What is it?
A demo on how to build a simple topological detector to analyse stock market crashes. To learn more, have a look at our [blog post](https://towardsdatascience.com/detecting-stock-market-crashes-with-topological-data-analysis-7d5dd98abe42).

## Getting started

Spin up a virtual environment and install the required libraries:

```
virtualenv -p python3.7 env
pip install -r requirements.txt
```

To make plotly play nice with JupyterLab one needs to also run

```
# Avoid "JavaScript heap out of memory" errors during extension installation
# (OS X/Linux)
export NODE_OPTIONS=--max-old-space-size=4096
# (Windows)
set NODE_OPTIONS=--max-old-space-size=4096

# Jupyter widgets extension
jupyter labextension install @jupyter-widgets/jupyterlab-manager@1.0 --no-build

# FigureWidget support
jupyter labextension install plotlywidget@1.2.0 --no-build

# and jupyterlab renderer support
jupyter labextension install jupyterlab-plotly@1.2.0 --no-build

# JupyterLab chart editor support (optional)
jupyter labextension install jupyterlab-chart-editor@1.2 --no-build

# Build extensions (must be done to activate extensions since --no-build is used above)
jupyter lab build

# Unset NODE_OPTIONS environment variable
# (OS X/Linux)
unset NODE_OPTIONS
# (Windows)
set NODE_OPTIONS=
```
