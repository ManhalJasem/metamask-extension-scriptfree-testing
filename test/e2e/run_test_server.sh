#!/usr/bin/env bash

set -x
set -e
set -u
set -o pipefail

export PATH="$PATH:./node_modules/.bin"
export GANACHE_ARGS='--blockTime 2 --quiet'

concurrently --kill-others \
  --names 'ganache,dapp' \
  --prefix '[{time}][{name}]' \
  --success first \
  'yarn ganache:start' \
  'yarn dapp'