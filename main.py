#-m venv flaskvenv
#>flaskvenv\Scripts\activate.bat
from hello_world.init import app

#init in website folder becomes python package, when import folder name, will by default run all things in init file,
# so, can import anything in init file like create_app

if __name__ == "__main__": #only run when run this file directly, not run when import
    app.run(debug=True)  #when make chg to code, auto re-run server, avoid keep rerun code, need remove ltr