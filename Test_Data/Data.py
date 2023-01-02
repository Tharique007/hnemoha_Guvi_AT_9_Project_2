import random
import string


class Data:
    Admin_Username="Admin"
    Admin_Password ="admin123"

    #dashborad
    dashboard_url="https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    #left_nave_element
    Element_of_leftnave=["Admin","PIM","Leave","Time","Recruitment","My Info","Performance","Dashboard","Directory","Maintenance","Buzz"]

    #list of options in user roll
    user_role_list=["-- Select --", "Admin", "ESS"]

    #list_of_options_in_Status_dd
    status_list=["-- Select --", "Enabled", "Disabled"]

    #PIM_Input_Data
    First_name="Mohamed"
    Middle_name="Tharique"
    Last_name="Haneefa A M"
    Pim_UserName="hnemoha661"+str(random.randrange(1,25))
    Pim_password= Pim_UserName+"!"+"A"
    PIM_SubNave=["Personal Details","Contact Details","Emergency Contacts","Dependents","Immigration","Job","Salary","Tax Exemptions","Report-to","Qualifications","Memberships"]

    PIM_Nickname="hnemohaa"
    PIM_otherid=str(random.randrange(100,1000))
    listnum=random.sample(range(1,8),7)
    listalpha=random.sample(range(65,90),9)
    PIM_DL=""
    for i in listnum:
        PIM_DL = PIM_DL+str(i)
    for j in listalpha:
        PIM_DL=PIM_DL+str(chr(j))
    PIM_DL_EXP = "2023-12-20"
    PIM_DOB = "1995-01-07"
    PIM_SSN = "789456123"
    listssn=random.sample(range(0,9),9)
    for i in listssn:
        PIM_SSN = PIM_SSN + str(i)
    PIM_Nationality = "indian"
    PIM_Marital_Status = "Single"

    PIM_DOB = "1995-01-07"
    PIM_gender = "Male"
    PIM_Military_Serv = ""
    PIM_Smoker_ = "No"
    PIM_Blood_grp = "AB+"


    #PIM_ContactDetails page variable
    PIM_CD_Street1=str(random.randrange(1,100))+" Kaseem street"
    PIM_CD_Street2=str(random.randrange(1,12))+"nd lane"
    PIM_CD_City="Chennai"
    PIM_CD_State="TamilNadu"
    PIM_CD_PIN=random.randrange(600000,600100)
    PIM_Home_Phn="7"
    PIM_HM_Ph_list=random.sample(range(0,9),9)
    for i in PIM_HM_Ph_list:
        PIM_Home_Phn += str(i)
    PIM_Mobile_PHN="8"
    PIM_MOB_PH_list=random.sample(range(0,9),9)
    for j in PIM_MOB_PH_list:
        PIM_Mobile_PHN += str(j)
    PIM_Work_Phn="9"
    PIM_Work_Phn_list=random.sample(range(0,9),9)
    for k in PIM_Work_Phn_list:
        PIM_Work_Phn += str(k)
    PIM_Email=""
    alphabest=random.sample(range(65,90),9)
    Numeric=random.sample(range(0,9),5)
    for i in alphabest:
        PIM_Email += chr(i)
    for j in Numeric:
        PIM_Email += str(j)
    PIM_Email += "@example.com"
    PIM_CD_Country="India"

    #PIM_Emergency_contact Data
    PIM_EC_Name=random.choice(["Faridha Begam M","Ameer Salma A M","Thasleem"])
    PIM_EC_Relationship=random.choice(["Mother","Sister","Aunt"])
    PIM_EC_Home_Tele= "98"
    EC_Home_tel = random.sample(range(0,9),8)
    for i in EC_Home_tel:
        PIM_EC_Home_Tele += str(i)
    PIM_EC_Mobile_Tele="98"
    EC_Mobile_Tele = random.sample(range(0,9),8)
    for i in EC_Mobile_Tele:
        PIM_EC_Mobile_Tele +=str(i)
    PIM_EC_Work_Tele="98"
    EC_Work_Tele = random.sample(range(0,9),8)
    for i in EC_Mobile_Tele:
        PIM_EC_Work_Tele +=str(i)

    #PIM_Dependents_varibale
    PIM_Dep_relationship="Other"
    PIM_Dep_DOB="1950-07-06"

    PIM_Immig_Document="Passport"
    PIM_Immig_Num="789789456456123123"
    PIM_Immg_issueDate="2000-07-01"
    PIIM_Immg_expdate="2024-12-20"
    PIM_immg_Eligible_Status="Eligible"
    PIM_Immg_rivewDate="2022-01-01"
    PIM_Immig_Passport_issue_country="India"

    #PIM_Job_Details
    PIM_Job_JoiningDate="2011-01-04"
    PIM_Job_Title="QA Lead"
    PIM_Job_Category="Professionals"
    PIM_Job_Sub_Unit="Quality Assurance"
    PIM_Job_Location="New York Sales Office"
    PIM_Job_Employment_Status="Full-Time Permanent"
    PIM_Job_Contratc_StartDate="2020-01-01"
    PIM_Job_Contract_EndDate="2023-01-31"

    #PIM_Job_Termination_Details
    PIM_Termination_Reason="Resigned"
    PIM_Termination_Date="2023-01-31"
    PIM_Termination_Reason_Note=''.join(random.choice(string.ascii_letters) for i in range(10))

    #PIM_Salary_Tab_variable
    PIM_Salary_Compensation=str(random.randrange(600000,900000))
    PIM_Salary_PayGrade="Grade 5"
    PIM_Salary_PayFrequecny="Monthly"
    PIM_Salary_Currency = "United States Dollar"
    PIM_Salary_Monthy_amount=random.randrange(10000,20000)
    PIM_Salary_AccNo=""
    AccNo=random.sample(range(10,30),8)
    for i in AccNo:
        PIM_Salary_AccNo += str(i)
    PIM_Acc_Type="Savings"
    PIM_Routing_Number=""
    Rout_num=random.sample(range(10,20),4)
    for i in Rout_num:
        PIM_Routing_Number += str(i)

    #PIM_Tax_Exemption_Variable
    PIM_Tax_Status="Single"
    PIM_Tax_Exemption=random.randrange(1,99)
    PIM_Tax_State="Indiana"
    PIM_Tax_UnemploymetState="California"







class Selectors:
    #login page Selectors
    login_username="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input"
    login_password="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input"
    loginPage_loginButton="/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button"

    # left_nave
    leftnave_admin = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span'
    leftname_listofElement='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span'

    #Dashboard page
    dashbord_header='//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6'

    #admin page
    admin_header='//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6[1]'
    admin_page_subheading='//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6[2]'


    Admin_page_Usermanagement_tab='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/span'
    Admin_page_Usermanagement_tab_user_DD='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li/a'

    Admin_page_leftnave_search_field='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/div/div/input'
    Admin_page_leftnave_search_result='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span'

    UserManagement_UserRole_DD='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]'
    UserManagement_UserRole_DD_='// *[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[@role="listbox"]'
    UserManagement_UserRole_DD_list='// *[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div[@role="listbox"]/div'

    UserManagement_Status_DD='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]'
    UserManagement_Status_DD_='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div[@role="listbox"]'
    UserManagement_Status_DD_list='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div[@role="listbox"]/div'

    #PIM page selector
    PIM_in_leftnave='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span'
    PIM_leftnave_list='//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li/a/span'
    PIM_Top_Headder='//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6'
    PIM_ADD_Button='//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button/i'
    PIM_AddEmployee='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/h6'
    PIM_CreateLoginDetail_toggleButton='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[2]/div/label/span'
    PIM_Emp_ID='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input'
    PIM_EmpId_Exist_error='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/span'

    PIM_FirstName='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input'
    PIM_MiddleName='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input'
    PIM_LastName='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input'
    PIM_UserName='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[1]/div/div[2]/input'
    PIM_Password='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[1]/div/div[2]/input'
    PIM_ConfirmPassword='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[4]/div/div[2]/div/div[2]/input'
    PIM_Status_Enabled='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/div[1]/div[2]/div/label/span'
    PIM_Status_Disabled='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[3]/div/div[2]/div/div[2]/div[2]/div[2]/div/label/span'
    PIM_Save_Button='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[text()=" Save "]'
    PIM_Cancel_Button='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[1]'
    PIM_Employee_List_Tab='//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a'
    PIM_Personal_Deatails='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/h6'
    PIM_EmployeeListTab_SubNave='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div/div/div/a'
    PIM_Personal_Deatails_subnave='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[1]/a'

    PIM_PersDetail_NickName='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input'
    PIM_PersDetail_EmployeeId='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[1]/div/div[2]/input'
    PIM_PersDetail_OtherID='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input'
    PIM_PersDetail_DrivingLic='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input'
    PIM_PersDetail_licenceEXP='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input'
    PIM_PersDetail_SSN='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input'

    PIM_Nationality='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[1]'
    PIM_Nationality_list='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div[@role="listbox"]'
    PIM_Nationality_IND='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div[@role="listbox"]/div'

    PIM_Marital_Status='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[1]'
    PIM_Marital_Status_list='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div[@role="listbox"]'
    PIM_Marital_status_Single='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div[@role="listbox"]/div'

    PIM_DOB='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input'
    PIM_Gender_Male='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span'
    PIM_Gen_Male='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/input'
    PIM_Gender_Female='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/label/span'
    PIM_Gen_Female='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[2]/div[2]/div/label/input'

    PIM_MilitaryServices='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div/div[2]/input'
    PIM_Smoker_checkbox='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[2]/div/div[2]/div/label/span'
    PIM_PD_SaveButton1='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'
    PIM_PD_SaveButton2='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button'
    PIM_PD_Blood_Grp='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div[2]/div/div/div[1]'
    PIM_PD_Blood_Grp_lst='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div[2]/div/div[@role="listbox"]'
    PIM_PD_Blood_grp_val='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div[2]/div/div[@role="listbox"]/div'

    PIM_PD_FirstName='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input'
    PIM_PD_MiddleName='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input'
    PIM_PD_LastName='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input'

    #PIM_CaseDeatial page elements

    PIM_CD_Tab='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/a'
    PIM_CD_Street1='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    PIM_CD_Street2='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input'
    PIM_CD_City='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input'
    PIM_CD_State='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/input'
    PIM_CD_Zip='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input'

    PIM_CD_Country='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div/div[1]'
    PIM_CD_Country_list='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div[@role="listbox"]'
    PIM_CD_Country_value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div[@role="listbox"]/div'

    PIM_CD_Home_Phone='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input'
    PIM_CD_Mobile_Phone='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input'
    PIM_CD_Work_Phone='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input'

    PIM_CD_EmailId='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/input'
    PIM_CD_SaveButton='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button'

    #PIM_EmergrncyContatc_tab_Elements
    PIM_EC_Tab='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]/a'
    PIM_EC_Add_Button='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button/i'
    PIM_EC_Name='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    PIM_EC_Relationship='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input'
    PIM_EC_Home_Tele='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input'
    PIM_EC_Mobile_Tele='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input'
    PIM_EC_Work_Tele='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input'
    PIM_EC_Save_button='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[text()=" Save "]'


    PIM_EC_Saved_Name='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div'
    PIM_EC_Saved_Realtionship='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div'
    PIM_EC_Saved_HomeTele='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[4]/div'
    PIM_EC_Saved_MobileTele='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[5]/div'
    PIM_EC_Saved_WorkTele='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[6]/div'

    #PIM_Dependents_page_selectors
    PIM_Dependents_tab='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[4]/a'
    PIM_Dependents_addButton='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button'
    PIM_Dependents_Name='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'

    PIM_Dependents_relation='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]'
    PIM_Dependents_relation_list='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div[@role="listbox"]'
    PIM_Dependents_relation_value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div[@role="listbox"]/div'
    PIM_Dependents_other='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/input'
    PIM_Dependents_DOB='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div/div/div[2]/div/div/input'
    PIM_Dependents_save_button='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]'

    PIM_Dependents_saved_name='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div'
    PIM_Dependents_saved_Relationship='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div'
    PIM_Dependents_saved_DOB='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[4]/div'

    #PIM_Immigration_Page_Selectors
    PIM_Immigration_tab='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[5]/a'
    PIM_Immigration_Add_button='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button'
    PIM_Immigration_Passport_radio='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div/div/div[2]/div[1]/div[2]/div/label/span'
    PIM_Immigration_Visa_radio='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div/div/div[2]/div[1]/div[2]/div/label/span'
    PIM_Immigration_Number='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input'
    PIM_Immigration_issueDate='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/div/div/input'
    PIM_Immigration_ExpDate='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/div/div/input'
    PIM_Immigration_Eligibility_status='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[4]/div/div[2]/input'
    PIM_issuedby_='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[5]/div/div[2]/div/div/div[1]'
    PIM_issuedby_list='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[5]/div/div[2]/div/div[@role="listbox"]'
    PIM_issuedby_value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[5]/div/div[2]/div/div[@role="listbox"]/div'
    PIM_Immigration_Eligibility_review_date='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[6]/div/div[2]/div/div/input'
    PIM_Immigration_save_button='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[2]'

    PIM_Immigration_saved_name = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div'
    PIM_Immigration_Saved_Number = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div'
    PIM_Immigration_Saved_issued_date = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[5]/div'
    PIM_Immigration_Saved_Exipiry_Date = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[6]/div'

    #PIM_JobPage_Selector
    PIM_job_tab='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[6]/a'
    PIM_job_joinedDate='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div/input'
    PIM_Job_Title='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]'
    PIM_Job_Title_list='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div[@role="listbox"]'
    PIM_Job_Title_value = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div[@role="listbox"]/div'

    PIM_Job_Category='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]'
    PIM_Job_Category_list ='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div[@role="listbox"]'
    PIM_Job_Category_value = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div[@role="listbox"]/div'

    PIM_Job_Sub_Unit='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/div/div/div[1]'
    PIM_Job_Sub_Unit_list='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/div/div[@role="listbox"]'
    PIM_Job_Sub_Unit_value = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/div/div[@role="listbox"]/div'

    PIM_Job_Location='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div/div[1]'
    PIM_Job_Location_list='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div[@role="listbox"]'
    PIM_Job_Location_value = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div[@role="listbox"]/div'

    PIM_Job_Employe_status='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[7]/div/div[2]/div/div/div[1]'
    PIM_Job_Employe_list='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[7]/div/div[2]/div/div[@role="listbox"]'
    PIM_Job_Employe_value = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[7]/div/div[2]/div/div[@role="listbox"]/div'
    PIM_Job_Emp_ContactDetail_toggle='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/label/span'
    PIM_Job_Contract_Start_Date='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[1]/div/div[2]/div/div/input'
    PIM_Job_Contratc_End_Date='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/div[2]/div/div[2]/div/div/input'
    PIM_Job_Save_Button='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button[text()=" Save "]'

    #PIM_Job_Terminate_Employment
    PIM_Job_Terminate_Employment='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button[text()=" Terminate Employment "]'
    PIM_Job_Terminate_Employment_form='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div'
    PIM_Job_Termination_Date='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[1]/div/div[2]/div/div/input'

    PIM_Job_Termination_Reason='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[2]/div/div[2]/div/div/div[1]'
    PIM_Job_Termination_Reason_List='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[2]/div/div[2]/div/div[@role="listbox"]'
    PIM_Job_Termination_Reason_value = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[2]/div/div[2]/div/div[@role="listbox"]/div'
    PIM_Job_Termination_Reason_Note='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[3]/div/div[2]/textarea'
    PIM_Job_Termination_Reason_Save_Button='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div/div/form/div[4]/button[text()=" Save "]'
    PIM_Job_TerminationOn_link='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/p'
    PIM_Job_Activate_Employment_button='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/button[text()=" Activate Employment "]'

    PIM_Salary_Tab = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[7]/a'
    PIM_Salary_AddButton='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button'
    PIM_Salary_Compensation='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input'
    PIM_Salary_PayGrade='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]'
    PIM_Salary_PayGrade_List='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div[@role="listbox"]'
    PIM_Salary_ParGrade_Value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div[@role="listbox"]/div'
    PIM_Salary_PayFrequency='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]'
    PIM_Salary_PayFrequency_List='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/div/div[@role="listbox"]'
    PIM_Salary_PayFrequency_value = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[3]/div/div[2]/div/div[@role="listbox"]/div'
    PIM_Salary_Currency='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]'
    PIM_Salary_Currency_List='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div[@role="listbox"]'
    PIM_Salary_Currency_Value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div[@role="listbox"]/div'
    PIM_Salary_Amount='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[5]/div/div[2]/input'
    PIM_Salary_DDDetails='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div/label/span'
    PIM_Salary_AccNo='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[1]/div/div[2]/input'
    PIM_Salary_AccType='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[2]/div/div[2]/div/div/div[1]'
    PIM_Salary_AccType_List='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[2]/div/div[2]/div/div[@role="listbox"]'
    PIM_Salary_AccType_Value = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[1]/div[2]/div/div[2]/div/div[@role="listbox"]/div'
    PIM_Salary_RountingNumber='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/div[1]/div/div[2]/input'
    PIM_Salary_DD_Amount='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div[2]/div[2]/div/div[2]/input'
    PIM_Salary_Save_Button='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button[text()=" Save "]'

    PIM_Salary_Saved_comp='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[2]/div'
    PIM_Salary_Saved_Amount='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div'
    PIM_Salary_Saved_Currecny='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[4]/div'
    PIM_Salary_Saved_Frequency='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[5]/div'
    PIM_Salary_Saved_DD_Amount='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/div[2]/div/div/div[6]/div'

    #PIM_Tax_Excemption_Selectors
    PIM_TaxExemp_Tab = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[8]/a'
    PIM_TaxExemp_Status = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]'
    PIM_TaxExemp_Status_List = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div[@role="listbox"]'
    PIM_TaxExemp_Status_Value = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/div/div[@role="listbox"]/div'
    PIM_TaxExemp_Exemption = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input'
    PIM_TaxExemp_State = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/div/div/div[1]'
    PIM_TaxExemp_State_List = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/div/div[@role="listbox"]'
    PIM_TaxExemp_State_Value = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/div/div[@role="listbox"]/div'
    PIM_TaxExemp_Status2 = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/div/div/div[1]'
    PIM_TaxExemp_Status2_List = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/div/div[@role="listbox"]'
    PIM_TaxExemp_Status2_Value = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/div/div[@role="listbox"]/div'
    PIM_TaxExemp_Exemptions = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input'
    PIM_TaxExemp_UnemploymentState = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[4]/div/div[2]/div/div/div[1]'
    PIM_TaxExemp_UnemploymentState_List = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[4]/div/div[2]/div/div[@role="listbox"]'
    PIM_TaxExemp_UnemploymentState_Value = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[4]/div/div[2]/div/div[@role="listbox"]/div'
    PIM_TaxExemp_WorkState = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[5]/div/div[2]/div/div/div[1]'
    PIM_TaxExemp_WorkState_List = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[5]/div/div[2]/div/div[@role="listbox"]'
    PIM_TaxExemp_WorkState_Value = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[5]/div/div[2]/div/div[@role="listbox"]/div'
    PIM_TaxExemp_Save_Button='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button[text()=" Save "]'


