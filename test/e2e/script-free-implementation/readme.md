Artifacts for "Web Element Identification by Combining NLP and Heuristic Search for Web Testing" presented in SANER2022.

# Preparation

- Install chromedriver as `/usr/local/bin/chromedriver`
- Download fastText model with subword from [here](https://fasttext.cc/docs/en/english-vectors.html) or [here](https://github.com/facebookresearch/fastText/issues/656) or [here](https://github.com/facebookresearch/fastText/issues/656).
- Put the model as `./data/fasttext.bin`
- Put test case in `./test_cases_metamask_experiment`
- Specify target test cases via `./src/Setting.py`

These directory names can be changed via `./src/Setting.py`

# Build

`pipenv install`

# Run

`pipenv run gen`
