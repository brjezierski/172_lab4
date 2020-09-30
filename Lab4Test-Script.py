# Lab4Test-Script.py
# Created by Kelvin Ferreiras, modified by Vladimir Maksimovski, Dominick Harasimiuk, Akira
# Created on Nov. 16, 2017
# Last Modification on Sep. 30, 2020 by Bartlomiej Jezierski
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
input_file_name = 'Lab4Test'

# Take the name of all the .zip files into a list
submissions=glob.glob(dirPath + "/*.zip")
output_case_directory = '/output/'

out_file_extension = '.out'
ans_file_extension = '.ans'

#removes leftover files. FNULL serves to suppress output
FNULL = open(os.devnull, 'w')
subprocess.call('rm *.java', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
subprocess.call('rm *.class', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)

# Run the test case of the given number
def runTestCase(test_num, test_out, test_ans):
    subprocess.call('java ' + labname + ' ' + arraysize + ' input/' + input_file_name + test_num + '.txt ' + '>' + '\"' + test_out + '\"', shell=True)

    # Compare compressed and the decompressed output file with the original file
    compare_command = 'diff -w -B ' + '\"' + test_ans + '\"' + ' ' + '\"' + test_out + '\"'
    compare_command = shlex.split(compare_command)
    compare_result = subprocess.Popen(compare_command, stdout=subprocess.PIPE).communicate()[0].rstrip().decode(
        'ascii')

    # If both files are identical, test case passed
    if compare_result == '':
        return True
    return False

def testSubmission(submission, output_case_directory):
    subprocess.call(['unzip', '-o', ''+submission])

    # Extract student_id out of zip filename
    list_of_basename_elements = submission.split('_', 1)
    student_id = list_of_basename_elements[0]

    # Compile java files and run the test
    subprocess.call('javac *.java', shell = True)

    correctCases = 0
    totalCases = 0

    test_cases = glob.glob(dirPath + output_case_directory + '*.ans')
    test_cases.sort()

    error_dict = build_error_dict("error_msgs.txt")

    # Run tests on each ouput directory file
    for test_case in test_cases:

        test_num = str(int(test_case[-6:-4]))
        testHeader = test_case[:-4]

        out_file = testHeader + out_file_extension
        ans_file = testHeader + ans_file_extension

        print('\nCurrently testing Lab4, test case #' + test_num)

        if runTestCase(test_num, out_file, ans_file) is True:
            print("SUCCESS!")
            correctCases += 1
        else:
            print("WRONG! Error in: {}".format(error_dict[test_num]))

        totalCases += 1

    return student_id, correctCases, totalCases

# Build a dictionary of case numbers to error messages
def build_error_dict(filename):
    errors = {}
    with open(filename) as fh:
        for line in fh:
            number, description = line.strip().split('\t')
            errors[number] = description.strip()
    return errors

# Iterate on every .zip file
for currentZip in submissions:
    # Extract file name from path
    name_of_file = os.path.basename(currentZip)

    student_id, correct, total = testSubmission(name_of_file, output_case_directory)

    # Record grade in the TestResult text file
    gradebook = open('TestResult.txt', 'a')
    gradebook.write("NetId: " + student_id + "    Evaluation Result: " + str(correct) + '/' + str(total) + "\n")
    gradebook.flush()

    # removes leftover files again for good measures. FOR EVERY STUDENT. -Akira. FNULL serves to suppress output
    FNULL = open(os.devnull, 'w')
    subprocess.call('rm *.java', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
    subprocess.call('rm *.class', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
    subprocess.call('rm output/*.out', shell=True, stdout=FNULL, stderr=subprocess.STDOUT)