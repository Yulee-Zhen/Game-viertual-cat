def show(status): 
    if status == 'cat':
        figure = r'''
               meow~~~
   /\     /\
  /  `---'  \
 {   O   O   }         _
 ~~=   W    =~~      / /
   { ````` }-````、  \ \
  {         }     \__/ /
   {  \ /  }`\   )____/
    \  V  )  / _/
     \ | /(_/
     (_Y_)
 '''
    elif status == 'confuse':
        figure = r'''                  
   /\     /\   ??
  /  `---'  \
 {   ?   ?   }         
 ~~=   W    =~~  
     `````   
 '''
    elif status == 'feed':
        figure = r'''                  
   /\     /\   Yammy!
  /  `---'  \
 {   ^   ^   }        
 ~~=   W    =~~  
     `````   
 '''

    elif status == 'outdoor':
        figure = r'''
   ☀️☁️☁️
        /\_/\     🦋
       ( ◕ᴥ◕ )━☆
🌸      /   \  /
 🌳    /     \/   🌳🌳
🌳🌻🌳~≈~≈~≈~≈~🌳🌻🌳🌷
'''

    print(figure)

        