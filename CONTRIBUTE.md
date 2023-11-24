## 常用命令

brew install twine

python3 test_client.py

python3 -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*


## 发布命令

pip3 install setuptools wheel


rm -rf dist && python3 setup.py bdist_wheel

#twine upload --verbose dist/*
python3 -m twine upload --verbose dist/*