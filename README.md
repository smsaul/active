# active
active projects

These are all written for Python 3.

Although these programs are a work in progress, all are currently in a functional state considering reasonable input. If crazy stuff is put in, crazy things will probably still happen.

drugcalc - This is a library of functions to calculate drip rates of medicaiton infusions.

hasher - This is my most complex project yet. This generates a four-word password for a named user, stores the salted and hashed password in a SQL database, and can then authenticate a user based on this database. Protection from code injection is in place, and no plain-text passwords are avaliable beyond the prompt from the commandline when a new password is created. This code is structured to be used in a larger application easily.

meal_planner - This picks random meals my significant other and I like to prepare for busy weeks. It pulls four random meals and spreads them out over a few days. The simple version is designed to be simple and is considered complete. The complex version is structured using dictionaries. Future plans intend to leverage the dictionary structure in order to make shopping lists from the random draws.

medpump - This builds off the drugcalc calculations by using them in a command line interface to program a simulated medication pump. Predefined medications are stored in the program and allow for safe dose ranges, and custom infusion information is possible as well. Once the parameters of the infusion are defined, the console prints the word "drip" at the rate a medicaiton infusion would "drip" in a real infusion setup.

paycheck_calculator - this is a simple tool to estimate an after-taxes paycheck amount, including calculations for 1.5x overtime. The estimated tax rate can be easily changed in the code to fit an individual's amount, and is accurate within a dollar with my paycheck. Note that the actual figures have been edited for privacy's sake.
