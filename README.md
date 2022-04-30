# Title Swap

This Python3 script searches a .docx file for 'PLACEHOLDER' and replaces it with the provided job title.

## SETUP

1) Create a 'dist' folder in this project directory.
2) In the dist directory, create a copy of your .docx resume and name it 'placeholder_resume.docx'

A succesful setup should look like this
-- /dist
  -- placeholder_resume.docx
-- /resumes
-- app.py
-- README.md

## Running the script

The script requires 2 arguments
1) New job title
2) New file name (without the extension)

Example:
    python3 app.py 'Frontend Engineer' Ryan_M_Resume

This will create a Ryan_M_Resume.docx file where PLACEHOLDER is replaced with 'Frontend Engineer'. The file is saved in the resumes directory, packaged in a directory with the same name as the job title.

-- /resumes
  -- /Frontend_Engineer
    -- Ryan_M_Resume.docx