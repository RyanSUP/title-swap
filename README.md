# Title Swap
The goal of this project was to streamline the resume editing process for those darn ATS robots.

This Python3 script searches a .docx file for 'PLACEHOLDER' and replaces it with the provided job title and neatly stores the new document for future use.

🚨 Currently, the job title (PLACEHOLDER) needs to be on its own line 🚨

## SETUP

1) Create a 'dist' folder in this project directory.
2) In the dist directory, create a copy of your .docx resume and name it 'placeholder_resume.docx'
3) Replace the job title in placeholder_resume.docx with 'PLACEHOLDER' (no quotes)

A succesful setup should look like this
```
-- /dist
 -- placeholder_resume.docx
-- /resumes
-- app.py
-- README.md
```

## Running the script

The script requires 2 arguments
1) New job title
2) New file name (without the extension)

Example:
    python3 app.py 'Frontend Engineer' Ryan_M_Resume

This will create a Ryan_M_Resume.docx file where PLACEHOLDER is replaced with 'Frontend Engineer'. The file is saved in the resumes directory, packaged in a directory with the same name as the job title.
```
  -- /resumes
    -- /Frontend_Engineer
      -- Ryan_M_Resume.docx
```