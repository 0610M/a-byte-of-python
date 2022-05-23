''''''

from Admin import *
from User import User

# Admin = User.Admin('lin', 'da', 12) #导入整个模块
# Admin.describle_user()
# Admin.privileges.show_privileges()

user1 = User('li', 'wang', 12)
user1.describle_user()
Admin = Admin('lin', 'da', 12)
Admin.privileges.show_privileges()
