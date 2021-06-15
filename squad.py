playernames = ["b"]

main_loop = True

while main_loop:
  print("hey lads build a team, type the player that you want in the box mate")
  lw_is_found = False
  lw = ""
  while not lw_is_found: 
    lw = input("\nChoose a LW: ")
    if lw in playernames:
      print(lw + " has been added")
      lw_is_found = True
    else:
      print("Player is not found   ")


  rw_is_found = False
  rw = ""
  while not rw_is_found: 
    rw = input("\nChoose a RW: ")
    if lw in playernames:
      print(rw + " has been added")
      rw_is_found = True
    else:
      print("Player is not found")


  st_is_found = False
  st = ""
  while not st_is_found: 
    st = input("\nChoose a ST: ")
    if st in playernames:
      print(st + " has been added")
      st_is_found = True
    else:
      print("Player is not found")


  cam_is_found = False
  cam = ""
  while not cam_is_found: 
    cam = input("\nChoose a CAM: ")
    if cam in playernames:
      print(cam + " has been added")
      cam_is_found = True
    else:
      print("Player is not found")


  cm_is_found = False
  cm = ""
  while not cm_is_found: 
    cm = input("\nChoose a CM: ")
    if cm in playernames:
      print(cm + " has been added")
      cm_is_found = True
    else:
      print("\nPlayer is not found")


  cdm_is_found = False
  cdm = ""
  while not cdm_is_found: 
    cdm = input("\nChoose a CDM: ")
    if cdm in playernames:
      print(cdm + " has been added")
      cdm_is_found = True
    else:
      print("Player is not found")

      
  rb_is_found = False
  rb = ""
  while not rb_is_found: 
    rb = input("\nChoose a RB: ")
    if rb in playernames:
      print(rb + " has been added")
      rb_is_found = True
    else:
      print("Player is not found")
      

  lb_is_found = False
  lb = ""
  while not lb_is_found: 
    lb = input("\nChoose a LB: ")
    if lw in playernames:
      print(lb + " has been added")
      lb_is_found = True
    else:
      print("Player is not found")
      

  lcb_is_found = False
  lcb = ""
  while not lcb_is_found: 
    lcb = input("\nChoose a LCB: ")
    if lcb in playernames:
      print(lcb + " has been added")
      lcb_is_found = True
    else:
      print("Player is not found")
      
  rcb_is_found = False
  rcb = ""
  while not rcb_is_found: 
    rcb = input("\nChoose a RCB: ")
    if rcb in playernames:
      print(rcb + " has been added")
      rcb_is_found = True
    else:
      print("Player is not found")


  gk_is_found = False
  gk = ""
  while not gk_is_found: 
    gk = input("\nChoose a GK: ")
    if gk in playernames:
      print(gk + " has been added")
      gk_is_found = True
    else:
      print("Player is not found")


  print("\nThis is your final team:")
  print("LW: " + lw)
  print("ST: " + st)
  print("RW: " + rw)
  print("CAM: " + cam)
  print("CM: " + cm)
  print("CDM: " + cdm)
  print("LB: " + lb)
  print("RB: " + rb)
  print("LCB: " + lcb)
  print("RCB: " + rcb)
  print("GK: " + gk)


  make_another_team = True
  while make_another_team:
    go_again = input("\nWould you like to make another team? ")
    if go_again == "no":
      print("Bye")
      make_another_team = False
      main_loop = False
    elif go_again == "yes":
      make_another_team = False
    else:
      print("Answer must be yes or no")
      
      

      