SHELL = /bin/sh
IMAGE := ctfd/ctfd
DOCKER_NAME := ctfd-bootcamp
CTFD_PATH := CTFd

docker-run:
	cd $(CTFD_PATH)
	docker run -p 8000:8000 -it --name $(DOCKER_NAME) $(IMAGE)

docker-start:
	docker start $(DOCKER_NAME)

docker-stop:
	docker stop $(DOCKER_NAME)

docker-rm: docker-stop
	docker rm $(DOCKER_NAME)

docker-rmi:
	docker rmi $(IMAGE)

.PHONY: clean
clean: docker-rm docker-rmi

.PHONY: install
