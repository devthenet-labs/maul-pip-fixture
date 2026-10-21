# maul-pip-fixture

Test fixture for maul's egress-proxy tunnel (step 3): a tiny Python package whose dependencies come from PyPI
(`pypi.org`, `files.pythonhosted.org`) through the `py` network profile's hostname-allowlisted CONNECT tunnel.

- `requirements.txt` pins the runtime dependencies, `requirements-dev.txt` the test ones.
- `.maul/Dockerfile` is the agent image (python:3.13-slim + git), built, pushed to ECR and KMS-signed by
  `.github/workflows/agent-image.yml`; `.maul/agent.yaml` declares it.
- `pytest` runs the tests (`.github/workflows/test.yml`).
