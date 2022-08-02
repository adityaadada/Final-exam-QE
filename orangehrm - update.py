import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

        
    def test_a_1_admin(self): 
        # steps
        browser = self.browser #buka web browser 
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login") #web
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin")#teks
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")#teks
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() #klik
        time.sleep(1)
        browser.find_element(By.ID,"menu_admin_viewAdminModule").click() #klik
        time.sleep(1)
        browser.find_element(By.ID,"searchSystemUser_userName").send_keys("Garry.White")#teks
        time.sleep(1)        
        browser.find_element(By.ID,"searchBtn").click() #klik
        time.sleep(1)
        # validasi
        response_data = browser.find_element(By.XPATH,'//*[@id="resultTable"]/tbody/tr/td[2]/a').text
        
        self.assertIn("Garry.White", response_data)

    
    def test_a_2_pim(self): 
        # steps
        browser = self.browser #buka web browser 
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login") #web
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin")#teks
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")#teks
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() #klik
        time.sleep(1)
        browser.find_element(By.ID,"menu_pim_viewPimModule").click() #klik
        time.sleep(1)
        browser.find_element(By.ID,"empsearch_employee_name_empName").send_keys("Garry White")#teks
        time.sleep(1)        
        browser.find_element(By.ID,"searchBtn").click() #klik
        time.sleep(1)
        
        

        # validasi
        response_data = browser.find_element(By.XPATH,'//*[@id="resultTable"]/tbody/tr/td[3]/a').text

        self.assertIn("Garry", response_data)



    def test_a_3_leave(self): 
        # steps
        browser = self.browser #buka web browser 
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login") #web
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin")#teks
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")#teks
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() #klik
        time.sleep(1)
        browser.find_element(By.ID,"menu_leave_viewLeaveModule").click() #klik
        time.sleep(1)
        browser.find_element(By.ID,"leaveList_txtEmployee_empName").send_keys("Garry White")#teks
        time.sleep(1)        
        browser.find_element(By.ID,"btnSearch").click() #klik
        time.sleep(1)
    
        # validasi
        response_data = browser.find_element(By.XPATH,'//*[@id="resultTable"]/tbody/tr[1]/td[2]/a').text

        self.assertIn("Garry White", response_data)


    def test_a_4_time(self): 
        # steps
        browser = self.browser #buka web browser 
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login") #web
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin")#teks
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")#teks
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() #klik
        time.sleep(1)
        browser.find_element(By.ID,"menu_time_viewTimeModule").click() #klik
        time.sleep(1)
        browser.find_element(By.ID,"menu_admin_ProjectInfo").click() #klik
        time.sleep(1)
        browser.find_element(By.ID,"menu_admin_viewProjects").click() #klik
        time.sleep(1)
        browser.find_element(By.ID,"searchProject_customer").send_keys("Internal")#teks
        time.sleep(1)        
        browser.find_element(By.ID,"btnSearch").click() #klik
        time.sleep(1) 
        # validasi
        response_data = browser.find_element(By.XPATH,'//*[@id="resultTable"]/tbody/tr[1]/td[3]/a').text

        self.assertIn("General HR Tasks", response_data)



    def test_a_5_recruitmen(self): 
        # steps
        browser = self.browser #buka web browser 
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login") #web
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin")#teks
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")#teks
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() #klik
        time.sleep(1)
        browser.find_element(By.ID,"menu_recruitment_viewRecruitmentModule").click() #klik
        time.sleep(1)
        browser.find_element(By.ID,"candidateSearch[candidateName]").send_keys("Garry White")#teks
        time.sleep(1)        
        browser.find_element(By.ID,"btnSrch").click() #klik
        time.sleep(1)
        # validasi
        response_data = browser.find_element(By.XPATH,'//*[@id="resultTable"]/tbody/tr[4]/td[3]/a').text

        self.assertIn("Garry White", response_data)

    def test_a_6_myinfo(self): 
        # steps
        browser = self.browser #buka web browser 
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login") #web
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin")#teks
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")#teks
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() #klik
        time.sleep(1)
        browser.find_element(By.ID,"menu_pim_viewMyDetails").click() #klik
        time.sleep(1)        
        browser.find_element(By.ID,"btnSave").click() #klik
        time.sleep(1)
        browser.find_element(By.ID,"personal_txtEmpFirstName").clear()
        time.sleep(1)
        browser.find_element(By.ID,"personal_txtEmpFirstName").send_keys("Tester")#teks
        time.sleep(1)
        browser.find_element(By.ID,"btnSave").click() #klik
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"personal_txtEmpFirstName").text
        self.assertIn("Tester", response_data)

    def test_a_7_performance(self): 
        # steps
        browser = self.browser #buka web browser 
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login") #web
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin")#teks
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")#teks
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() #klik
        time.sleep(1)
        browser.find_element(By.ID,"menu__Performance").click() #klik
        time.sleep(1) 
        browser.find_element(By.ID,"menu_performance_viewEmployeePerformanceTrackerList").click() #klik
        time.sleep(1) 
        # validasi
        response_data = browser.find_element(By.XPATH,'//*[@id="resultTable"]/thead/tr/th[1]/span').text

        self.assertIn("Employee", response_data)

    def test_a_8_dashboard(self): 
        # steps
        browser = self.browser #buka web browser 
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login") #web
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin")#teks
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")#teks
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() #klik
        time.sleep(1)
        browser.find_element(By.ID,"menu_dashboard_index").click() #klik
        time.sleep(1)



        # validasi
        response_data = browser.find_element(By.XPATH,'//*[@id="dashboard-quick-launch-panel-menu_holder"]/table/tbody/tr/td[1]/div/a/span').text

        self.assertIn("Assign Leave", response_data)


    def test_a_9_directory(self): 
        # steps
        browser = self.browser #buka web browser 
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login") #web
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin")#teks
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")#teks
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() #klik
        time.sleep(1)
        browser.find_element(By.ID,"menu_directory_viewDirectory").click() #klik
        time.sleep(1)
        browser.find_element(By.ID,"searchDirectory_emp_name_empName").send_keys("Garry White")#teks
        time.sleep(1)        
        browser.find_element(By.ID,"searchBtn").click() #klik
        time.sleep(1)    


        # validasi
        response_data = browser.find_element(By.XPATH,'//*[@id="resultTable"]/tbody/tr[2]/td[2]/ul/li[2]').text

        self.assertIn("HR Associate", response_data)


    def test_a_10_maintenance(self): 
        # steps
        browser = self.browser #buka web browser 
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login") #web
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin")#teks
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")#teks
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() #klik
        time.sleep(1)

        browser.find_element(By.ID,"menu_maintenance_accessEmployeeData").click() #klik
        time.sleep(1)
        browser.find_element(By.ID,"confirm_password").send_keys("admin123")#teks
        time.sleep(1)        
        browser.find_element(By.XPATH,'//*[@id="frmPurgeEmployeeAuthenticate"]/div/div/input').click() #klik
        time.sleep(1)    
        browser.find_element(By.ID,"employee_empName").send_keys("Garry White")#teks
        time.sleep(1)        
        browser.find_element(By.XPATH,'//*[@id="frmAccessEmployeeData"]/div/div/input').click() #klik
        time.sleep(1)    

  
        # validasi
        response_data = browser.find_element(By.ID,'full_name').text

        self.assertIn("Garry White", response_data)


    def test_a_11_buzz(self): 
        # steps
        browser = self.browser #buka web browser 
        browser.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login") #web
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin")#teks
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123")#teks
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() #klik
        time.sleep(1)
        browser.find_element(By.ID,"menu_buzz_viewBuzz").click() #klik
        time.sleep(1)
        browser.find_element(By.ID,"rightBarHeadingAnniv").click() #klik
        time.sleep(1)

        # validasi
        response_data = browser.find_element(By.ID,"name2").text

        self.assertIn(" No Upcoming Anniversaries For Next 30 Days ", response_data)


    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()