## Script-Free Testing

This project integrates the “script-free” GUI-testing technique introduced by Kirinuki *et al.* (ICSME 2021 & SANER 2022). Instead of brittle, locator-based Selenium code, each test step is expressed in plain English (e.g., `click "Login"`), and the framework uses NLP and heuristic search to identify the correct element at runtime.

### Objectives

* **Lower maintenance costs** by eliminating explicit locators and reducing test flakiness after UI changes.
* **Assess robustness** of the script-free approach on evolving web applications and real-world test suites.
* **Provide a reproducible benchmark** (build scripts, Docker setup, and example branches) so others can compare against traditional locator-repair techniques.
* **Document best practices** and pitfalls discovered while adopting script-free testing in a standard Node/Playwright workflow.

---

## Getting Started

### 1 · Prerequisites

| Tool        | Recommended Version | Notes                                                                                       |
| ----------- | ------------------- | ------------------------------------------------------------------------------------------- |
| **Node.js** | 10.x                | `nvm use` will auto-select the right version.                                               |
| **Yarn**    | ≥ 1.22              | Install via `npm i -g yarn` or follow the [Yarn docs](https://yarnpkg.com/en/docs/install). |

### 2 · Script-Free Preparation

Follow the step-by-step setup in [`test/e2e/script-free-implementation/readme.md`](./test/e2e/script-free-implementation/readme.md) **before** continuing.

---

## Building Local Test Bundles

```bash
git checkout <branch-to-test>   # e.g. before_app_change_b7eae4b
yarn            # install dependencies
yarn build:test # outputs uncompressed files to /dist and compressed builds to /builds
```

---

## Running Script-Free End-to-End Tests

```bash
yarn test:e2e:scriptfree
```

---

## Example Branch Pairs for Locator-Change Experiments

| Before change               | After change                                  |
| --------------------------- | --------------------------------------------- |
| `after_app_change_before_locator_change_b7eae4b` | `after_app_change_and_locator_change_b7eae4b` |

---
## Running the experiment

- Checkout to the branch before test locator change e.g. `git checkout after_app_change_before_locator_change_b7eae4b`
- Expected results in the before locator change is that the normal e2e tests fail due to not located element
- Install dependencies and build the test project `yarn install` then `yarn build:test`
- To run normal e2e test execute `yarn test:e2e:chrome`
- Make sure the tests fail due to not located element
- Now, you can run the scriptfree tests with `yarn test:e2e:scriptfree`
- After Script generation, adjust the metamask runner in "test/e2e/script-free-implementation/test_script/metamask_exp/metamask_tests_runner.py 
  to run the newly generated selenium script.
- run the script with `./test/e2e/metamask-ui-run-generated-script`
- The script should work fine (tip: check screenshots)
- After ensuring correct run in the before change branch we run the scriptfree test in the after change branch
- Now `git checkout after_app_change_and_locator_change_b7eae4b`
- Expected results here are that both the normal and the script free tests succeed
- Install dependencies and build the test project `yarn install` then `yarn build:test`
- follow the same steps as before
---
## MetaMask Browser Extension

The original MetaMask extension source is available at
[https://github.com/MetaMask/metamask-extension](https://github.com/MetaMask/metamask-extension).

---

## Further Reading

* Kirinuki *et al.* “NLP-Assisted Web Element Identification Toward Script-Free Testing” — ICSME 2021.
* Kirinuki *et al.* “Web Element Identification by Combining NLP and Heuristic Search for Web Testing” — SANER 2022.
* Jasem “Assessing the Robustness of Script-Free GUI Testing in Evolving Web Applications” — Bachelor Thesis Proposal, Ruhr-Uni Bochum (2025).


