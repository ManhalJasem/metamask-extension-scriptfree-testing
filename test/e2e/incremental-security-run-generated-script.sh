#!/usr/bin/env bash

set -x
set -e
set -u
set -o pipefail

export PATH="$PATH:./node_modules/.bin"
export GANACHE_ARGS='--blockTime 2 --quiet'
export SELENIUM_BROWSER="chrome" 
export SELENIUM_CHROME_BINARY="./node_modules/.bin/chrome113"

export GANACHE_ARGS="$GANACHE_ARGS --deterministic --account=0x53CB0AB5226EEBF4D872113D98332C1555DC304443BEE1CF759D15798D3C55A9,25000000000000000000"
export GANACHE_ARGS="$GANACHE_ARGS --deterministic --account=0x53CB0AB5226EEBF4D872113D98332C1555DC304443BEE1CF759D15798D3C55A9,25000000000000000000"

export GANACHE_ARGS="$GANACHE_ARGS --deterministic --account=0x250F458997A364988956409A164BA4E16F0F99F916ACDD73ADCD3A1DE30CF8D1,0  --account=0x53CB0AB5226EEBF4D872113D98332C1555DC304443BEE1CF759D15798D3C55A9,25000000000000000000"

rm -rf test/e2e/script-free-implementation/chrome-profiles/mm-chrome-profile/*

concurrently --kill-others \
  --names 'ganache,sendwithprivatedapp,e2e' \
  --prefix '[{time}][{name}]' \
  --success first \
  'npm run ganache:start' \
  'npm run sendwithprivatedapp' \
  'sleep 5 && cd test/e2e/script-free-implementation && pipenv run python3 -m test_script.metamask_exp.incremental_security_tests_runner'