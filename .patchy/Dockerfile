# patchy agent image for patchy-pip-fixture: python:3.13-slim (Debian, glibc)
# plus git, the agent image contract (bash, sh, git; uid 65532, home
# /workspace), and the project's dependencies baked into the system
# site-packages. Unlike patchy's offline Python example, pip is NOT told to
# stay offline (no PIP_NO_INDEX): the operator's `py` network profile gives
# build Jobs a CONNECT tunnel to pypi.org and files.pythonhosted.org, so the
# agent can `pip install -r requirements.txt` after adding a dependency. The
# system site-packages is read-only in the pod, so pip installs into the user
# site (PYTHONUSERBASE, under /tmp).
#
# Built, pushed and KMS-signed by .github/workflows/agent-image.yml; to build by
# hand, use the repository root as the context:
#
#   docker build --platform linux/amd64 -f .patchy/Dockerfile -t patchy-pip-fixture-agent .
FROM python:3.13-slim@sha256:70729b46c69b4f1e97c4822c1af3df53a1476cf5ddc6c087c0c10bc3a5678c2f

# hadolint ignore=DL3008
RUN apt-get update \
  && apt-get install -y --no-install-recommends git ca-certificates \
  && rm -rf /var/lib/apt/lists/* \
  && groupadd -g 65532 patchy \
  && useradd -u 65532 -g 65532 -d /workspace -M -s /bin/bash patchy

WORKDIR /tmp/deps
COPY requirements.txt requirements-dev.txt ./
RUN pip install --no-cache-dir --root-user-action=ignore -r requirements.txt -r requirements-dev.txt \
  && rm -rf /tmp/deps

# Caches and the user site under /tmp (writable in the pod, outside the
# repository, so nothing reaches the changeset). No bytecode next to sources.
ENV XDG_CACHE_HOME=/tmp/.cache \
    TMPDIR=/tmp \
    LANG=C.UTF-8 \
    PYTHONUSERBASE=/tmp/.local \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

LABEL org.opencontainers.image.source="https://github.com/devthenet-labs/patchy-pip-fixture" \
      org.opencontainers.image.title="patchy-pip-fixture agent image" \
      org.opencontainers.image.description="patchy agent image for patchy-pip-fixture: Python 3.13 (slim) with git and the project's dependencies"

WORKDIR /workspace
USER 65532:65532
