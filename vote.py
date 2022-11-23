def Main():
  candidate1=input("enter 1st candidate name")
  candidate2=input("enter 2nd candidate name")
  cand1_votes=0
  cand2_votes=0
  voters_id=[101,102,103,104,105,106]
  no_of_voters=len(voters_id)
  print("no of voters",no_of_voters)
  voted=[]
  while True:
    if voters_id==[]:
          print("voting is over")
          if cand1_votes>cand2_votes:
            print(f"{candidate1}won the election with{cand1_votes}")
          elif cand2_votes>cand1_votes:
            print(f"{candidate2}won the election with {cand2_votes}")
          elif cand1_votes==cand2_votes:
            print("tied")
          break
    else:
          age = int(input("Enter ur age"))
          if age>=18:
            voter=int(input("enter ur id"))
            if voter in voted:
                print("u already voted")
            else:
                if voter in voters_id:
                    print(f"1.{candidate1} \n2.{candidate2}")
                    choice=int(input("enter ur choice"))
                if choice==1:
                        cand1_votes+=1
                        print(f"you voted{candidate1}")
                        voters_id.remove(voter)
                        voted.append(voter)
                elif choice==2:
                      cand2_votes+=1  
                      print(f"you voted{candidate2}")
                      voters_id.remove(voter)
                      voted.append(voter)
                else:
                  print("you are not allowed to vote ")
          else:
            print("you are a minor")

def Verify():
  user = input("Enter ur UserId")
  passcode = int(input("Enter the password"))

  id = "bharat07"
  code = 5551

  if(user == id and passcode == code):
    Main()
  elif(user == id and passcode != code):
    print("Password is Wrong")
    Verify()
  elif(user != id and passcode == code):
    print("UserID is Wrong")
    Verify()
  else:
    exit()
  
Verify()