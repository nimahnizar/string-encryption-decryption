# February 13 10:02pm

I have just gotten started with the project. So far, I have had to create 
the devlog which has been pretty easy. For tonight,my goal is to finish 
the initial commit for the devlog. I want to build a structure so I can 
work efficiently and finish this project on time. 

# March 3 8:05pm

Today my plan is to map out the structure of the project and see if i'm able to ad a description of the project in the readme.md as well as create a rough program for the logger. As each step is being checked off my task list for today, I will be coming back to log it. 

# March 3 8:26pm

I had to refer to a website makeareadme.com to learn how to draft a readme.md. However, once I looked at the template, it seemed relatively easy. I realized that a readme isn't the final description, but a draft. I added all the program names and their descriptions as well as my progress with regards to each program. 

# March 3 8:48pm

Reflection: 
I have successfully created a draft of README.md using the template. I now have a cler structure for the project and can start implementing the logger.py program. 

# March 3 9:24pm

I have now gotten started with the logger program. The language I will be using is Python, and am coding Pycharm. 

# March 4 9:38pm 

I got really sleepy last night and couldn't work on the logger program. However, I have now started working on it.From my understanding, the logger function accepts standard input, seperating the action and message, and attaches a timestamp in the specified format. I will be creating a test file to manually test the program and make sure it stops when QUIT is entered. 

# March 5 3:05pm

I finished working on the logger program. I drew inspiration from the general logger program on google and learned how to tweak it so it would work for this project. I tested it with a testlog.txt file and found that it was working as expected. It correctly displayed the timestamp as well as the action and message. 


# March 8 3:10pm

I plan on finishing the encryptor.py program this session. I did some example encryption and decryption on vigenere cipher websites online to get a general idea of the working of the program. 

# March 8 5:58pm

I began implementing the encryptor.py program. I created functions for both encryption and decryption using the Vigenere cipher. The functions loop through each character of the message and apply a shift based on the corresponding character in the key.


# March 8 8:15pm

I added command handling so the program can read input from standard input. The program now supports PASS, ENCRYPT, DECRYPT, and QUIT commands. PASS stores the key, while ENCRYPT and DECRYPT call their respective functions. The program also prints an error message when an unknown command is entered. 

# March 8 9:50pm

Upon testing the program, I noticed that the program was giving the output 'Password not set' or 'Error unknown command' despite entering the passkey. By the end of this session, I plan on fixing this bug and making sure the program passes all testcases. 

# March 8 10:01pm

It just occured to me that the reason the program was acting up was because it accepts 'PASS' as a command not 'PASSKEY'. I have made amendments so it accepts both. It seems to be working with the set of inputs provided in the document. 


# March 8 11:19pm

Today I worked on improving encryptor.py to make it more user-friendly. Originally, the program only accepted the command PASS to set the encryption key, but I realized that in the example testcase, PASSKEY was used. This caused the program to throw an "Unknown command" error. 

I had to carefully update the command handling logic to accept both PASS and PASSKEY without breaking existing functionality. This required debugging the input parsing and ensuring that the key was properly stored and recognized for subsequent ENCRYPT and DECRYPT commands. 

This was more challenging than I expected because it forced me to think about user behavior, edge cases, and how even small differences in input can cause the program to fail. After several rounds of testing, the program now correctly handles both commands and provides consistent, expected output for encryption and decryption.

# March 9 9:43am 

In this session, I plan on revising the entire project outline to understand how the 3 programs are expected to run in unison. The logger is mainly used for user interaction, which increases the complexity of the program. I plan on laying out a structure of the entire program before beginning to code. The menu system, input validation and runtime history will require precise thinking, which I plan on doing before starting. I feel like this step could be chsllenging since the smallest mistake can disrupt communication between processes and lead to failure. 

# March 9 9:08pm

While implementing, everything seemed straightforward at first. The structure of the driver matched the specifications, and I implemented helper functions for logging, validating letters-only input, and displaying the history. I also made sure to handle case-insensitivity and avoid storing passwords in the history. However, when I first tested the password command, I noticed that after entering a new password, the program did not display the expected `RESULT` output from `encryptor.py`. The driver was waiting indefinitely at the point where it tries to read the encryption program’s stdout. This is confusing because the driver code itself was correct; the issue was somewhere else in the pipeline. I aim to work on fixing this bug by the end of this session. 

# March 9 9:25pm

When I looked into the problem, I found that encryptor.py was actually setting the passkey correctly. The issue was that it wasn’t immediately sending the RESULT message back to the driver. Python keeps output in a buffer when using pipes, so the driver didn’t see the message right away. This made it seem like the program was stuck after entering a password, even though everything had worked behind the scenes. My plan for the following days is to make sure the repository has been zipped up correctly and the code passes multiple tests. 


# March 11 8:15pm

I conducted a number of manual tests after the implementation was finished to confirm accuracy, resilience, and adherence to the project requirements. Setting a password, encrypting strings, decrypting results, and viewing the history are examples of common use cases that I evaluated. Additionally, I tested a number of problem scenarios, such as trying to encrypt or decrypt without a password, using unfamiliar commands, and entering non-alphabetic input for strings and passwords.

By making sure stdout was correctly flushed, I confirmed that the driver received all responses from the encryption application right away. Additionally, I verified that passwords were never recorded to the log file or kept in history.Every test performed as anticipated, and in every case, the program ended smoothly.
