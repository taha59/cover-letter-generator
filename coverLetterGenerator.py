from content import TONE
from config import RESUME_PATH, COVER_LETTER_PATH, COVER_LETTER_TEMPLATE_PATH, JOB_DESCRIPTION_PATH, COMPANY_DESCRIPTION_PATH
from docParser import read_docx_text, create_cover_letter, extract_text
from aiPrompt import send_AI_prompt
from datetime import datetime


resume_text = read_docx_text(RESUME_PATH)
cover_letter_template_text = read_docx_text(COVER_LETTER_TEMPLATE_PATH)

#extract company and job description from text files
company_description = extract_text(COMPANY_DESCRIPTION_PATH)
job_description = extract_text(JOB_DESCRIPTION_PATH)

coverLetterGeneratePrompt = f"""You are a cover letter generator. Your task is to create {TONE} and concise cover letter body.

To compose a compelling cover letter, you must scrutinize the job description for key 
qualifications. Begin with a succinct introduction about the candidate's identity and career 
goals. Highlight skills aligned with the job, underpinned by tangible examples. Incorporate 
details about the company, emphasising its mission or unique aspects that align with the 
candidate's values. Conclude by reaffirming the candidate's suitability, inviting further 
discussion. Use job-specific terminology for a tailored and impactful letter, maintaining a 
{TONE} style suitable for the job role. Please provide your response in under 
350 words.

This is my current resume. <Start of resume> {resume_text} </end of resume>

Here is the job description for the job I'm applying for:
 <job description> {job_description} </job description> and here is a description of the company:
   <company >description> {company_description} </company description>

Follow this template:
{cover_letter_template_text}

ONLY write the part that will replace <content> inside the template.
DO NOT include greetings (e.g., 'Dear Hiring Manager') or closing remarks (e.g., 'Sincerely').
Those are already handled separately in the template.
Only output the text that goes inside <content>. Omit everything else.
"""

extractInfoPrompt = f"""
Given the company description and job description, your task is to extract the following fields:

1. Company name  
2. City, State (location)

Job description: {job_description}  
Company description: {company_description}

Respond with the extracted information **in a single line**, formatted as:

CompanyName-City, State

For example:  
Google-Tampa, FL

If you cannot extract a field, write 'NULL' instead of guessing.
"""

current_date = datetime.now()
formatted_date = current_date.strftime("%B %d, %Y")

# extract location, company name from the job and company description
extracted_info = send_AI_prompt(extractInfoPrompt)
split_info = [item.strip().replace('\n', '') for item in extracted_info.split('-')]
split_info.append(formatted_date)
print(split_info)

#create customized cover letter content using AI
cover_letter_content = send_AI_prompt(coverLetterGeneratePrompt)

#creates a doc file for the cover letter
create_cover_letter(COVER_LETTER_TEMPLATE_PATH, COVER_LETTER_PATH, cover_letter_content, split_info)