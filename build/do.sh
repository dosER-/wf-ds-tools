#!/bin/bash

VENV_PARENT_PATH="$( cd "$(dirname "$0")" ; pwd -P )"
VENV_DIR="venv"
VENV_PATH="$VENV_PARENT_PATH/$VENV_DIR"
PROJECT_PATH="$VENV_PARENT_PATH/../src"

# signature: show_usage()
function show_usage() {
   	echo "USAGE: do.sh <cmd>     cmd ::= prepare_env|build_venv|remove_venv|update_deps|test_all|build_docs|build_pkg|upload_pkg|run"
    echo "$VENV_PATH"
}


# signature: build_venv()
function build_venv() {
    virtualenv --python=python2.7 $VENV_PATH
    source $VENV_PATH/bin/activate
    pip install -U pip==9.0.1
}


# signature: remove_venv()
function remove_venv() {
    if [ -d $VENV_PATH ]; then
        deactivate
        read -p "Start to remove $VENV_PATH? (Y/n)" -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]
        then
            rm -rf $VENV_PATH;
        fi
    fi
}


# signature: update_deps()
function update_deps() {
    pip install -U -r $VENV_PARENT_PATH/../.meta/packages
}


# signature: test_pkg()
function test_all() {
    python -m unittest discover $PROJECT_PATH
}


# signature: run(params)
function run() {
    PARAMS=$@
    CWD=`pwd`

    cd $PROJECT_PATH
    PYTHON_PATH=. python -m dstools.ds_ctl $PARAMS
    cd $CWD
}


# signature: build_docs()
function build_docs() {
    echo 'build_docs'
}


# signature: build_pkg()
function build_pkg() {
    python setup.py sdist
}


# signature: upload_pkg()
function upload_pkg() {
    echo 'upload_pkg'
}


source "$VENV_PATH/bin/activate"

case "$1" in
    prepare_env)
        remove_venv
        build_venv
        update_deps
    ;;
    build_venv)
        build_venv
    ;;
    remove_venv)
        remove_venv
    ;;
    update_deps)
        update_deps
    ;;
    test_all)
        test_all
    ;;
    run)
        run "${@:2}"
    ;;
    build_docs)
        build_docs
    ;;
    build_pkg)
        build_pkg
    ;;
    upload_pkg)
        upload_pkg
    ;;
    *)
        show_usage
        exit 1
    ;;
esac
