SHELL = /bin/sh
IMAGE := ctfd/ctfd
DOCKER_NAME := ctfd-bootcamp
PORT = 8000

docker-run:
	docker run -p $(PORT):$(PORT) -it --name $(DOCKER_NAME) $(IMAGE)

docker-start:
	docker start $(DOCKER_NAME)

docker-stop:
	docker stop $(DOCKER_NAME)

docker-rm: docker-stop
	docker rm $(DOCKER_NAME)

docker-rmi:
	docker rmi $(IMAGE)

clean: docker-rm docker-rmi

.PHONY: clean install
