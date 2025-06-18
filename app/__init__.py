- name: Run tests
  run: pytest tests/
  env:
    PYTHONPATH: ${{ github.workspace }}
