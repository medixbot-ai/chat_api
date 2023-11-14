# API Functionality Overview

1. Retrieve a list of job positions based on the provided project description. (Redirect to OpenAI)
2. Generate job advertisements tailored to the specified position for recruitment purposes. (Redirect to OpenAI)
3. Compile a list of employees with matching percentages for a given job position using Pinecone:
   - Identify all employees who closely match the job requirements.
   - Optionally, specify the top 'n' employees with the highest matching percentages.

#endpoint
/analyze
- request format:
	curl -X POST -H "Content-Type: application/json" -d '{"text": "find of top 3 employees names who are more mached to the software developer job"}' http://localhost:5000/analyze
- response format:
{
  "generated_text": "\nIt is not possible to answer this question without prior knowledge of the software job's requirements and Sayali Patil's skills.", 
  "input_text": "Identify all  employees by their names whose skills align best with the requirements of the software job.", 
  "intention": "Listing Top Employee Names"
}

/set_project
	- request format
	   curl -X POST -H "Content-Type: application/json" -d '{"project": "Project Title: CloudBoost\nDescription:\nWelcome to CloudBoost, the ultimate cloud-based project management solution designed to streamline your workflow and elevate your team's productivity. CloudBoost is a SaaS platform that empowers businesses of all sizes to efficiently manage projects, collaborate seamlessly, and achieve project milestones with ease."}' http://localhost:5000/set_project
	- response format
		 {"response":"success"}

# Notes:
Add openai key 



