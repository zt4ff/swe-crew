from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import DirectoryReadTool, FileReadTool, WebsiteSearchTool

# from tools.custom_tool import MyCustomWriterTool
from src.dev.tools.custom_tool import MyCustomWriterTool
from textwrap import dedent

# tools
directory_read_tool = DirectoryReadTool(directory="./software")
file_read_tool = FileReadTool()
web_search_tool = WebsiteSearchTool()


@CrewBase
class DevCrew:
    """Dev crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    expected_output = "Implement the page code with appropriate mechanics."
    page_code = "a coffee shop website"

    @agent
    def senior_engineer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["senior_engineer_agent"],
            allow_delegation=False,
            verbose=True,
            memory=False,
            tools=[file_read_tool, directory_read_tool],
        )

    @agent
    def qa_engineer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["qa_engineer_agent"],
            allow_delegation=False,
            verbose=True,
            memory=False,
        )

    @agent
    def chief_qa_engineer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["chief_qa_engineer_agent"],
            allow_delegation=True,
            verbose=True,
            memory=True,
            tools=[file_read_tool, directory_read_tool],
        )

    @agent
    def writer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["writer_agent"],
            allow_delegation=False,
            verbose=True,
            memory=False,
            tools=[MyCustomWriterTool()],
        )

    @task
    def code_task(self):
        return Task(
            description=dedent(
                f"""You will create a page_code using HTML and JavaScript, these are the instructions:

            Instructions
            ------------
            {self.page_code}

            Your Final answer must be the full HTML and JavaScript code, only the HTML and JavaScript code and nothing else.
            """
            ),
            agent=self.senior_engineer_agent(),
            expected_output=self.expected_output,
        )

    @task
    def review_task(self):
        return Task(
            description=dedent(
                f"""\
                You are helping create a page_code using HTML and JavaScript, these are the instructions:

                Instructions
                ------------
                {self.page_code}

                Using the code you got, check for errors. Check for logic errors,
                syntax errors, missing imports, variable declarations, mismatched brackets,
                and security vulnerabilities.

                Your Final answer must be the full HTML and JavaScript code, only the HTML and JavaScript code and nothing else.
                """
            ),
            agent=self.qa_engineer_agent(),
            expected_output=self.expected_output,
        )

    @task
    def evaluate_task(
        self,
    ):
        return Task(
            description=dedent(
                f"""\
                You are helping create a page_code using HTML and JavaScript, these are the instructions:

                Instructions
                ------------
                {self.page_code}

                You will look over the code to insure that it is complete and
                does the job that it is supposed to do.

                Your Final answer must be the full HTML and JavaScript code, only the HTML and JavaScript code and nothing else.
                """
            ),
            agent=self.chief_qa_engineer_agent(),
            expected_output=self.expected_output,
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
