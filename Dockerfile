FROM ubuntu:latest

WORKDIR /CI-CD

# Intalling application dependencies
RUN apt-get update && apt-get install -y \
build-essential \
cmake \
python3 \
golang-go \
g++ \
curl \
shellcheck \
clang-tidy \
clang-tools \
pylint \
pycodestyle \
&& rm -rf /var/lib/apt/lists/*

# Install golangci-lint (latest version)
RUN curl -sSfL https://raw.githubusercontent.com/golangci/golangci-lint/HEAD/install.sh | sh -s -- -b /usr/local/bin latest

# Copy source code
COPY src ./src


CMD ["bash"]