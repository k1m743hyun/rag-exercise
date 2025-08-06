from numpy import dot
from numpy.linalg import norm
from langchain_openai import OpenAIEmbeddings

os.environ['OPENAI_API_KEY'] = ''

def cos_sim(A, B):
    return dot(A, B) / (norm(A) * norm(B))

if __name__ == '__main__':
    embedding_model = OpenAIEmbeddings()

    embeddings = embedding_model.embed_documents(
        [
            '안녕하세요!',
            '어! 오랜만이에요',
            '이름이 어떻게 되세요?',
            '날씨가 추워요',
            'Hello LLM!'
        ]
    )
    #print(len(embeddings))
    #print(len(embeddings[0]))
    #print(embeddings[0][:20])

    embedded_query = embedding_model.embed_query('첫인사를 하고 이름을 물어봤나요?')
    #print(embedded_query[:5])

    for embedding in embeddings:
        print(cos_sim(embedding, embedded_query))
