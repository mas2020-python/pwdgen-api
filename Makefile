test:
	@cd src; PYTHON_TEST=./src pytest

run_local:
	@cd src; uvicorn main:app --host "0.0.0.0" --port 8080 --reload