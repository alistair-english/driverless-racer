# Good reference: https://roboticseabass.com/2023/07/09/updated-guide-docker-and-ros2/

ARG ROS_DISTRO=humble

FROM osrf/ros:${ROS_DISTRO}-simulation as base

# setting the shell is important so we can source setup.bash files before building
SHELL ["/bin/bash", "-c"]

FROM base as dev

# Install extra tools for development
RUN apt update && apt install -y --no-install-recommends \
 gdb \
 gdbserver \
 nano \
 tmux \
 net-tools

# https://code.visualstudio.com/remote/advancedcontainers/add-nonroot-user#_creating-a-nonroot-user
ARG USERNAME=containuser
ARG USER_UID=1000
ARG USER_GID=${USER_UID}

RUN groupadd --gid ${USER_GID} ${USERNAME} \
 && useradd --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME} \
 && apt update \
 && apt install -y sudo \
 && echo ${USERNAME} ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/${USERNAME} \
 && chmod 0440 /etc/sudoers.d/${USERNAME}

# https://code.visualstudio.com/remote/advancedcontainers/persist-bash-history
RUN SNIPPET="export PROMPT_COMMAND='history -a' && export HISTFILE=/commandhistory/.bash_history" \
 && mkdir /commandhistory \
 && touch /commandhistory/.bash_history \
 && chown -R ${USERNAME} /commandhistory \
 && echo "$SNIPPET" >> "/home/${USERNAME}/.bashrc"

RUN mkdir -p /ws/src && chown -R ${USERNAME}:${USER_GID} /ws

ENV SHELL=/bin/bash
USER ${USERNAME}
WORKDIR /ws
