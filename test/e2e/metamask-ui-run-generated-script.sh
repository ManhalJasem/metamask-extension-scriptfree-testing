#!/usr/bin/env bash

set -x
set -e
set -u
set -o pipefail

export PATH="$PATH:./node_modules/.bin"
export GANACHE_ARGS='--blockTime 2 --quiet'
export SELENIUM_BROWSER="chrome" 
export SELENIUM_CHROME_BINARY="./node_modules/.bin/chrome113"

concurrently --kill-others \
  --names 'ganache,dapp,e2e' \
  --prefix '[{time}][{name}]' \
  --success first \
  'yarn ganache:start' \
  'yarn dapp' \
  'sleep 5 && mocha test/e2e/metamask-ui-setup-for-script-free.spec' 


concurrently --kill-others \
  --names 'ganache,dapp,generated_script' \
  --prefix '[{time}][{name}]' \
  --success first \
  'yarn ganache:start' \
  'yarn dapp' \
  'sleep 5 && cd test/e2e/script-free-implementation && pipenv run python3 -m test_script.metamask_exp.metamaskui_tests_runner'