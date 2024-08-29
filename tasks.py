from crewai import Task


class Tasks:
    def __init__(self, project_description):
        self.project_description = project_description

    def design_ui_task(self, agent):
        return Task(
            description=f"Design the user interface for the {self.project_description}. Include layouts for the home page, menu page, about us page, and contact page.",
            agent=agent,
            expected_output="Detailed UI design specifications including color schemes, layout descriptions, and user flow diagrams.",
        )

    def write_content_task(self, agent):
        return Task(
            description=f"Write engaging content for the {self.project_description}, including homepage copy, about us story, and .",
            agent=agent,
            expected_output="Written content for all pages of the website, including SEO-optimized text and product descriptions.",
        )

    def develop_frontend_task(self, agent):
        return Task(
            description=f"Implement the designed UI using HTML, CSS, and JavaScript. Create responsive layouts and interactive elements. Save all files in the {self.output_directory} folder.",
            agent=agent,
            expected_output=f"HTML, CSS, and JavaScript files for all pages, saved in the {self.output_directory} folder.",
        )

    def develop_backend_task(self, agent):
        return Task(
            description=f"Create a simple backend system to handle form submissions and manage a product inventory. Use a technology of your choice and save the files in the {self.output_directory}/backend folder.",
            agent=agent,
            expected_output=f"Backend code files and API endpoints documentation, saved in the {self.output_directory}/backend folder.",
        )

    def integrate_and_test_task(self, agent):
        return Task(
            description=f"Integrate the frontend and backend components. Perform thorough testing of all website functionalities, including responsiveness and cross-browser compatibility.",
            agent=agent,
            expected_output="Detailed test report including any identified issues and confirmation of successful integration.",
        )

    def finalize_project_task(self, agent):
        return Task(
            description=f"Review all components of the website, ensure all files are properly organized in the {self.output_directory} folder, and create a final project report.",
            agent=agent,
            expected_output=f"Final project report confirming completion of all tasks and proper organization of files in the {self.output_directory} folder.",
        )
