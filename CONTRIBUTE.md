## 常用命令

python3 test_client.py


## 发布命令

pip3 install setuptools wheel


rm -rf dist && python3 setup.py bdist_wheel


twine upload --verbose dist/*