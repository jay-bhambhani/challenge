# challenge
## Setup
Just run docker-compose up! You can run the script ./scripts/test_challenge.py.
Insert a record with:
 ```
 python scripts/test_challenge.py question -c create -n "does this also work" -t test
 ```
 Update it:
 ```
  python scripts/test_challenge.py question -c update -n "does this work too?" -q <question id returned from above response>
 ```
 And view history
 ```
   python scripts/test_challenge.py history <question id returned from above response>
 ```
## Summary
### What went well
It overall wasn't a super hard task
### What didn't go well
I think I struggled to build models that would account for the structure of the conversations. Should have asked for more info here
### What would I improve
Definitely spend more time getting a thorough download of requirements. Also I definitely would improve my folder structure and setup work (I know I slapped it together instead of diligently building things out the way I would have liked)
