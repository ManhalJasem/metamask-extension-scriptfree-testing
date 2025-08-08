# Scriptfree Testing
Refere to this [paper](https://ieeexplore.ieee.org/document/9609160)

## Scriptfree Preparation
Follow steps in this [manual](./test/e2e/script-free-implementation/readme.md) before continuing next steps.

## Building Test Builds locally

- Choose the branch you want to test, git checkout ...
- Install [Node.js](https://nodejs.org) version 10
    - If you are using [nvm](https://github.com/creationix/nvm#installation) (recommended) running `nvm use` will automatically choose the right node version for you.
- Install [Yarn](https://yarnpkg.com/en/docs/install)
- Install dependencies: `yarn`
- Build the test project to the `./dist/` folder with `yarn build:test`.
Uncompressed builds can be found in `/dist`, compressed builds can be found in `/builds` once they're built.

## Running Script free Tests

- Run `yarn test:e2e:scriptfree`


## MetaMask Browser Extension

HERE is the link for the original MetaMask Extension: https://github.com/MetaMask/metamask-extension
