# $ chmod +x run_tests/b_test.sh
export MY_ENV_VAR="b"
poetry run pytest tests/ -rfE -m b
exit $?