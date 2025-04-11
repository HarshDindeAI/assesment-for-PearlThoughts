from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_openai import AzureOpenAIEmbeddings
from langchain_openai import AzureChatOpenAI
import os
import numpy as np
from dotenv import load_dotenv
load_dotenv()
# Init embedding model
embedding_model = AzureOpenAIEmbeddings(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_EMBEDDING"),
)


# LangChain LLM setup
llm = AzureChatOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_CHAT"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION_CHAT"),
)

# Prompt template
system_template = """
You are a physician writing high-quality, professional LinkedIn posts on healthcare AI.
Your tone is thoughtful and optimistic about AI as a tool that helps — not replaces — clinicians.
Make sure to reflect these perspectives:
{perspectives}
"""

human_template = """
Given this article summary:

{article_summary}

Write a 200–250 word LinkedIn post that reflects the client's philosophy and perspective.
"""

prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(system_template),
    HumanMessagePromptTemplate.from_template(human_template)
])


def generate_physician_linkedin_post(article_summary: str, perspectives: list[str]):

    """
    Generate a physician's LinkedIn post based on an article summary and perspectives.

    This function uses a language model to generate a LinkedIn post that reflects a client's
    philosophy and perspective on healthcare AI. It constructs the message from the given article
    summary and perspectives, and then uses an embedding model to compute the semantic similarity
    between the generated post and the provided perspectives. The average similarity score is
    calculated and returned as a confidence score.

    Args:
        article_summary (str): A brief summary of the article to base the LinkedIn post on.
        perspectives (list[str]): A list of perspectives that should be reflected in the post.

    Returns:
        dict: A dictionary containing the generated LinkedIn post and a confidence score indicating
            how well the post aligns with the given perspectives.
    """

    perspective_text = "\n".join([f"- {p}" for p in perspectives])
    messages = prompt.format_messages(
        article_summary=article_summary,
        perspectives=perspective_text
    )

  
    response = llm.invoke(messages)
    post = response.content.strip()


    post_embedding = embedding_model.embed_query(post)
    perspective_embeddings = embedding_model.embed_documents(perspectives)
    scores = [np.dot(post_embedding, p_emb) / (np.linalg.norm(post_embedding) * np.linalg.norm(p_emb)) for p_emb in perspective_embeddings]
    avg_score = round(sum(scores) / len(scores), 2)
    return {
        "linkedin_post": post,
        "confidence_score": avg_score
    }
