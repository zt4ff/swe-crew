import os
from crewai import Agent, Crew, Process, Task
from tools.file_tool import FileWriteTool

from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


class WebsiteDevCrew:
    """Website Development Crew"""

    def __init__(self, project_description):
        self.project_description = project_description
        self.output_directory = "./project"

    def project_manager(self) -> Agent:
        return Agent(
            role="Project Manager",
            goal="Oversee the development of the entire website and ensure all components work together seamlessly",
            backstory="You are an experienced project manager with a strong background in web development.",
            allow_delegation=True,
            verbose=True,
        )

    def ui_ux_designer(self) -> Agent:
        return Agent(
            role="UI/UX Designer",
            goal=f"Design an intuitive and appealing user interface for the {self.project_description}",
            backstory="You are a creative UI/UX designer with a passion for creating beautiful and functional web experiences.",
            allow_delegation=False,
            verbose=True,
        )

    def frontend_developer(self) -> Agent:
        return Agent(
            role="Frontend Developer",
            goal="Implement the designed UI using HTML, CSS, and JavaScript",
            backstory="You are a skilled frontend developer with expertise in modern web technologies.",
            allow_delegation=False,
            verbose=True,
            tools=[FileWriteTool()],
        )

    def backend_developer(self) -> Agent:
        return Agent(
            role="Backend Developer",
            goal="Create a robust backend system to support the website's functionality",
            backstory="You are an experienced backend developer with knowledge of server-side technologies and APIs.",
            allow_delegation=False,
            verbose=True,
            tools=[FileWriteTool()],
        )

    def content_writer(self) -> Agent:
        return Agent(
            role="Content Writer",
            goal=f"Create compelling content for the {self.project_description}",
            backstory="You are a talented writer with experience in creating engaging web content.",
            allow_delegation=False,
            verbose=True,
        )

    def qa_engineer(self) -> Agent:
        return Agent(
            role="QA Engineer",
            goal="Ensure the website is bug-free and functions correctly across different devices and browsers",
            backstory="You are a detail-oriented QA engineer with a keen eye for identifying and resolving issues.",
            allow_delegation=False,
            verbose=True,
        )

    def design_ui_task(self):
        return Task(
            description=f"Design the user interface for the {self.project_description}. Include layouts for the home page, menu page, about us page, and contact page.",
            agent=self.ui_ux_designer(),
            expected_output="Detailed UI design specifications including color schemes, layout descriptions, and user flow diagrams.",
        )

    def write_content_task(self):
        return Task(
            description=f"Write engaging content for the {self.project_description}, including homepage copy, about us story, and .",
            agent=self.content_writer(),
            expected_output="Written content for all pages of the website, including SEO-optimized text and product descriptions.",
        )

    def develop_frontend_task(self):
        return Task(
            description=f"Implement the designed UI using HTML, CSS, and JavaScript. Create responsive layouts and interactive elements. Save all files in the {self.output_directory} folder.",
            agent=self.frontend_developer(),
            expected_output=f"HTML, CSS, and JavaScript files for all pages, saved in the {self.output_directory} folder.",
        )

    def develop_backend_task(self):
        return Task(
            description=f"Create a simple backend system to handle form submissions and manage a product inventory. Use a technology of your choice and save the files in the {self.output_directory}/backend folder.",
            agent=self.backend_developer(),
            expected_output=f"Backend code files and API endpoints documentation, saved in the {self.output_directory}/backend folder.",
        )

    def integrate_and_test_task(self):
        return Task(
            description=f"Integrate the frontend and backend components. Perform thorough testing of all website functionalities, including responsiveness and cross-browser compatibility.",
            agent=self.qa_engineer(),
            expected_output="Detailed test report including any identified issues and confirmation of successful integration.",
        )

    def finalize_project_task(self):
        return Task(
            description=f"Review all components of the website, ensure all files are properly organized in the {self.output_directory} folder, and create a final project report.",
            agent=self.project_manager(),
            expected_output=f"Final project report confirming completion of all tasks and proper organization of files in the {self.output_directory} folder.",
        )

    def run(self):
        crew = Crew(
            agents=[
                self.project_manager(),
                self.ui_ux_designer(),
                self.frontend_developer(),
                self.backend_developer(),
                self.content_writer(),
                self.qa_engineer(),
            ],
            tasks=[
                self.design_ui_task(),
                self.write_content_task(),
                self.develop_frontend_task(),
                self.develop_backend_task(),
                self.integrate_and_test_task(),
                self.finalize_project_task(),
            ],
            process=Process.sequential,
            verbose=True,
        )
        result = crew.kickoff()
        return result


if __name__ == "__main__":
    project = input("What Project will you like to build please: \n")
    website_crew = WebsiteDevCrew(project_description=project)
    result = website_crew.run()
    print(result)
