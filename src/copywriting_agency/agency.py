import os
from agency_swarm import Agency, set_openai_key
# from agency_swarm.tools.send_message import SendMessage
from .Copywriter import Copywriter_test
# from datetime import datetime, timezone
# # from .utils import load_config
from dotenv import load_dotenv

load_dotenv()

# # # loads API keys from config.yaml
# # load_config(file_path="./config.yaml")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
set_openai_key(OPENAI_API_KEY)



# def get_current_utc_datetime():
#     now_utc = datetime.now(timezone.utc)
#     current_time_utc = now_utc.strftime("%Y-%m-%d %H:%M:%S %Z")
#     return current_time_utc

# manager_instructions_with_datetime = manager_instructions.format(datetime=get_current_utc_datetime())

copywriter = Copywriter_test()


# Create an agency with the agents
agency = Agency([copywriter],
                #  [copywriter, seooptimizer],
                #  [copywriter, complianceandreview],
                #  [seooptimizer, complianceandreview],
                #  [seooptimizer, copywriter],
                #  [complianceandreview, contentstrategymanager],
                #  [complianceandreview, copywriter]],
                # send_message_tool_class=SendMessage,
                shared_instructions='./agency_manifesto.md',  # shared instructions for all agents
                # max_prompt_tokens=25000,  # default tokens in conversation for all agents
                temperature=0.3,  # default temperature for all agents
                )

if __name__ == '__main__':
    agency.demo_gradio()
    # agency.run_demo()