Write-Output "Running Mypy"
mypy py_rpg
Write-Output ""
Write-Output "Running unit tests"
coverage run -m unittest discover py_rpg
coverage report -m
