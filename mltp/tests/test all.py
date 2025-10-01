import syntax_test
import semantics_test
import functions_test
import proofs_test
import prover_test
import some_proofs_test
import deduction_test
import prenex_test
import completeness_test

def main():
    debug = True
    syntax_test.test_all(debug)
    semantics_test.test_all(debug)
    functions_test.test_all(debug)
    proofs_test.test_all(debug)
    prover_test.test_all(debug)
    some_proofs_test.test_all(debug)
    deduction_test.test_all(debug)
    prenex_test.test_all(debug)
    completeness_test.test_all(debug)
main()