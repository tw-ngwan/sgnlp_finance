# Test file to evaluate the performance of the Evaluator. NOT TO BE USED

from evaluate import Evaluator

evaluator = Evaluator()

print(evaluator.gather_results("Adani is falling", ["Adani"]))
