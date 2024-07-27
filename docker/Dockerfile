# Good reference: https://roboticseabass.com/2023/07/09/updated-guide-docker-and-ros2/

ARG ROS_DISTRO

FROM osrf/ros:${ROS_DISTRO}-desktop AS base

# setting the shell is important so we can source setup.bash files before building
SHELL ["/bin/bash", "-c"]


# ======================================================================================================================
FROM alpine AS package_xml_only
COPY ./ /src/
RUN find /src ! -name "package.xml" -type f -delete


# ======================================================================================================================
FROM base AS src_dependencies

RUN apt update -y \
  && apt install -y --no-install-recommends \
  ros-${ROS_DISTRO}-simulation

RUN mkdir -p /ws/src

RUN apt update -y \
 && apt install -y python3-pip -y \
 && pip install transforms3d

# grab dependencies to make sure we install any of their requirements
COPY ./src/dependencies.repos /
RUN vcs import /ws/src < /dependencies.repos --recursive && rm /dependencies.repos

COPY --from=package_xml_only /src/ /ws/src/tmp

RUN apt update -y \
 && rosdep install --from-paths /ws/src --ignore-src --rosdistro ${ROS_DISTRO} -y \
 && rm -rf /ws/src/tmp


# ======================================================================================================================
FROM src_dependencies AS dev

# install extra tools for development
RUN apt update && apt install -y --no-install-recommends \
 gdb \
 gdbserver \
 nano \
 tmux \
 htop \
 net-tools \
 mesa-utils

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

# set up the entrypoint
COPY ./docker/entrypoint.sh /
RUN chmod 777 /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]

# source ROS environment
RUN echo "source /opt/ros/${ROS_DISTRO}/setup.bash" >> "/home/${USERNAME}/.bashrc"

# source workspace if it exists and not in a login shell
# - this is because we don't want the workspace always loaded in. VSCode starts a login shell which spawns all other
#   terminals it creates. These terminals inherit from the login shell
# - https://code.visualstudio.com/docs/terminal/advanced#_environment-inheritance
# shopt -q login_shell checks if the shell is login (https://unix.stackexchange.com/a/26782)
RUN echo "if ! shopt -q login_shell; then [ -f /ws/install/setup.bash ] && source /ws/install/setup.bash; fi" >> "/home/${USERNAME}/.bashrc"

# chown workspace
RUN chown -R ${USERNAME}:${USER_GID} /ws

ENV SHELL=/bin/bash
USER ${USERNAME}
WORKDIR /ws
