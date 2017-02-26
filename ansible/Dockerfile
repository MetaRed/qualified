FROM        alpine:3.4
MAINTAINER  Richard Lopez <metaredlabs@gmail.com>

ENV \
CGO_ENABLED=0 \
GOOS=linux \
CC=/usr/bin/gcc \
ALPINE_GO=1.6.3-r0 \
PROMETHEUS_VERSION=v1.4.1 \
GOPATH=/gopath \
PATH=$GOPATH/bin:/usr/local/go/bin:$PATH \
GOROOT=/usr/lib/go

RUN \
apk add --no-cache --virtual .build-deps \
    go=${ALPINE_GO} \
    git \
    make \
    gcc \
    musl-dev \
&& mkdir /build \
&& mkdir -p /gopath/src/github.com/prometheus \
&& cd /gopath/src/github.com/prometheus \
&& git clone https://github.com/prometheus/prometheus \
&& cd prometheus \
&& git checkout ${PROMETHEUS_VERSION} \
&& go build -a -tags netgo --ldflags \
'-s -linkmode external -extldflags "-static"' \
-o /build/prometheus ./cmd/prometheus/
