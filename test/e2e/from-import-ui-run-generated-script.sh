#!/usr/bin/env bash

set -x
set -e
set -u
set -o pipefail

export PATH="$PATH:./node_modules/.bin"
export GANACHE_ARGS='--blockTime 2 --quiet'
export GANACHE_ARGS="$GANACHE_ARGS --deterministic --account=0x53CB0AB5226EEBF4D872113D98332C1555DC304443BEE1CF759D15798D3C55A9,25000000000000000000"

concurrently --kill-others \
  --names 'ganache,dapp,generated_script' \
  --prefix '[{time}][{name}]' \
  --success first \
  'yarn ganache:start' \
  'yarn dapp' \
  'sleep 5 && cd test/e2e/script-free-implementation && pipenv run python3 -m test_script.metamask_exp.metamask_tests_runner'