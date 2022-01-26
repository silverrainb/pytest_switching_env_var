# $ chmod +x run_tests/a_test.sh
export MY_ENV_VAR="a"
poetry run pytest tests/ -rfE -m a
exit $?
