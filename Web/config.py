class DataBaseConfig:
    mysql_Host = 'localhost'
    mysql_User = 'root'
    mysql_Password = 'Progynova'
    mysql_Database = 'OJ'

class LoginConfig:
    Login_Life_Time = 24 * 60 * 60 * 60 # s

class WebConfig:
    Problems_Each_Page = 20

class JudgeConfig:
    Judge_Each_Page = 15
    Max_Duration = 120
    Web_Server_Secret = 'Progynova'

class ProblemConfig:
    Max_Code_Length = 16384