## Development
1. checkout to wf-ds-tools
2. ```cd wf-ds-tools/```

### Prepare environment
1. cumulative prepare: ```build/do.sh prepare_env```

OR

1. remove old virtual env:
```build/do.sh remove_venv```
2. create virtual env in build/venv:
```build/do.sh build_venv```
3. update dependencies
```build/do.sh update_deps```

### Demo run
1. Test run in demo mode:
 ```build/do.sh run dtc_fit -D --verbose --demo```

### Run tests:
1. ```build/do.sh test_all```

### Build package
1. ```build/do.sh build_pkg```

### install
```pip install dist/wf-ds-tools-<version>.tar.gz

## Description
### Brief
1. DS tools package
2. DTClassifier.fit method
3. dst - entry point for all tools (from any dir)

#### dst
```
$ dst --help
usage: ds_ctl.py [-h] {dtc_fit} ...

DS CTL (v.1.0.0)

positional arguments:
  {dtc_fit}

optional arguments:
  -h, --help  show this help message and exit

```

#### dtc_fit
```
$ dst dtc_fit --help
usage: ds_ctl.py dtc_fit [-h] [-v] [-D] [-cpu MAX_CPU_SECONDS] [-rss MAX_RSS]
                         [-ip INPUT_PATH] [-op OUTPUT_PATH]
                         [-c {gini,entropy}] [-s {best,random}]
                         [-md MAX_DEPTH] [-mss MIN_SAMPLES_SPLIT]
                         [-msl MIN_SAMPLES_LEAF]

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Debug logging level (default: False)
  -D                    Dry run mode off (default: False)
  -cpu MAX_CPU_SECONDS, --max-cpu-seconds MAX_CPU_SECONDS
                        Max used CPU seconds (default: None (-1: INF))
  -rss MAX_RSS, --max-rss MAX_RSS
                        Max used rss memory in MB (default: NoneMB, (-1: INF))
  -ip INPUT_PATH, --input-path INPUT_PATH
                        Path to container directory (default: ~/input)
  -op OUTPUT_PATH, --output-path OUTPUT_PATH
                        Path to output file (default: ~/output/data.pickle)
  -c {gini,entropy}, --criterion {gini,entropy}
                        The function to measure the quality of a split
                        (default: gini)
  -s {best,random}, --splitter {best,random}
                        The strategy used to choose the split at each node
                        (default: best)
  -md MAX_DEPTH, --max-depth MAX_DEPTH
                        The maximum depth of the tree (default: None)
  -mss MIN_SAMPLES_SPLIT, --min-samples-split MIN_SAMPLES_SPLIT
                        The minimum number of samples required to split an
                        internal node (default: 2)
  -msl MIN_SAMPLES_LEAF, --min-samples-leaf MIN_SAMPLES_LEAF
                        The minimum number of samples required to be at a leaf
                        node (default: 1)

```
