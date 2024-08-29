import os
from crewai import Agent, Crew, Process, Task
from agents import Agents
from tasks import Tasks
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

agents = Agents()
tasks = Tasks()


class WebsiteDevCrew:
    """Website Development Crew"""

    def __init__(self, project_description):
        self.project_description = project_description
        self.output_directory = "./project"

    def run(self):
        crew = Crew(
            agents=[
                agents.project_manager(),
                agents.ui_ux_designer(),
                agents.frontend_developer(),
                agents.backend_developer(),
                agents.content_writer(),
                agents.qa_engineer(),
            ],
            tasks=[
                tasks.design_ui_task(agent=agents.ui_ux_designer),
                tasks.write_content_task(agent=agents.content_writer),
                tasks.develop_frontend_task(agent=agents.frontend_developer),
                tasks.develop_backend_task(agent=agents.backend_developer),
                tasks.integrate_and_test_task(agent=agents.qa_engineer),
                tasks.finalize_project_task(agent=agents.project_manager),
            ],
            process=Process.sequential,
            verbose=True,
        )
        result = crew.kickoff()
        return result


if __name__ == "__main__":
    print("==========================================")
    project = input("What Project will you like to build please: \n")
    website_crew = WebsiteDevCrew(project_description=project)
    result = website_crew.run()
    print(result)
