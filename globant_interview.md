dict_records = {"user": "some_user", "pass"= "$%@deT"}

@pytest.fixture.set_up("[params]" scope= "class")
def set_up(request):
    driver initialize
    open browser with URL
    cls.variable = driver
    cls.data =dict_records
    yeild
        driver.quit()

@pytest
def test_login():
  	browser_instance = cls.varible
    data = cls.data
    input user = data.
    input pass
    click login
  
==================

Class A:
    def do_something():
      passs
      
Class B:
    def do_something():
      passs    

objA = A()

interface_dosomething(objA)

def interface_dosomething(operator):
    operator.dosomething()
    
    
===============
     
list1 = [
        {
            'name': 'XYZ',
            'certificates': 'java,php,python'
        },
        {
            'name': 'ABC',
            'certificates': 'java,c#'
        },
        {
            'name': 'LMN',
            'certificates': 'perl,JS,python'
        }
    ]
    
count_certs = list(lambda item["certificates"]: item["name"]=='LMN' , list1)[0].count(",")+1

==========================


input = ["10:20", "11:05", "12:10", "05:30", "01:45", "09:09"]
output = ["11:05", "09:09", "12:10", "10:20", "05:30", "01:45"]

temp_list =[]
for item in input:
    split_item = item.split(":")   # ["10","20"]
    item_sec_part = split_item[1]  # "20"
    temp_list.append(int(item_sec_part))    # [20, 05,...]

temp_list.sort()       # [05, 09, 10,..]

result = []
for item in temp_list:            [05, --]
     for item_input in input:			["10:20", -- ]
          if str(item) in item_input:      "05" in "10.20" ---
              result.append(item_input)
print(result)
    
==========================


Select  Name    Age  Salary
1.      XYZ  	30   15000
2.      ABC     40   10000
3.		LMN		35   20000

//td[text()='ABC']/parent::tr/td/child::input

==========================

driver.find_elements(By.XPATH, '//input')[0].send_keys("some text")