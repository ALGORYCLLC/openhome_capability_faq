import asyncio
import json
import os

from src.agent.capability import MatchingCapability
from src.main import AgentWorker
from src.agent.capability_worker import CapabilityWorker

FIRST_PROMPT = "Please ask a question related to Openhome, If you want to exit please say Exit Capability."
MAIN_PROMPT = """Here are some frequently asked questions and their answers:\n {faq_context} \n\n
            User's question: {user_question} \n
            Don't repeat the question in your response
            Please provide a relevant and relatively shorter (maximum 3 to 4 sentences long) but full of details answer or state that no relevant information is found if context is cintext has little or noformation realted to user's question."""
SORRY_PROMPT = "I'm sorry, but no relevant information is found. Please contact a support person."
FEEDBACK_PROMPT = "Thank you for using the FAQ capability! How would you rate your experience? Please provide your feedback."
EXITING_PROMPT = "Feedback recorded, resuming normal flow"

class FaqtestingCapability(MatchingCapability):
    worker: AgentWorker = None
    capability_worker: CapabilityWorker = None
    faqs: list = []

    @classmethod
    def register_capability(cls) -> "MatchingCapability":
        with open(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json"),
        ) as file:
            data = json.load(file)

        return cls(
            unique_name=data["unique_name"],
            matching_hotwords=data["matching_hotwords"],
        )

    def load_faqs(self):
        # Load FAQs from OpenHome.md file
        openhome_md_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "OpenHome.md")
        if not os.path.exists(openhome_md_path):
            self.worker.editor_logging_handler.info(f"OpenHome.md file not found at path: {openhome_md_path}")
            return

        with open(openhome_md_path) as file:
            openhome_content = file.read()
            # self.worker.editor_logging_handler.info(f"OpenHome.md content: {openhome_content}")

        self.faqs = openhome_content.split("\n\n")  # Split FAQs based on blank lines
        # self.worker.editor_logging_handler.info(f"Extracted FAQs: {self.faqs}")

    async def get_gpt_response(self, prompt: str, history: list = []) -> str:
        # Replace with actual GPT call logic
        response = self.capability_worker.text_to_text_response(prompt, history)
        return response

    async def handle_user_query(self):
        """
        Handle user queries in a loop until the user decides to exit.
        """
        # Load FAQs before starting the loop
        self.load_faqs()

        while True:
            await self.capability_worker.speak(FIRST_PROMPT)
            user_question = await self.capability_worker.user_response()
            self.worker.editor_logging_handler.info("user question: %s" %user_question)

            if "exit" in user_question.lower():
                self.worker.editor_logging_handler.info("Inside exit if")
                await self.get_feedback()
                break

            # Prepare prompt with FAQs for context
            faq_context = "\n".join(self.faqs)
            # self.worker.editor_logging_handler.info("context: %s" % faq_context)
            prompt = MAIN_PROMPT.format(faq_context=faq_context, user_question=user_question)

            gpt_response = await self.get_gpt_response(prompt)

            if "no relevant information" in gpt_response.lower():
                await self.capability_worker.speak(SORRY_PROMPT)
            else:
                await self.capability_worker.speak(gpt_response)

    async def get_feedback(self):
        """
        Get feedback from the user upon exiting.
        """
        feedback_question = FEEDBACK_PROMPT
        await self.capability_worker.speak(feedback_question)
        feedback_response = await self.capability_worker.user_response()
        # You can handle the feedback response as needed
        await self.capability_worker.speak(EXITING_PROMPT)
        self.capability_worker.resume_normal_flow()

    def call(self, worker: AgentWorker):
        # Initialize the worker and capability worker
        self.worker = worker
        self.capability_worker = CapabilityWorker(self.worker)

        # Start handling user queries and wait for it to complete
        asyncio.create_task(self.handle_user_query())
