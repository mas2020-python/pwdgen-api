test:
	@cd src; pytest

run_local:
	@cd src; uvicorn main:app --host "0.0.0.0" --port 8080 --reload

run_docker:
	@docker pull mas2020/pwdgen-api:latest
	@docker run --rm -it --name pwdgen-api --publish 8080:8080 mas2020/pwdgen-api:latest