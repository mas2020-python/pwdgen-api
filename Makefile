test:
	@cd src; PYTHON_TEST=./src pytest

run_local:
	@uvicorn src.main:app --host "0.0.0.0" --port 8080 --reload