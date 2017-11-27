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

### Install
```pip install dist/wf-ds-tools-<version>.tar.gz```

## Description
### Brief
1. DS tools package
2. DTClassifier.fit method
3. dst - entry point for all tools (from any dir)

#### dst
```
$ dst --help
usage: ds_ctl.py [-h] {dtc_fit} ...

DS CTL (v.1.0.3)

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

##### Remarks
**0)** All tools work in **Dry-run** mode by default

**1)** Default values of limits (cpu, rss) is None. If limit is None then system resource limit is not changed.

**2)** All resource limits are ulimit limits

**-cpu**:

```
 resource.RLIMIT_CPU
    The maximum amount of processor time (in seconds) that a process can use. If this limit is exceeded, a SIGXCPU signal is sent to the process.
```

**-rss**:

```
resource.RLIMIT_RSS
    The maximum resident set size that should be made available to the process.
```

**-heap**:

```
resource.RLIMIT_DATA
    The maximum size (in bytes) of the process’s heap.

```

**-stack**:

```
resource.RLIMIT_STACK
    The maximum size (in bytes) of the call stack for the current process. This only affects the stack of the main thread in a multi-threaded process.
```

**3)** To add limits (one of dstools.utils.limits.DEFAULT_ARGS key, for example *'heap'*) to cmd arguments you need to add limit description to dstools.utils.limits.ARGS list

```
DEFAULT_KWARGS = {
    'max_cpu_seconds': None,
    'max_heap': None,
    'max_rss': None,
    'max_stack': None,
}
```

```
ARGS = [
    ...
    Arg(
        flags=['-heap', '--max-heap'],
        dest='max_heap', type=int, choices=None,
        help='Max used memory for data in MB (default: {default}MB, (-1: INF))'
    ),
]
```

**4)** To add DTC fit arguments (one of dstools.tree.dtc.DEFAULT_KWARGS key) to cmd args you need to add argument description to dstools.tree.dtc.ARGS (in the same way as in the point 3)
