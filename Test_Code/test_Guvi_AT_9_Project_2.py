from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test_Data import Data
from selenium.webdriver.chrome.options import Options


class Test_guvi_AT_9_project_2:
    url = "https://opensource-demo.orangehrmlive.com/"
    option = Options()
    option.headless = False
    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")
    option.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1})
    driver = webdriver.Chrome(chrome_options= option, executable_path = "D:\\Guvi\\webdriver\\chromedriver.exe")
    actions= ActionChains(driver)

    @pytest.fixture(autouse=True, scope="session")
    def setup(self):
        self.driver.get(self.url)
        time.sleep(5)
        self.driver.maximize_window()
        print("SUCESS # user is navigated to OrangeHRM login page")
        time.sleep(5)
        self.driver.maximize_window()
        if self.driver.title == "OrangeHRM":
            print("SUCESS # user is navigated to OrangeHRM login page")
        else:
            print("Failure # user is not navigated to OrangeHRM login page")
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=Data.Selectors.login_username).send_keys(Data.Data.Admin_Username)
        self.driver.find_element(by=By.XPATH, value=Data.Selectors.login_password).send_keys(Data.Data.Admin_Password)
        self.driver.find_element(by=By.XPATH, value=Data.Selectors.loginPage_loginButton).click()
        try:
            time.sleep(2)
            print(self.driver.switch_to.alert.text)
            self.driver.switch_to.alert.accept()
        except:
            print("No Alert")
        if self.driver.current_url == Data.Data.dashboard_url:
            print("SUCESS # current Url matches with the dashboard url ")
        else:
            print("Current URL is not matching the dashboard")
        if self.driver.find_element(by=By.XPATH, value=Data.Selectors.dashbord_header).text == "Dashboard":
            print("SUCESS #user navigated to the Dashboard")
        else:
            print("user is not navigated to the Dashboard")
        yield
        self.driver.close()


    def test_TC_PIM_01_1(self):
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=Data.Selectors.leftnave_admin).click()
        time.sleep(3)
        assert self.driver.find_element(by=By.XPATH, value=Data.Selectors.admin_header).text == "Admin"
        print("SUCESS # user is in Admin page")

    def test_TC_PIM_01_2(self):
        # veriy the user is able to selct user_management
        self.driver.find_element(by=By.XPATH, value=Data.Selectors.Admin_page_Usermanagement_tab).click()
        time.sleep(5)
        ActionChains(self.driver).move_to_element(self.driver.find_element(by=By.XPATH, value=Data.Selectors.Admin_page_Usermanagement_tab_user_DD)).click().perform()
        time.sleep(3)
        assert self.driver.find_element(by=By.XPATH, value=Data.Selectors.admin_page_subheading).text == "User Management"
        print("SUCESS # user is naviagated to user management")

    def test_TC_PIM_01_3(self):
        #verifying_leftnave has all the elements
        list_of_leftnave_element = self.driver.find_elements(by=By.XPATH, value=Data.Selectors.leftname_listofElement)
        result = True
        if len(list_of_leftnave_element) == 11:
            for i in range (0,11):
                if list_of_leftnave_element[i].text == Data.Data.Element_of_leftnave[i]:
                    print("SUCESS # the {element} is present in the leftnave".format(element=Data.Data.Element_of_leftnave[i]))
                else:
                    result = False
                    print("Failure # the {element} is not present in the leftnave".format(element=Data.Data.Element_of_leftnave[i]))
        assert result


    def test_TC_PIM_01_4(self):
        rilling = True
        list_of_leftnave_element = self.driver.find_elements(by=By.XPATH, value=Data.Selectors.leftname_listofElement)
        for i in range (0,11):
            if list_of_leftnave_element[i].is_displayed():
                print("SUCESS # the {element} is displayed in the leftnave".format(element=Data.Data.Element_of_leftnave[i]))
            else:
                rilling = False
                print("Failure # the {element} is not displayed in the leftnave".format(element=Data.Data.Element_of_leftnave[i]))
        assert rilling

    def test_TC_PIM_01_5(self):
        #check is search box is displayed
        assert self.driver.find_element(by=By.XPATH, value=Data.Selectors.Admin_page_leftnave_search_field).is_displayed()
        print("SUCESS # user is able to see search box in left nave in Admin page")

    def test_TC_PIM_01_6(self):
        #check if search bar shows the result when searching with the elements in Upper case
        result = True
        for i in range(0,11):
            capslock_element = Data.Data.Element_of_leftnave[i].upper()
            self.driver.find_element(by=By.XPATH, value=Data.Selectors.Admin_page_leftnave_search_field).send_keys(capslock_element)
            time.sleep(2)
            if (self.driver.find_element(by=By.XPATH, value=Data.Selectors.Admin_page_leftnave_search_result).text.upper() == capslock_element):
                #print("SUCESS #{element} is displayed in leftnave when searched ".format(element=Data.Data.Element_of_leftnave[i]))
                time.sleep(2)
                self.driver.find_element(by=By.XPATH, value=Data.Selectors.Admin_page_leftnave_search_field).send_keys(Keys.CONTROL+'a')
                self.driver.find_element(by=By.XPATH, value=Data.Selectors.Admin_page_leftnave_search_field).send_keys(Keys.DELETE)
                time.sleep(2)
            else:
                result = False
                print("SUCESS #{element} is displayed in leftnave when searched (uppercase)".format(element=Data.Data.Element_of_leftnave[i]))
        assert result
        print("SUCESS # Step 6 is complete ")

    def test_TC_PIM_01_7(self):
        #check if search bar shows the result when searching with the elements in lower case
        result = True
        for i in range(0,11):
            lowercase_element = Data.Data.Element_of_leftnave[i].lower()
            self.driver.find_element(by=By.XPATH, value=Data.Selectors.Admin_page_leftnave_search_field).send_keys(lowercase_element)
            time.sleep(2)
            if (self.driver.find_element(by=By.XPATH, value=Data.Selectors.Admin_page_leftnave_search_result).text.lower() == lowercase_element):
                #print("SUCESS #{element} is displayed in leftnave when searched ".format(element=Data.Data.Element_of_leftnave[i]))
                time.sleep(2)
                self.driver.find_element(by=By.XPATH, value=Data.Selectors.Admin_page_leftnave_search_field).send_keys(Keys.CONTROL+'a')
                self.driver.find_element(by=By.XPATH, value=Data.Selectors.Admin_page_leftnave_search_field).send_keys(Keys.DELETE)
                time.sleep(2)
            else:
                result = False
                print("Failure #{element} is not displayed in leftnave when searched(lower case)".format(element=Data.Data.Element_of_leftnave[i]))
        assert result
        print("SUCESS # step 7 is passed ")


    def test_TC_PIM_02_1(self):
        print("User Role enabled:", self.driver.find_element(by=By.XPATH, value=Data.Selectors.UserManagement_UserRole_DD).is_enabled())
        print("User Role displayed",self.driver.find_element(by=By.XPATH, value=Data.Selectors.UserManagement_UserRole_DD).is_displayed())
        assert (self.driver.find_element(by=By.XPATH, value=Data.Selectors.UserManagement_UserRole_DD).is_displayed() and self.driver.find_element(by=By.XPATH, value=Data.Selectors.UserManagement_UserRole_DD).is_enabled())
        print("SUCESS #UserRole drop_done is displayed and enabled")

    def test_TC_PIM_02_2(self):
        assert (self.driver.find_element(by=By.XPATH, value=Data.Selectors.UserManagement_Status_DD).is_displayed() and self.driver.find_element(by=By.XPATH, value=Data.Selectors.UserManagement_Status_DD).is_enabled())
        print("SUCESS #Status drop_done is displayed and enabled")

    def test_TC_PIM_02_3(self):
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.UserManagement_UserRole_DD).click()
        time.sleep(2)
        self.actions.move_to_element(self.driver.find_element(by=By.XPATH, value=Data.Selectors.UserManagement_UserRole_DD_)).perform()
        time.sleep(2)
        local_list = self.driver.find_elements(by=By.XPATH,value=Data.Selectors.UserManagement_UserRole_DD_list)
        len_local_list= len(local_list)
        result = True
        if len_local_list == 3:
            for i in range(0,len_local_list):
                if local_list[i].text== Data.Data.user_role_list[i]:
                    if local_list[i].is_displayed() and local_list[i].is_enabled():
                        continue
                    else:
                        result = False
                        print("{element} is not displayed/enabled in userrole ".format(element=local_list[i].text))
                else:
                    result = False
                    print("{element} is not in user role".format(element=local_list[i].text))
        else:
            result=False
            print("the length of the userrole list is {listlength}".format(listlength=len_local_list))
        assert result
        print("SUCESS #all three options are displayed in userrole dropdown ")
        time.sleep(2)
        self.actions.move_to_element(local_list[2]).click().perform()

    def test_TC_PIM_02_4(self):
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.UserManagement_Status_DD).click()
        time.sleep(2)
        self.actions.move_to_element(self.driver.find_element(by=By.XPATH, value=Data.Selectors.UserManagement_Status_DD_)).perform()
        time.sleep(2)
        local_list=self.driver.find_elements(by=By.XPATH, value=Data.Selectors.UserManagement_Status_DD_list)
        len_local_list=len(local_list)
        results = True
        if len_local_list == 3:
            for i in range(0,len_local_list):
                #print(local_list[i].text)
                if local_list[i].text == Data.Data.status_list[i]:
                    if local_list[i].is_displayed() and local_list[i].is_enabled():
                        continue
                    else:
                        results = False
                        print("{element} is not displayed/enabled in status ".format(element=local_list[i].text))
                else:
                    results = False
                    print("{element} is not in Status ".format(element=local_list[i].text))
        else:
            results = False
            print("the length of the status list is {listlength}".format(listlength=len_local_list))
        assert results
        print("SUCESS #all three options are displayed in status dropdown")
        self.actions.move_to_element(local_list[1]).click().perform()

    def test_TC_PIM_03_1(self):
        self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_in_leftnave).click()
        time.sleep(3)
        local_listof_ElementInLeftNave=self.driver.find_elements(by=By.XPATH, value=Data.Selectors.PIM_leftnave_list)
        len_local_listof_ElementInLeftNave=len(local_listof_ElementInLeftNave)
        result = True
        result2 = True
        if len_local_listof_ElementInLeftNave == 11:
            for i in range(0,len_local_listof_ElementInLeftNave):
                if(local_listof_ElementInLeftNave[i].text==Data.Data.Element_of_leftnave[i]):
                    continue
                else:
                    result = False
                    print("{element} is not displayed in the".format(element=local_listof_ElementInLeftNave[i]))
        else:
            result = False
            print("the length of the Element in the left nave is {lenth} ".format(lenth=len_local_listof_ElementInLeftNave))
        if (self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Top_Headder).text) == "PIM":
            pass
        else:
            result2 = False
            print("the heading of the page is not PIM")
        assert result and result2
        print("test_TC_PIM_03_1 is completed")

    def test_TC_PIM_03_2(self):
        self.resulting_test_TC_PIM_03_2 = False
        self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_ADD_Button).click()
        time.sleep(5)
        if (self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_AddEmployee).text == "Add Employee"):
            self.resulting_test_TC_PIM_03_2 = True
            time.sleep(2)
            self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_CreateLoginDetail_toggleButton).click()
            time.sleep(5)
            if self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_CreateLoginDetail_toggleButton).is_enabled():
                self.resulting_test_TC_PIM_03_2 = True
                time.sleep(2)
                self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_FirstName).send_keys(Data.Data.First_name)
                time.sleep(2)
                self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_MiddleName).send_keys(Data.Data.Middle_name)
                time.sleep(2)
                self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_LastName).send_keys(Data.Data.Last_name)
                time.sleep(2)
                self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_UserName).send_keys(Data.Data.Pim_UserName)
                time.sleep(2)
                self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Password).send_keys(Data.Data.Pim_password)
                time.sleep(2)
                self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_ConfirmPassword).send_keys(Data.Data.Pim_password)
                time.sleep(2)
                Enabled_status=self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Status_Enabled).is_selected()
                Diable_status=self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Status_Disabled).is_selected()

                print("Enabled_Status: ", Enabled_status)
                print("Disable_Status: ", Diable_status)
                if Enabled_status == True and Diable_status == False:
                    try:
                        emp_exist_error_elm = self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_EmpId_Exist_error)
                        if emp_exist_error_elm.is_displayed():
                            emp_id = int(
                                self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Emp_ID).get_attribute('value'))
                            emp_id = emp_id + 2
                            self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Emp_ID).send_keys(
                                Keys.CONTROL + 'a')
                            self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Emp_ID).send_keys(
                                Keys.DELETE)
                            self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Emp_ID).send_keys(emp_id)
                            self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Save_Button).click()
                            time.sleep(5)
                    except:
                        pass
                elif Enabled_status == False:
                    self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Status_Enabled).click()
                    time.sleep(1)
                    try:
                        emp_exist_error_elm = self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_EmpId_Exist_error)
                        if emp_exist_error_elm.is_displayed():
                            emp_id = int(self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Emp_ID).get_attribute('value'))
                            emp_id = emp_id + 2
                            self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Emp_ID).send_keys(
                                Keys.CONTROL + 'a')
                            self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Emp_ID).send_keys(
                                Keys.DELETE)
                            self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Emp_ID).send_keys(emp_id)
                            self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Save_Button).click()
                            time.sleep(5)
                    except:
                        pass
                else:
                    print("status of enabled button: ", Enabled_status)
                    print("status of Disabled button:", Diable_status)
                self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Save_Button).click()
                time.sleep(5)
                Employee_List_result=False
                Personal_Details_result=False
                time.sleep(5)
                if self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Employee_List_Tab).text == "Employee List":
                    Employee_List_result = True
                if self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Personal_Deatails).text == "Personal Details":
                    Personal_Details_result = True
                if Employee_List_result==True and Personal_Details_result==True:
                    self.resulting_test_TC_PIM_03_2 = True
                else:
                    self.resulting_test_TC_PIM_03_2 = False
                    print("personal Details status: ",Personal_Details_result)
                    print("Employee_list_result:",Employee_List_result)
            else:
                self.resulting_test_TC_PIM_03_2 = False
                print("PIM_CreateLoginDetail_toggleButton is not selected ")
        else:
            self.resulting_test_TC_PIM_03_2 = False
            print("user is not navigated to Add_Employee page ")
        assert self.resulting_test_TC_PIM_03_2
        print("test_TC_PIM_03_2 is completed ")
        
    def test_TC_PIM_4_1(self):
        time.sleep(2)
        self.result_test_TC_PIM_4_1 = True
        list_of_elements_in_subnave = self.driver.find_elements(by=By.XPATH, value=Data.Selectors.PIM_EmployeeListTab_SubNave)
        len_of_element_in_suubnave = len(list_of_elements_in_subnave)
        if len_of_element_in_suubnave == 11:
            self.result_test_TC_PIM_4_1 = True
            for i in range(0,11):
                if Data.Data.PIM_SubNave.count(list_of_elements_in_subnave[i].text):
                    self.result_test_TC_PIM_4_1 = True
                    if list_of_elements_in_subnave[i].text == Data.Data.PIM_SubNave[i]:
                        self.result_test_TC_PIM_4_1 = True
                        if list_of_elements_in_subnave[i].is_displayed():
                            self.result_test_TC_PIM_4_1 = True
                        else:
                            self.result_test_TC_PIM_4_1 = False
                            print("{elm} is not displayed in the webpage".format(elm=list_of_elements_in_subnave[i]))
                    else:
                        self.result_test_TC_PIM_4_1 = False
                        print("{element} is not present in the index{index}".format(element=list_of_elements_in_subnave[i], index=i))
                else:
                    self.result_test_TC_PIM_4_1 = False
                    print("{Element} is  not present in PIM Subnave list".format(Element=list_of_elements_in_subnave[i].text))

        else:
            print("the lenth of the list_of_elements_in_subnave is :",len_of_element_in_suubnave)
            self.result_test_TC_PIM_4_1 = False

        assert self.result_test_TC_PIM_4_1
        print("SUCESS # test_TC_PIM_4_1 completed")

    def test_TC_PIM_05_01(self):
        self.test_TC_PIM_05_01_result=True
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Personal_Deatails_subnave).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_PersDetail_NickName).send_keys(Data.Data.PIM_Nickname)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_PersDetail_OtherID).send_keys(Data.Data.PIM_otherid)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_PersDetail_DrivingLic).send_keys(Data.Data.PIM_DL)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_PersDetail_licenceEXP).send_keys(Data.Data.PIM_DL_EXP)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_PersDetail_SSN).send_keys(Data.Data.PIM_SSN)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Nationality).click()
        time.sleep(2)
        self.actions.move_to_element(self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Nationality_list)).perform()
        print(Data.Selectors.PIM_Nationality_list)
        time.sleep(2)
        print(Data.Selectors.PIM_Nationality_IND)
        #self.actions.scroll_to_element(self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Nationality_IND)).click().perform()
        #time.sleep(2)
        list_of_nations=self.driver.find_elements(by=By.XPATH,value=Data.Selectors.PIM_Nationality_IND)
        for i in list_of_nations:
            time.sleep(1)
            self.actions.scroll_to_element(i).perform()
            if i.text.lower() == Data.Data.PIM_Nationality.lower():
                time.sleep(5)
                self.actions.move_to_element(i).click().perform()
                break
        time.sleep(2)
        self.actions.move_to_element(self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Marital_Status)).perform()
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Marital_Status).click()
        time.sleep(3)
        self.actions.move_to_element(self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Marital_Status_list)).perform()
        time.sleep(2)
        print(Data.Selectors.PIM_Marital_status_Single)
        #self.actions.move_to_element(self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Marital_status_Single)).click().perform()
        #time.sleep(2)
        list_maritalstatus = self.driver.find_elements(by=By.XPATH, value=Data.Selectors.PIM_Marital_status_Single)
        time.sleep(3)
        print(len(list_maritalstatus))
        for i in range(0,len(list_maritalstatus)):
            time.sleep(1)
            self.actions.scroll_to_element(list_maritalstatus[i]).perform()
            if list_maritalstatus[i].text.lower() == Data.Data.PIM_Marital_Status.lower():
                time.sleep(2)
                self.actions.move_to_element(list_maritalstatus[i]).perform()
                self.actions.click().perform()
                break
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_DOB).send_keys(Data.Data.PIM_DOB)
        time.sleep(2)
        if Data.Data.PIM_gender == "Male":
            self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Gender_Male).click()
        elif Data.Data.PIM_gender == "Female":
            self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Gender_Female).click()
        time.sleep(2)
        if len(Data.Data.PIM_Military_Serv) > 0:
            self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_MilitaryServices).send_keys(Data.Data.PIM_Military_Serv)
        time.sleep(2)
        if Data.Data.PIM_Smoker_ == "Yes":
            self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Smoker_checkbox).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_PD_Blood_Grp).click()
        time.sleep(2)
        self.actions.move_to_element(self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_PD_Blood_Grp_lst)).perform()
        time.sleep(2)
        list_of_bloodgrp=self.driver.find_elements(by=By.XPATH, value=Data.Selectors.PIM_PD_Blood_grp_val)
        for i in list_of_bloodgrp:
            self.actions.scroll_to_element(i).perform()
            time.sleep(1)
            if i.text == Data.Data.PIM_Blood_grp:
                self.actions.move_to_element(i).click().perform()
                time.sleep(1)
                break
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_PD_SaveButton2).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_PD_SaveButton1).click()
        time.sleep(5)
        if self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_PD_FirstName).get_attribute('value') != Data.Data.First_name:
            self.test_TC_PIM_05_01_result = False
            print("First name is not meeting the expectations")
        if self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_PD_MiddleName).get_attribute('value') != Data.Data.Middle_name:
            self.test_TC_PIM_05_01_result = False
            print("middle name is not meeting the expectations")
        if self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_PD_LastName).get_attribute('value') != Data.Data.Last_name:
            self.test_TC_PIM_05_01_result = False
            print("lastname did not meet the expectation")
        if self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_PersDetail_NickName).get_attribute('value') != Data.Data.PIM_Nickname:
            self.test_TC_PIM_05_01_result = False
            print("Nickname is not matching ")
        if self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_PersDetail_OtherID).get_attribute('value') != Data.Data.PIM_otherid:
            self.test_TC_PIM_05_01_result = False
            print("Nickname is not matching ")
        if self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_PersDetail_DrivingLic).get_attribute('value') != Data.Data.PIM_DL:
            self.test_TC_PIM_05_01_result = False
            print("DL is not matching")
        if self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_PersDetail_licenceEXP).get_attribute('value') != Data.Data.PIM_DL_EXP:
            self.test_TC_PIM_05_01_result = False
            print("DL_EXP  is not matching")
        print("SSN: ",self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_PersDetail_SSN).get_attribute('value') )
        if self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_PersDetail_SSN).get_attribute('value') != Data.Data.PIM_SSN:
            self.test_TC_PIM_05_01_result = False
            print("SSN  is not matching")
        print(self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Nationality).text)
        if self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Nationality).text.lower() != Data.Data.PIM_Nationality.lower():
            self.test_TC_PIM_05_01_result = False
            print("Nationlaity  is not matching")
        print(self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Marital_Status).text)
        if self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Marital_Status).text.lower() != Data.Data.PIM_Marital_Status.lower():
            self.test_TC_PIM_05_01_result = False
            print("Maternity Status  is not matching")
        if Data.Data.PIM_gender == "Male":
            if (self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Gen_Male).is_selected() != True):
                self.test_TC_PIM_05_01_result = False
                print("Male checkbox is not enabled")
        if Data.Data.PIM_gender == "Female":
            if (self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Gen_Female).is_selected() != True):
                self.test_TC_PIM_05_01_result = False
                print("Female checkbox is not enabled")
        print("mit serv:", self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_MilitaryServices).get_attribute('value'))
        if self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_MilitaryServices).get_attribute('value') != Data.Data.PIM_Military_Serv:
            self.test_TC_PIM_05_01_result = False
            print("Military serv is not matching ")
        if Data.Data.PIM_Smoker_ == "Yes":
            if self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Smoker_checkbox).is_selected() != True:
                self.test_TC_PIM_05_01_result = False
                print("Smoker checkbox is not enabled")
        elif Data.Data.PIM_Smoker_ == "No":
            if self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Smoker_checkbox).is_selected() != False:
                self.test_TC_PIM_05_01_result = False
                print("Smoker checkbox is enabled while the input is No")
        print("Blood Grp:", self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_PD_Blood_Grp).text)
        if self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_PD_Blood_Grp).text != Data.Data.PIM_Blood_grp:
            self.test_TC_PIM_05_01_result = False
            print("blood group is not matching")
        time.sleep(3)
        assert self.test_TC_PIM_05_01_result
        print("SUCESS # TC_PIM_05_01_result completed ")

    def test_TC_PIM_06_1(self):
        self.TC_PIM_06_1_result=True
        time.sleep(5)
        self.actions.scroll_to_element(self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_CD_Tab)).perform()
        self.actions.move_to_element(self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_CD_Tab)).click().perform()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_CD_Street1).send_keys(Data.Data.PIM_CD_Street1)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_CD_Street2).send_keys(Data.Data.PIM_CD_Street2)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_CD_City).send_keys(Data.Data.PIM_CD_City)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_CD_State).send_keys(Data.Data.PIM_CD_State)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_CD_Zip).send_keys(Data.Data.PIM_CD_PIN)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_CD_Country).click()
        time.sleep(2)
        lis_of_country=self.driver.find_elements(by=By.XPATH,value=Data.Selectors.PIM_CD_Country_value)
        for i in lis_of_country:
            self.actions.scroll_to_element(i).perform()
            time.sleep(1)
            if i.text == Data.Data.PIM_CD_Country.capitalize():
                time.sleep(2)
                self.actions.move_to_element(i).perform()
                self.actions.click().perform()
                break
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_CD_Home_Phone).send_keys(Data.Data.PIM_Home_Phn)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_CD_Mobile_Phone).send_keys(Data.Data.PIM_Mobile_PHN)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_CD_Work_Phone).send_keys(Data.Data.PIM_Work_Phn)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_CD_EmailId).send_keys(Data.Data.PIM_Email)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_CD_SaveButton).click()
        time.sleep(5)
        try:
            self.driver.switch_to.alert.dismiss()
        except:
            pass
        print("street1: ",self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_CD_Street1).get_attribute('value'))
        if self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_CD_Street1).get_attribute('value') != Data.Data.PIM_CD_Street1:
            self.TC_PIM_06_1_result = False
            print("Street 1 is not matchiing ")
        print("street2: ",self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_CD_Street2).get_attribute('value'))
        if self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_CD_Street2).get_attribute('value') != Data.Data.PIM_CD_Street2:
            self.TC_PIM_06_1_result = False
            print("Street 2 is not matchiing ")
        print("city: ",self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_CD_City).get_attribute('value'))
        if self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_CD_City).get_attribute('value') != Data.Data.PIM_CD_City:
            self.TC_PIM_06_1_result = False
            print("City is not matchiing ")
        print("zip: ",self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_CD_Zip).get_attribute('value'))
        if str(self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_CD_Zip).get_attribute('value')).__contains__(str(Data.Data.PIM_CD_PIN)) != True:
            self.TC_PIM_06_1_result = False
            print("ZIP/PIN is not matchiing ")
        if self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_CD_Country).text != Data.Data.PIM_CD_Country:
            self.TC_PIM_06_1_result = False
            print("country is not matchiing ")
        if self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_CD_Home_Phone).get_attribute('value') != Data.Data.PIM_Home_Phn:
            self.TC_PIM_06_1_result = False
            print("Home Phone is not matchiing ")
        if self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_CD_Mobile_Phone).get_attribute('value') != Data.Data.PIM_Mobile_PHN:
            self.TC_PIM_06_1_result = False
            print("Mobile Phone is not matchiing ")
        if self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_CD_Work_Phone).get_attribute('value') != Data.Data.PIM_Work_Phn:
            self.TC_PIM_06_1_result = False
            print("Work Phone is not matchiing ")
        if self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_CD_EmailId).get_attribute('value') != Data.Data.PIM_Email:
            self.TC_PIM_06_1_result = False
            print("Email is not matchiing ")

        assert self.TC_PIM_06_1_result
        print("SUCCESS # TC_PIM_06_1_result is compleate ")

    def test_TC_PIM_07_1(self):
        self.TC_PIM_07_1_result = True
        time.sleep(5)
        self.actions.scroll_to_element(self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_EC_Tab)).move_to_element(self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_EC_Tab)).perform()
        self.actions.click().perform()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_EC_Add_Button).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_EC_Name).send_keys(Data.Data.PIM_EC_Name)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_EC_Relationship)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_EC_Relationship).send_keys(Data.Data.PIM_EC_Relationship)
        time.sleep(3)
        #self.driver.find_element(by=By.XPATH, value=Data.Data.PIM_EC_Home_Tele).click()
        #time.sleep(2)
        #self.driver.find_element(by=By.XPATH,value=Data.Data.PIM_EC_Home_Tele).send_keys(Data.Data.PIM_EC_Home_Tele)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_EC_Mobile_Tele).send_keys(Data.Data.PIM_EC_Mobile_Tele)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_EC_Work_Tele).click()
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_EC_Work_Tele).send_keys(Data.Data.PIM_EC_Work_Tele)
        time.sleep(3)
        try:
            self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Save_Button).click()
        except:
            self.actions.send_keys(Keys.ENTER).perform()
            print("Enter key action is performed ")
        time.sleep(5)
        print("Name: ",self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_EC_Saved_Name).text)
        if self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_EC_Saved_Name).text != Data.Data.PIM_EC_Name:
            self.TC_PIM_07_1_result = False
            print("Name is not matching")
        print("Relation: ", self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_EC_Saved_Realtionship).text)
        if self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_EC_Saved_Realtionship).text != Data.Data.PIM_EC_Relationship:
            self.TC_PIM_07_1_result = False
            print("Relationship is not matching")
        print("Home Telephone: ",self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_EC_Saved_HomeTele).text)
        '''if self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_EC_Saved_HomeTele).text != Data.Data.PIM_EC_Home_Tele:
            self.TC_PIM_07_1_result = False
            print("Relationship is not matching")'''
        print("Mobile Telephone: ",self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_EC_Saved_MobileTele).text)
        if self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_EC_Saved_MobileTele).text != Data.Data.PIM_EC_Mobile_Tele:
            self.TC_PIM_07_1_result = False
            print("Mobile Tele is not matching")
        print("Mobile Telephone: ",self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_EC_Saved_WorkTele).text)
        if self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_EC_Saved_WorkTele).text != Data.Data.PIM_EC_Mobile_Tele:
            self.TC_PIM_07_1_result = False
            print("work tele is not matching")
        assert self.TC_PIM_07_1_result
        print("SUCESS # test_TC_PIM_07_1 is completed ")

    def test_TC_PIM_08_1(self):
        self.TC_PIM_08_1_result = True
        time.sleep(3)
        self.actions.scroll_to_element(self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Dependents_tab)).perform()
        self.actions.move_to_element(self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Dependents_tab)).click().perform()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Dependents_addButton).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Dependents_Name).send_keys(Data.Data.PIM_EC_Name)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Dependents_relation).click()
        time.sleep(2)
        self.actions.move_to_element(self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Dependents_relation_list))
        time.sleep(2)
        list_of_relation=self.driver.find_elements(by=By.XPATH,value=Data.Selectors.PIM_Dependents_relation_value)
        for i in list_of_relation:
            self.actions.move_to_element(i)
            if i.text.lower() == Data.Data.PIM_Dep_relationship.lower():
                self.actions.move_to_element(i).click().perform()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Dependents_other).send_keys(Data.Data.PIM_EC_Relationship)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Dependents_DOB).send_keys(Data.Data.PIM_Dep_DOB)
        time.sleep(2)
        try:
            self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Dependents_save_button).click()
            print("click got performed ")
        except:
            self.actions.send_keys(Keys.ENTER).perform()
            print("Enter action key is performed ")
        time.sleep(5)
        print(self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Dependents_saved_name).text)
        if self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Dependents_saved_name).text != Data.Data.PIM_EC_Name:
            self.TC_PIM_08_1_result = False
            print("Names are not matching")
        print(self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Dependents_saved_DOB).text)
        if self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Dependents_saved_DOB).text != Data.Data.PIM_Dep_DOB:
            self.TC_PIM_08_1_result = False
            print("DOB is not matching")
        print(self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Dependents_saved_Relationship).text)
        if self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Dependents_saved_Relationship).text != Data.Data.PIM_EC_Relationship:
            self.TC_PIM_08_1_result = False
            print("DOB is not matching")
        assert self.TC_PIM_08_1_result
        print("SUCESS # TC_PIM_08_1 is completed")

    def test_TC_PIM_09_1(self):
        self.TC_PIM_09_1=True
        time.sleep(3)
        self.actions.scroll_to_element(self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Immigration_tab)).perform()
        self.actions.move_to_element(self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Immigration_tab)).click().perform()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Immigration_Add_button).click()
        time.sleep(2)
        if Data.Data.PIM_Immig_Document == "Passport":
            if self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Immigration_Passport_radio).is_enabled() != True:
                self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Immigration_Passport_radio).click()
        elif Data.Data.PIM_Immig_Document == "Visa":
            if self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Immigration_Visa_radio).is_enabled() != True:
                self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Immigration_Passport_radio).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Immigration_Number).send_keys(Data.Data.PIM_Immig_Num)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Immigration_issueDate).send_keys(Data.Data.PIM_Immg_issueDate)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Immigration_ExpDate).send_keys(Data.Data.PIIM_Immg_expdate)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Immigration_Eligibility_status).send_keys(Data.Data.PIM_immg_Eligible_Status)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_issuedby_).click()
        time.sleep(1)
        self.actions.move_to_element(self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_issuedby_list))
        list_of_issued_country=self.driver.find_elements(by=By.XPATH,value=Data.Selectors.PIM_issuedby_value)
        for i in list_of_issued_country:
            time.sleep(1)
            self.actions.move_to_element(i).perform()
            if i.text.lower() == Data.Data.PIM_Immig_Passport_issue_country.lower():
                self.actions.move_to_element(i).click().perform()
                break
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Immigration_Eligibility_review_date).send_keys(Data.Data.PIM_Immg_rivewDate)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Immigration_save_button).click()
        time.sleep(5)
        print("Document:",self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Immigration_saved_name).text)
        if self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Immigration_saved_name).text != Data.Data.PIM_Immig_Document:
            self.TC_PIM_09_1 = False
            print("Document is not matching")
        print("Doc number:", self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Immigration_Saved_Number).text)
        if self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Immigration_Saved_Number).text != Data.Data.PIM_Immig_Num:
            self.TC_PIM_09_1 = False
            print("Number is not matching")
        print("issue date:",self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Immigration_Saved_issued_date).text)
        if self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Immigration_Saved_issued_date).text != Data.Data.PIM_Immg_issueDate:
            self.TC_PIM_09_1 = False
            print("issue date is not matching")
        print("issue date:",self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Immigration_Saved_Exipiry_Date).text)
        if self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Immigration_Saved_Exipiry_Date).text != Data.Data.PIIM_Immg_expdate:
            self.TC_PIM_09_1 = False
            print("expire date is not matching")
        assert self.TC_PIM_09_1
        print("SUCESS # TC_PIM_09_1 test  case is completed ")

    def test_TC_PIM_10_1(self):
        self.TC_PIM_10_1_result=True
        time.sleep(3)
        self.actions.scroll_to_element(self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_job_tab)).perform()
        self.actions.move_to_element(self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_job_tab)).click().perform()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_job_joinedDate).send_keys(Data.Data.PIM_Job_JoiningDate)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Job_Title).click()
        time.sleep(1)
        self.actions.move_to_element(self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Job_Title_list))
        time.sleep(1)
        list_of_job_title=self.driver.find_elements(by=By.XPATH,value=Data.Selectors.PIM_Job_Title_value)
        for i in list_of_job_title:
            self.actions.move_to_element(i).perform()
            if i.text.lower() == Data.Data.PIM_Job_Title.lower():
                self.actions.move_to_element(i).click().perform()
                break
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Job_Category).click()
        time.sleep(1)
        self.actions.move_to_element(self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Job_Category_list))
        time.sleep(1)
        list_of_job_Category = self.driver.find_elements(by=By.XPATH, value=Data.Selectors.PIM_Job_Category_value)
        for i in list_of_job_Category:
            self.actions.move_to_element(i).perform()
            if i.text.lower() == Data.Data.PIM_Job_Category.lower():
                self.actions.move_to_element(i).click().perform()
                break
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Job_Sub_Unit).click()
        time.sleep(1)
        self.actions.move_to_element(self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Job_Sub_Unit_list))
        time.sleep(1)
        list_of_job_sub_unit = self.driver.find_elements(by=By.XPATH, value=Data.Selectors.PIM_Job_Sub_Unit_value)
        for i in list_of_job_sub_unit:
            self.actions.move_to_element(i).perform()
            if i.text.lower() == Data.Data.PIM_Job_Sub_Unit.lower():
                self.actions.move_to_element(i).click().perform()
                break
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Job_Location).click()
        time.sleep(1)
        self.actions.move_to_element(self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Job_Location_list))
        time.sleep(1)
        list_of_job_location = self.driver.find_elements(by=By.XPATH, value=Data.Selectors.PIM_Job_Location_value)
        for i in list_of_job_location:
            self.actions.move_to_element(i).perform()
            if i.text.lower() == Data.Data.PIM_Job_Location.lower():
                self.actions.move_to_element(i).click().perform()
                break
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Job_Employe_status).click()
        time.sleep(1)
        self.actions.move_to_element(self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Job_Employe_list))
        time.sleep(1)
        list_of_job_Emp_Status = self.driver.find_elements(by=By.XPATH, value=Data.Selectors.PIM_Job_Employe_value)
        for i in list_of_job_Emp_Status :
            self.actions.move_to_element(i).perform()
            if i.text.lower() == Data.Data.PIM_Job_Employment_Status.lower():
                self.actions.move_to_element(i).click().perform()
                break
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Job_Emp_ContactDetail_toggle).click()
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Job_Contract_Start_Date).send_keys(Data.Data.PIM_Job_Contratc_StartDate)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Job_Contratc_End_Date).send_keys(Data.Data.PIM_Job_Contract_EndDate)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Job_Save_Button).click()
        time.sleep(5)
        if self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_job_joinedDate).get_attribute('value') != Data.Data.PIM_Job_JoiningDate:
            self.TC_PIM_10_1_result = False
            print("Joining date is not mathcing")
        time.sleep(1)
        if self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Job_Title).text.lower() != Data.Data.PIM_Job_Title.lower():
            self.TC_PIM_10_1_result = False
            print("Job title is not mathcing")
        time.sleep(1)
        if self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Job_Category).text.lower() != Data.Data.PIM_Job_Category.lower():
            self.TC_PIM_10_1_result = False
            print("category is not mathcing")
        time.sleep(1)
        if self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Job_Sub_Unit).text.lower() != Data.Data.PIM_Job_Sub_Unit.lower():
            self.TC_PIM_10_1_result = False
            print("sub_unit is not mathcing")
        time.sleep(1)
        if self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Job_Location).text.lower() != Data.Data.PIM_Job_Location.lower():
            self.TC_PIM_10_1_result = False
            print("Location is not mathcing")
        time.sleep(1)
        if self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Job_Employe_status).text.lower() != Data.Data.PIM_Job_Employment_Status.lower():
            self.TC_PIM_10_1_result = False
            print("Employee status is not mathcing")
        time.sleep(1)
        if self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Job_Emp_ContactDetail_toggle).is_enabled() != True:
            self.TC_PIM_10_1_result = False
            print("Employe Contact detial toggle status is not enabled")
        time.sleep(1)
        if self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Job_Contract_Start_Date).get_attribute('value').lower() != Data.Data.PIM_Job_Contratc_StartDate.lower():
            self.TC_PIM_10_1_result = False
            print("contract start date is not mathching")
        time.sleep(1)
        if self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Job_Contratc_End_Date).get_attribute('value').lower() != Data.Data.PIM_Job_Contract_EndDate.lower():
            self.TC_PIM_10_1_result = False
            print("contract end date is not mathching")

        assert self.TC_PIM_10_1_result
        print("SUCESS # TC_PIM_10_1 is completed")

    def test_TC_PIM_11_1(self):
        self.TC_PIM_11_1 = True
        time.sleep(4)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Job_Terminate_Employment).click()
        WebDriverWait(self.driver,20).until(EC.visibility_of(self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Job_Terminate_Employment_form)))
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Job_Termination_Date).send_keys(Data.Data.PIM_Termination_Date)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Job_Termination_Reason).click()
        time.sleep(3)
        self.actions.move_to_element(self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Job_Termination_Reason_List)).perform()
        time.sleep(1)
        list_of_reason=self.driver.find_elements(by=By.XPATH,value=Data.Selectors.PIM_Job_Termination_Reason_value)
        for i in list_of_reason:
            self.actions.move_to_element(i).perform()
            print("Termination reason:",i.text.lower())
            time.sleep(1)
            if i.text.lower() == Data.Data.PIM_Termination_Reason.lower():
                self.actions.move_to_element(i).click().perform()
                break
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Job_Termination_Reason_Note).send_keys(Data.Data.PIM_Termination_Reason_Note)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Job_Termination_Reason_Save_Button).click()
        time.sleep(6)
        WebDriverWait(self.driver,15).until(EC.visibility_of(self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Job_TerminationOn_link)))
        Terminated_on= "Terminated on: "+Data.Data.PIM_Termination_Date
        if self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Job_TerminationOn_link).text.lower().__contains__(Terminated_on.lower()) != True:
            self.TC_PIM_11_1 = False
            print("Termination on date is not matching")
        if self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Job_Activate_Employment_button).is_displayed() != True:
            if self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Job_Activate_Employment_button).text.lower() != " Activate Employment ":
                self.TC_PIM_11_1 = False
                print("Activate Employment is not matching")
        assert self.TC_PIM_11_1
        print("SUCESS # TC_PIM_11_1 is compleat")

    def test_TC_PIM_12_1(self):
        self.TC_PIM_12_1 = True
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Job_Activate_Employment_button).click()
        time.sleep(5)
        WebDriverWait(self.driver,20).until(EC.visibility_of(self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Job_Terminate_Employment)))
        if self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Job_Terminate_Employment).is_displayed() != True:
            self.TC_PIM_12_1 = False
            print("Terminate Employment button is not displayed ")
            if self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Job_Terminate_Employment).text.lower() != " Terminate Employment ":
                self.TC_PIM_12_1 = False
                print("Terminate Employment is not displayed in the button")
        assert self.TC_PIM_12_1
        print("SUCESS #TC_PIM_12_1 is compleat ")

    def test_TC_PIM_13_1(self):
        self.TC_PIM_13_1_result = True
        time.sleep(2)
        self.actions.scroll_to_element(self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Salary_Tab)).perform()
        self.actions.move_to_element(self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Salary_Tab)).click().perform()
        time.sleep(6)
        WebDriverWait(self.driver,15).until(EC.visibility_of(self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Salary_AddButton)))
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Salary_AddButton).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Salary_Compensation).send_keys(Data.Data.PIM_Salary_Compensation)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Salary_PayGrade).click()
        time.sleep(1)
        self.actions.move_to_element(self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Salary_PayGrade_List)).perform()
        time.sleep(2)
        list_Paygrade= self.driver.find_elements(by=By.XPATH,value=Data.Selectors.PIM_Salary_ParGrade_Value)
        for i in list_Paygrade:
            self.actions.move_to_element(i).perform()
            time.sleep(1)
            if i.text.lower() == Data.Data.PIM_Salary_PayGrade.lower():
                self.actions.move_to_element(i).click().perform()
                break
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Salary_PayFrequency).click()
        time.sleep(1)
        self.actions.move_to_element(self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Salary_PayFrequency_List)).perform()
        time.sleep(2)
        list_Payfrequency = self.driver.find_elements(by=By.XPATH, value=Data.Selectors.PIM_Salary_PayFrequency_value)
        for i in list_Payfrequency:
            self.actions.move_to_element(i).perform()
            time.sleep(1)
            if i.text.lower() == Data.Data.PIM_Salary_PayFrequecny.lower():
                self.actions.move_to_element(i).click().perform()
                break
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Salary_Currency).click()
        time.sleep(1)
        self.actions.move_to_element(
            self.driver.find_element(by=By.XPATH, value=Data.Selectors.PIM_Salary_Currency_List)).perform()
        time.sleep(2)
        list_Currency = self.driver.find_elements(by=By.XPATH, value=Data.Selectors.PIM_Salary_Currency_Value)
        for i in list_Currency:
            self.actions.move_to_element(i).perform()
            time.sleep(1)
            if i.text.lower() == Data.Data.PIM_Salary_Currency.lower():
                self.actions.move_to_element(i).click().perform()
                break
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Salary_Amount).send_keys(Data.Data.PIM_Salary_Monthy_amount)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Salary_DDDetails).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Salary_AccNo).send_keys(Data.Data.PIM_Salary_AccNo)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Salary_AccType).click()
        time.sleep(1)
        self.actions.move_to_element(self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Salary_AccType_List))
        time.sleep(1)
        list_AccType= self.driver.find_elements(by=By.XPATH,value=Data.Selectors.PIM_Salary_AccType_Value)
        for i in list_AccType:
            self.actions.move_to_element(i).perform()
            time.sleep(1)
            if i.text.lower() == Data.Data.PIM_Acc_Type.lower():
                self.actions.move_to_element(i).click().perform()
                break
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Salary_RountingNumber).send_keys(Data.Data.PIM_Routing_Number)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Salary_DD_Amount).send_keys(Data.Data.PIM_Salary_Monthy_amount)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Salary_Save_Button).click()
        time.sleep(5)
        print("Compensation: ",self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Salary_Saved_comp).text)
        if self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Salary_Saved_comp).text != Data.Data.PIM_Salary_Compensation:
            self.TC_PIM_13_1_result = False
            print("Compensation is not matching")
        print("monthly amt:",int(self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Salary_Saved_Amount).text))
        if int(self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Salary_Saved_Amount).text) != Data.Data.PIM_Salary_Monthy_amount:
            self.TC_PIM_13_1_result = False
            print("Monthly Amount  is not matching")
        print("Currency: ",self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Salary_Saved_Currecny).text)
        if self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Salary_Saved_Currecny).text.lower() != Data.Data.PIM_Salary_Currency.lower():
            self.TC_PIM_13_1_result = False
            print("currency  is not matching")
        print("Frequecny:",self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Salary_Saved_Frequency).text)
        if self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Salary_Saved_Frequency).text.lower() != Data.Data.PIM_Salary_PayFrequecny.lower():
            self.TC_PIM_13_1_result = False
            print("frequecny  is not matching")
        print("Monthly DD:", float(self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Salary_Saved_DD_Amount).text), float(round(Data.Data.PIM_Salary_Monthy_amount,2)))
        if float(self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_Salary_Saved_DD_Amount).text) != float(round(Data.Data.PIM_Salary_Monthy_amount,2)):
            self.TC_PIM_13_1_result = False
            print("frequecny  is not matching")
        assert self.TC_PIM_13_1_result
        print("SUCESS # completed TC 13")

    def test_TC_PIM_14_1(self):
        self.TC_PIM_14_1_result = True
        time.sleep(4)
        self.actions.scroll_to_element(self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_TaxExemp_Tab)).perform()
        self.actions.move_to_element(self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_TaxExemp_Tab)).click().perform()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_TaxExemp_Status).click()
        time.sleep(1)
        self.actions.move_to_element(self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_TaxExemp_Status_List)).perform()
        list_of_status=self.driver.find_elements(by=By.XPATH,value=Data.Selectors.PIM_TaxExemp_Status_Value)
        for i in list_of_status:
            self.actions.move_to_element(i).perform()
            if i.text.lower() == Data.Data.PIM_Tax_Status.lower():
                self.actions.click().perform()
                break
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_TaxExemp_Exemption).send_keys(Data.Data.PIM_Tax_Exemption)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_TaxExemp_State).click()
        time.sleep(1)
        self.actions.move_to_element(self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_TaxExemp_State_List)).perform()
        time.sleep(1)
        list_of_state= self.driver.find_elements(by=By.XPATH,value=Data.Selectors.PIM_TaxExemp_State_Value)
        for i in list_of_state:
            self.actions.move_to_element(i).perform()
            if i.text.lower() == Data.Data.PIM_Tax_State.lower():
                self.actions.click().perform()
                break
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_TaxExemp_Status2).click()
        self.actions.move_to_element(self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_TaxExemp_Status2_List)).perform()
        list_Of_Tax_Status= self.driver.find_elements(by=By.XPATH,value=Data.Selectors.PIM_TaxExemp_Status2_Value)
        for i in list_Of_Tax_Status:
            self.actions.move_to_element(i).perform()
            time.sleep(1)
            if i.text.lower() == Data.Data.PIM_Tax_Status.lower():
                self.actions.move_to_element(i).click().perform()
                break
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_TaxExemp_Exemptions).send_keys(Data.Data.PIM_Tax_Exemption)
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_TaxExemp_UnemploymentState).click()
        self.actions.move_to_element(self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_TaxExemp_UnemploymentState_List)).perform()
        List_of_UnemployedState= self.driver.find_elements(by=By.XPATH,value=Data.Selectors.PIM_TaxExemp_UnemploymentState_Value)
        for i in List_of_UnemployedState:
            self.actions.move_to_element(i).perform()
            time.sleep(1)
            if i.text.lower() == Data.Data.PIM_Tax_UnemploymetState.lower():
                self.actions.move_to_element(i).click().perform()
                break
        time.sleep(1)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_TaxExemp_WorkState).click()
        self.actions.move_to_element(self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_TaxExemp_WorkState_List)).perform()
        list_Of_WorkState=self.driver.find_elements(by=By.XPATH,value=Data.Selectors.PIM_TaxExemp_WorkState_Value)
        for i in list_Of_WorkState:
            self.actions.move_to_element(i).perform()
            time.sleep(1)
            if i.text.lower() == Data.Data.PIM_Tax_State.lower():
                self.actions.move_to_element(i).click().perform()
                break
        time.sleep(2)
        self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_TaxExemp_Save_Button).click()
        time.sleep(5)
        print("Tax Status: ",self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_TaxExemp_Status).text)
        if self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_TaxExemp_Status).text.lower() != Data.Data.PIM_Tax_Status.lower():
            self.TC_PIM_14_1_result = False
            print("Tax Status is mismatching")
        print("Tax Exemption1: ",self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_TaxExemp_Exemption).get_attribute('value'))
        if int(self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_TaxExemp_Exemption).get_attribute('value')) != Data.Data.PIM_Tax_Exemption:
            self.TC_PIM_14_1_result = False
            print("Tax Exemption1 is mismatching")
        print("State: ",self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_TaxExemp_State).text)
        if self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_TaxExemp_State).text.lower() != Data.Data.PIM_Tax_State.lower():
            self.TC_PIM_14_1_result = False
            print("State  is mismatching")
        print("status2:",self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_TaxExemp_Status2).text)
        if self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_TaxExemp_Status2).text.lower() != Data.Data.PIM_Tax_Status.lower():
            self.TC_PIM_14_1_result = False
            print("Status2  is mismatching")
        print("Exemption2: ",self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_TaxExemp_Exemptions).get_attribute('value'))
        if int(self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_TaxExemp_Exemptions).get_attribute('value')) != Data.Data.PIM_Tax_Exemption:
            self.TC_PIM_14_1_result = False
            print("Exemption2  is mismatching")
        print("Unemployed state: ",self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_TaxExemp_UnemploymentState).text)
        if self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_TaxExemp_UnemploymentState).text.lower() != Data.Data.PIM_Tax_UnemploymetState.lower():
            self.TC_PIM_14_1_result = False
            print("unemployment state  is mismatching")
        print("Working state: ",self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_TaxExemp_WorkState).text)
        if self.driver.find_element(by=By.XPATH,value=Data.Selectors.PIM_TaxExemp_WorkState).text.lower() != Data.Data.PIM_Tax_State.lower():
            self.TC_PIM_14_1_result = False
            print("Working state  is mismatching")
        assert self.TC_PIM_14_1_result
        print("SUCESS # TC_PIM_14_1 test is completed ")


















