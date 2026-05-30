from agents import Agent, Runner
from connection import config

faq_agent = Agent(
    name="FAQ Agent", instructions="You are a helpful FAQ bot. Answer any questions asked"
)

questions=["What's your name?", "What can you do?","What is your main function?" ]


def main():
    for i in range(len(questions)):
        result = Runner.run_sync(
            faq_agent, input=questions[i], run_config=config
        )
        print(result.final_output)

    print("Hello from practice-assignments!")


if __name__ == "__main__":
    main()
