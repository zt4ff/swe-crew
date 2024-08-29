from crewai import Agent
from tools.file_tool import FileWriteTool

class Agents():
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
