#!/usr/bin/env bash

set -x
set -e
set -u
set -o pipefail

export PATH="$PATH:./node_modules/.bin"
export GANACHE_ARGS='--blockTime 2 --quiet'
export SELENIUM_CHROME_BINARY="./node_modules/.bin/chrome113"

concurrently --kill-others \
  --names 'ganache,dapp,e2e' \
  --prefix '[{time}][{name}]' \
  --success first \
  'yarn ganache:start' \
  'yarn dapp' \
  'sleep 5 && mocha test/e2e/metamask-ui-setup-for-script-free.spec' 


concurrently --kill-others \
  --names 'ganache,dapp,scriptfree' \
  --prefix '[{time}][{name}]' \
  --success first \
  'yarn ganache:start' \
  'yarn dapp' \
  'sleep 5 && cd test/e2e/script-free-implementation && pipenv run gen metamaskui'

export GANACHE_ARGS="$GANACHE_ARGS --deterministic --account=0x53CB0AB5226EEBF4D872113D98332C1555DC304443BEE1CF759D15798D3C55A9,25000000000000000000"
concurrently --kill-others \
  --names 'ganache,dapp,e2e' \
  --prefix '[{time}][{name}]' \
  --success first \
  'yarn ganache:start' \
  'yarn dapp' \
  'sleep 5 && mocha test/e2e/from-import-ui-setup-for-script-free.spec' 


concurrently --kill-others \
  --names 'ganache,dapp,scriptfree' \
  --prefix '[{time}][{name}]' \
  --success first \
  'yarn ganache:start' \
  'yarn dapp' \
  'sleep 5 && cd test/e2e/script-free-implementation && pipenv run gen from_import_ui'