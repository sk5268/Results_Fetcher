# Results_Fetcher
Fetch Results from the univeristy's result server without manual intervention &amp; generate insights

This project was specifically built for Osmania University's server.
Although, idea is the same if your Uni's results are not password protected.

[output.pdf](https://github.com/user-attachments/files/18002560/output.pdf)

# Background

Well, everybody want's to check their position in their class, also it's a big mess to go through each and every roll number manually.
I got lazy enough to automate the boring part and hence this project was born.
The reason I didn't build a UI to it is because it would be an overkill.
Hardly used once or twice a semseter, UI was totally unnecessary. \
Apart from rankings, you can also calculate a few statistics namely, average GPA and number of students passed, failed & withheld.


# Requirements
1. reportlab python package (https://pypi.org/project/reportlab/)
2. re & requests (core python packages)

# Usage
1. change the variable `purl` to the live results link.
2. change the `r_start` & `r_end` variables with starting and ending roll numbers.
3. Run the script.

# Note
Last used: July 2024 \
Status: Working as intended

# Upcoming Features:
1. Relative GPA
2. Remove unnecessary disk writes and reads.
