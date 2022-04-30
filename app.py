import os   # For creating folders
import sys  # For accessing command line arguments
import docx # For manipulating docx files

new_job_title = sys.argv[1]
document_name = sys.argv[2]
directory_name = new_job_title.replace(' ', '_')
output_path = f'./resumes/{directory_name}/'
file_extenstion = '.docx'

doc = docx.Document('./dist/placeholder_resume.docx')

for paragraph in doc.paragraphs:
  for run in paragraph.runs:
    if run.text == 'PLACEHOLDER':
      run.text = new_job_title
      os.mkdir(output_path)
      doc.save(f'{output_path}{document_name}{file_extenstion}')
      break

