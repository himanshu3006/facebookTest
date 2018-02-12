#  Copyright 2017-2018 WiZR
#
#  Licensed under the  License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


from robot import run_cli
from robot import run
from robot.libraries import BuiltIn
import os
####################

# Runner Meat Data

####################

#This test configuration parameters and Test execution enviornment
#

from robot import run
import datetime

now = str(datetime.datetime.now())
test_run_folder="Robot_Logs"+datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

complete_dir_path = os.path.join(os.getcwd(), "logs" + os.sep + test_run_folder)
os.environ["RESULTS_PATH"]="%s"%test_run_folder
if not os.path.isdir(complete_dir_path):
    os.mkdir(complete_dir_path)
else:
    pass
#Export the result directory for the test suite
os.environ["RESULTS_PATH"]=test_run_folder
#Form complete path to store html rport
complete_report_path= os.path.join(complete_dir_path,"Functional_"+datetime.datetime.now().strftime("%Y%m%d-%H%M%S")+".html")
#Form complete path to store log report
complete_log_path=os.path.join(complete_dir_path,"Functional_log"+datetime.datetime.now().strftime("%Y%m%d-%H%M%S")+".html")

#start the suite
run(
    "resource/login.robot",

    report=complete_report_path,log=complete_log_path)


####################

# TBD

####################

