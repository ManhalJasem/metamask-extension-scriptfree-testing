## Script-Free Testing

This project integrates the *script-free* GUI-testing technique introduced by Kirinuki *et al.* (ICSME 2021 & SANER 2022). Instead of brittle, locator-based Selenium code, each test step is expressed in plain English (e.g., `click "Login"`), and the framework uses NLP and heuristic search to identify the correct element at runtime.

### Objectives

- **Lower maintenance costs** by eliminating explicit locators and reducing test flakiness after UI changes.
- **Assess robustness** of the script-free approach on evolving web applications and real-world test suites.
- **Provide a reproducible benchmark** (build scripts, Docker setup, and example branches) so others can compare against traditional locator-repair techniques.
- **Document best practices** and pitfalls discovered while adopting script-free testing in a standard Node/Playwright workflow.

---

## Getting Started

### 1 · Prerequisites

| Tool        | Recommended Version | Notes                                                                                       |
| ----------- | ------------------- | ------------------------------------------------------------------------------------------- |
| **Node.js** | 10.x                | `nvm use` will auto-select the right version.                                               |
| **Yarn**    | ≥ 1.22              | Install via `npm i -g yarn` or follow the [Yarn docs](https://yarnpkg.com/en/docs/install). |

### 2 · Script-Free Preparation

Follow the step-by-step setup in [`test/e2e/script-free-implementation/readme.md`](./test/e2e/script-free-implementation/readme.md) **before** continuing.

---

## Building Local Test Bundles

```bash
git checkout <branch-to-test>   # e.g., before_app_change_b7eae4b
yarn                            # install dependencies
yarn build:test                 # outputs uncompressed files to /dist and compressed builds to /builds
```

---

## Running Script-Free End-to-End Tests

```bash
yarn test:e2e:scriptfree
```

---

## Example Branch Pairs for Locator-Change Experiments

| Before app change           | After app change, before locator change             | After app change and locator change                     |
| --------------------------- | --------------------------------------------------- | ------------------------------------------------------- |
| `before_app_change_b7eae4b` | `after_app_change_before_locator_change_b7eae4b`    | `after_app_change_and_locator_change_b7eae4b`           |

**Descriptions**

- **Before app change**  
  Snapshot of the application *before* the changes that cause locator failures in the E2E tests.  
  *Significance:* Run script-free tests here to assess baseline robustness.

- **After app change and before locator change**  
  Snapshot of the application *with* the app changes that trigger locator failures, but **without** locator fixes in the E2E tests.  
  *Significance:* Confirms that failures are due to locator changes.

- **After app change and locator change**  
  Snapshot of the application *with* the app changes **and** updated locators in the E2E tests.  
  *Significance:* Both the normal E2E tests and the script-free tests should pass.

---

## Running the Experiment

1. **Verify failures on the “after app change, before locator change” branch**
   ```bash
   git checkout after_app_change_before_locator_change_b7eae4b
   yarn install
   yarn install-chrome
   yarn build:test
   yarn test:e2e:chrome
   ```
   **Expected result:** Normal E2E tests fail due to elements not being located.

2. **Run script-free on the “before app change” branch**
   ```bash
   git checkout before_app_change_b7eae4b
   yarn install
   yarn build:test
   yarn test:e2e:scriptfree
   ```
   After script generation, adjust the MetaMask runner at  
   `test/e2e/script-free-implementation/test_script/metamask_exp/metamaskui_tests_runner.py` and 
   `test/e2e/script-free-implementation/test_script/metamask_exp/from_import_ui_tests_runner.py`
   to execute the newly generated Selenium script.

   Then run:
   ```bash
   ./test/e2e/metamask-ui-run-generated-script.sh
   ./test/e2e/from-import-ui-run-generated-script.sh
   ```
   **Expected result:** The script runs successfully. *(Tip: check screenshots.)*

3. **Confirm success on the “after app change and locator change” branch**
   ```bash
   git checkout after_app_change_and_locator_change_b7eae4b
   yarn install
   yarn build:test
   # Repeat the same execution steps as above
   ```
   **Expected result:** Both normal E2E tests and script-free tests succeed.

---

## MetaMask Browser Extension

The original MetaMask extension source is available at  
[https://github.com/MetaMask/metamask-extension](https://github.com/MetaMask/metamask-extension).

---

## Further Reading

- Kirinuki *et al.* “NLP-Assisted Web Element Identification Toward Script-Free Testing” — ICSME 2021.  
- Kirinuki *et al.* “Web Element Identification by Combining NLP and Heuristic Search for Web Testing” — SANER 2022.  
- Jasem, “Assessing the Robustness of Script-Free GUI Testing in Evolving Web Applications” — Bachelor Thesis Proposal, Ruhr-Uni Bochum (2025).
