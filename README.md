LPA without  overlapping  + node influence
====================================
### Installation 
1. git clone https://github.com/bousrihIness/LPA-Influence.git

2. Open python project in PyCharm (or any Python editor)

### Requirements
The codebase is implemented in Python 3.9.2. Package versions used for development are :
```
jsonschema        4.4.0
tqdm              4.26.3
pandas            1.3.2
networkx          2.6.3
numpy             1.21.2
texttable         0.15.0
```

--------------------------------------------------------------------------------

### Datasets
<p align="justify">
The code takes an input graph in a csv or json file. Every row indicates an edge between two nodes separated by a comma. The input dataset is included in the  `data/` directory.</p>


### Run project:
In the terminal : 
```sh
$ python src/label_propagation.py
```




--------------------------------------------------------------------------------
