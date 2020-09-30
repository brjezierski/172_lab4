# Lab2Test-Script.py
# Created by Kelvin Ferreiras, modified by Vladimir Maksimovski, Dominick Harasimiuk
# Created on Nov. 16, 2017
# Last Modification on Feb. 16, 2019 by Akira
# This program tests Lab4 for CSC-172

import subprocess
import glob
import os
import shlex

currentFile = 'Lab4Test-Script'#Name of script file
realPath = os.path.realpath(currentFile)
dirPath = os.path.dirname(realPath)

labname = 'DNAList' # lab4 only has one main file
arraysize = '20'
labTests = ['Lab4Test1','Lab4Test2','Lab4Test3','Lab4Test4','Lab4Test5','Lab4Test6','Lab4Test7','Lab4Test8','Lab4Test9'
,'Lab4Test10','Lab4Test11','Lab4Test12','Lab4Test13','Lab4Test14','Lab4Test15','Lab4Test16','Lab4Test17']#names of tests (subdirectories of tests folder and names of command text files)

# Take the name of all the .zip files into a list
submissions=glob.glob(dirPath + "/*.zip")
test_case_directory = '/tests/'

out_file_extension = '.out'
ans_file_extension = '.ans'

#removes leftover files. FNULL serves to suppress output
FNULL = open(os.devnull, 'w')
subprocess.call('rm *.java', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
subprocess.call('rm *.class', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
subprocess.call('rm tests/Lab4Test1/*.out', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
subprocess.call('rm tests/Lab4Test2/*.out', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
subprocess.call('rm tests/Lab4Test3/*.out', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)

#src argument deleted for lab 4 cuz it only has one main file
def runTestCase(test, test_out, test_ans):
    subprocess.call('java ' + labname + ' ' + arraysize + ' ' + test + '.txt ' + '>' + '\"' + test_out + '\"', shell=True)

    # Compare compressed and the decompressed output file with the original file
    compare_command = 'diff -w -B ' + '\"' + test_ans + '\"' + ' ' + '\"' + test_out + '\"'
    compare_command = shlex.split(compare_command)
    compare_result = subprocess.Popen(compare_command, stdout=subprocess.PIPE).communicate()[0].rstrip().decode(
        'ascii')

    # If both files are identical, test case passed
    if compare_result == '':
        return True
    return False


def testSubmission(submission, labTests, test_case_directory):
    subprocess.call(['unzip', '-o', ''+submission])

    # Extract student_id out of zip filename
    list_of_basename_elements = submission.split('_', 1)
    student_id = list_of_basename_elements[0]

    # Compile java files and run the test
    subprocess.call('javac *.java', shell = True)

    correctCases = 0
    totalCases = 0

    #running tests on each test directory
    for test in labTests:
        
        test_cases = glob.glob(dirPath + test_case_directory + test + '/*.ans')

        #accounting for multiple .in files?
        #dunno if we need this but okay
        for testCasePath in test_cases:
            testName = testCasePath[-6:-4]
            testHeader = testCasePath[:-4]

            out_file = testHeader + out_file_extension
            ans_file = testHeader + ans_file_extension

            print('Currently testing ' + test + ', test case #' + testName)
            #lab 4 has just one main java file and multiple text files to test.
            if runTestCase(test, out_file, ans_file) is True:
                print("SUCCESS!")
                correctCases += 1
            else:
                print("WRONG")

            totalCases += 1

    return student_id, correctCases, totalCases


# Iterate on every .zip file
for currentZip in submissions:
    # Extract file name from path
    name_of_file = os.path.basename(currentZip)

    student_id, correct, total = testSubmission(name_of_file, labTests, test_case_directory)

    # Record grade in the TestResult text file
    gradebook = open('TestResult.txt', 'a')
    gradebook.write("NetId: " + student_id + "    Evaluation Result: " + str(correct) + '/' + str(total) + "\n")
    gradebook.flush()

    # removes leftover files again for good measures. FOR EVERY STUDENT. -Akira. FNULL serves to suppress output
    FNULL = open(os.devnull, 'w')
    subprocess.call('rm *.java', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
    subprocess.call('rm *.class', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
    subprocess.call('rm tests/Lab4Test1/*.out', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
    subprocess.call('rm tests/Lab4Test2/*.out', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
    subprocess.call('rm tests/Lab4Test3/*.out', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
    subprocess.call('rm tests/Lab4Test4/*.out', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
    subprocess.call('rm tests/Lab4Test5/*.out', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
    subprocess.call('rm tests/Lab4Test6/*.out', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
    subprocess.call('rm tests/Lab4Test7/*.out', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
    subprocess.call('rm tests/Lab4Test8/*.out', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
    subprocess.call('rm tests/Lab4Test9/*.out', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
    subprocess.call('rm tests/Lab4Test10/*.out', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
    subprocess.call('rm tests/Lab4Test11/*.out', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
    subprocess.call('rm tests/Lab4Test12/*.out', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
    subprocess.call('rm tests/Lab4Test13/*.out', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
    subprocess.call('rm tests/Lab4Test14/*.out', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
    subprocess.call('rm tests/Lab4Test15/*.out', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
    subprocess.call('rm tests/Lab4Test16/*.out', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
    subprocess.call('rm tests/Lab4Test17/*.out', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
