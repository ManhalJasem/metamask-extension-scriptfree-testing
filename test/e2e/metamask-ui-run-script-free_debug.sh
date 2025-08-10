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
  'sleep 5 && ./node_modules/.bin/chrome113 --user-data-dir=test/e2e/script-free-implementation/chrome-profiles/mm-chrome-profile --load-extension=dist/chrome' 