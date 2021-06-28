DOCKER_FILE := Dockerfile
IMAGE_VERSION := 0.1

WEB_SINGLE_PATTERN := web_single_pattern

.PHONY: build
build:
	docker build \
		-t $(WEB_SINGLE_PATTERN)_$(IMAGE_VERSION) \
		-f $(DOCKER_FILE) \
		.

.PHONY: run
run:
	docker run \
		-d \
		--name $(WEB_SINGLE_PATTERN)

.PHONY: stop
stop:
	docker rm -f $(WEB_SINGLE_PATTERN)
