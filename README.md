tradeoff is the output is going to look a little be non-standard

* Configure pyproject.toml:

```toml
[tool.pytest.ini_options]
addopts = "-rA -q"
markers = [
    "a",
    "b",
]
minversion = "6.2"
testpaths = [
    "run_tests"
]
```

* Set testpaths: testpaths must include shell script(s) and a test script.
* Set markers
* One trade off: pytest options ("-rA -q") with subprocess.run(shell=True, stdout=sys.stdout, stderr=sys.stderr) will produce most familiar format of test output.