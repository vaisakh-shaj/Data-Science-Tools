A set of tools that can come handy to Data Scientists
===============================================

[![DOI](https://zenodo.org/badge/77407674.svg)](https://zenodo.org/badge/latestdoi/77407674)

## Table of Contents

1. [Functionalities](#Functionalities)
2. [Dependencies](#dependencies)
3. [The `model`](#the-model)
4. [How to Use](#how-to-use)
5. [Future Work](#future-work)
6. [Citation](#citation)

This repo contains [adversarial image](https://arxiv.org/abs/1312.6199) crafting algorithms implemented in
**pure** Tensorflow.  The algorithms can be found in [attacks](attacks) folder.  The
implementation adheres to the principle **tensor-in, tensor-out**.  They all
return a Tensorflow operation which could be run through `sess.run(...)`.

## Functionalities

- Script for converting categorical values in a given dataframe to numerical values  (handle_non_numerical_data) 

  ```python
  handle_non_numerical_data(dataframe)
  ```

- Script for Tsne Plot for any data(sparse/non-sparse)  (tsne_plot) 

  ```python
    from plot_tsne import plotTsne
  ```

- Script to concatenate + normalize + balance + split  (CNBS) 

  ```python
    from CNBS import makeData
    cl=makeData(D,ratio)
                D has the format [(numpy1,label1),(numpy2,label2),(numpy3,label3)]
  ```


## Dependencies

1. Python3
2. Numpy
3. Pandas
4. Sklearn


## How to Use




## Future Work




## Citation
