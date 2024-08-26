import os
from crewai_tools import BaseTool


class MyCustomWriterTool(BaseTool):
    name: str = "File Write Tool"
    description: str = "A tool for writing contents to files"

    output_dir: str = "software"

    def _run(self, file_name: str, content: str) -> str:
        os.makedirs(self.output_dir, exist_ok=True)

        file_path = os.path.join(self.output_dir, file_name)

        try:
            with open(file_path, "w") as file:
                print(f"Writing to {file_path}")
                file.write(content)
        except Exception as e:
            return f"Error writing to file '{file_name}': {str(e)}"

        return f"File '{file_name}' written successfully."
