FROM mcr.microsoft.com/vscode/devcontainers/base:0-ubuntu-22.04

ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# hadolint ignore=DL3008
RUN apt-get update \
  && export DEBIAN_FRONTEND=noninteractive \
  && apt-get -y install \
  --no-install-recommends \
  verilator \
  iverilog \
  python3 \
  pip \
  python-is-python3 \
  python3-dev \
  # Clean up
  && apt-get autoremove -y \
  && apt-get clean -y \
  && rm -rf /var/lib/apt/lists/*

# hadolint ignore=DL3013
RUN pip install \
  --no-cache-dir \
  cocotb \
  pytest

# [Optional] Update UID/GID if needed
RUN if [ "$USER_GID" != "1000" ] || [ "$USER_UID" != "1000" ]; then \
    groupmod --gid $USER_GID $USERNAME \
    && usermod --uid $USER_UID --gid $USER_GID $USERNAME \
    && chown -R $USER_UID:$USER_GID /home/$USERNAME; \
  fi

USER vscode
